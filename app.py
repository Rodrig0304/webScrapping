from flask import Flask, render_template, request, session, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
import requests
import mysql.connector

from bs4 import BeautifulSoup

app = Flask(__name__)
app.secret_key = "secret_key"

# config de base de datos MySQL
try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="empleosallinstante"
    )
    message = "Se conectó"
    mycursor = con.cursor()

except mysql.connector.Error as e:
    message = "No se conectó"

# método para registrar usuario en BD
def sign_up_user(username, email, password):
    hashedPassword = generate_password_hash(password)
    query = "INSERT INTO Usuario (nombreUsuario, correoElectronico, contraseñaUsuario) VALUES (%s, %s, %s);"
    values = (username, email, hashedPassword)
    mycursor.execute(query, values)
    con.commit()

# método para ingresar sesion con usuario existente en BD
def login_user(email, password):
    try:
        query = "SELECT nombreUsuario, contraseñaUsuario FROM Usuario WHERE correoElectronico = %s"
        mycursor.execute(query, (email,))
        result = mycursor.fetchone()

        if result and check_password_hash(result[1], password):
            return result[0]
    except mysql.connector.Error as e:
        print(f"Error en verificacion de usuario: {e}")
    return False

# método para guardar trabajos en tabla empleo
def save_jobs_db(jobs):
    try:
        query = """
            INSERT INTO Empleo (tituloEmpleo, nombreEmpresa, ubicacionEmpleo,
            salario, fechaPublicacion, enlaceOferta, tipoTrabajo)
            VALUES (%s, %s, %s, %s, %s, %s, %s )
        """
        
        for job in jobs:
            # validar para ver si no hay valores nulos o vacíos
            job = tuple(None if v == '' else v for v in job)
            mycursor.execute(query, job)
        
        con.commit()
        print("Datos guardados en la BD")
    except mysql.connector.Error as e:
        print(f"Error al guardar los datos en BD: {e}")

def find_jobs(keyword):
    listJobsTitles = []
    hyperlinks = []
    companies = []
    workSites = []
    salaries = []
    jobTypes = []
    postedTimes = []

    keyword = keyword.lower().replace(" ", "-")
    url = f"https://mx.computrabajo.com/trabajo-de-{keyword}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, Gecko) Chrome/101.0.4951.41 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print("Respuesta recibida correctamente.")  # Mensaje de depuración
        
        soup = BeautifulSoup(response.content, "html.parser")

        # Obtener títulos y enlaces de trabajos
        results = soup.find_all("a", class_="js-o-link fc_base")
        print(f"Se encontraron {len(results)} trabajos.")  # Mensaje de depuración
        for result in results:
            hyperlink = f"https://mx.computrabajo.com{result['href']}"
            listJobsTitles.append(result.text.strip())
            hyperlinks.append(hyperlink)

        # Obtener nombres de empresas
        results = soup.find_all("p", class_="dIB fs16 fc_base mt5")
        print(f"Se encontraron {len(results)} nombres de empresas.")  # Mensaje de depuración
        for result in results:
            company_link = result.find("a")
            if company_link:
                companies.append(company_link.text.strip())
            else:
                companies.append("Empresa no disponible")

        # Obtener ubicaciones
        results = soup.find_all("p", class_="fs16 fc_base mt5")
        print(f"Se encontraron {len(results)} ubicaciones.")  # Mensaje de depuración
        for result in results:
            location_span = result.find("span")
            if location_span:
                workSites.append(location_span.text.strip())
            else:
                workSites.append("Ubicación no disponible")

        # Obtener salarios y tipos de trabajo
        salary_results = soup.find_all("div", class_="fs13 mt15")
        print(f"Se encontraron {len(salary_results)} salarios y tipos de trabajo.")  # Mensaje de depuración
        for result in salary_results:
            salary_span = result.find("span", class_="icon i_salary")
            if salary_span:
                salary_text = salary_span.find_next_sibling(text=True).strip() if salary_span.find_next_sibling() else "No disponible"
                salaries.append(salary_text)
            else:
                salaries.append("No disponible")

            job_type_span = result.find("span", class_="icon i_home")
            if job_type_span:
                job_type_text = job_type_span.find_next_sibling(text=True).strip() if job_type_span.find_next_sibling() else "No disponible"
                jobTypes.append(job_type_text)
            else:
                jobTypes.append("No disponible")

            posted_time_elem = result.find_next("p", class_="fs13 fc_aux mt15")
            posted_time_text = posted_time_elem.text.strip() if posted_time_elem else "No disponible"
            postedTimes.append(posted_time_text)

        return listJobsTitles, hyperlinks, companies, workSites, salaries, jobTypes, postedTimes

    except requests.exceptions.RequestException as e:
        print("Error en la solicitud:", e)
        return [], [], [], [], [], [], []

@app.route('/', methods=['GET', 'POST'])
def home():
    keyword = request.args.get('keyword', 'programador')
    location = request.args.get('location', '')
    job_type = request.args.get('job_type', '')

    listJobsTitles, hyperlinks, companies, workSites, salaries, jobTypes, postedTimes = find_jobs(keyword)

    all_jobs = []
    
    for i in range(len(listJobsTitles)):
        if (i < len(companies) and i < len(workSites) and 
            i < len(salaries) and i < len(jobTypes) and 
            i < len(postedTimes)):
            all_jobs.append((listJobsTitles[i], companies[i], workSites[i], salaries[i], postedTimes[i], hyperlinks[i], jobTypes[i]))

    # guardar empleos en BD
    save_jobs_db(all_jobs)

    filtered_jobs = all_jobs 

    if location or job_type:
        filtered_jobs = []
        for i in range(len(all_jobs)):
            if location and location.lower() not in all_jobs[i][3].lower():
                continue
            
            if job_type and job_type.lower() != all_jobs[i][5].lower():
                continue
            
            filtered_jobs.append(all_jobs[i])

    return render_template('jobs.html', jobs=filtered_jobs)

@app.route('/somos')
def somos():
    return render_template('somos.html')

@app.route('/cuenta', methods=['GET', 'POST'])
def cuenta():
    # iniciar sesion de usuario en BD
    if request.method == 'POST':
        email = request.form['correoElectronico']
        password = request.form['contraseñaUsuario']

        username = login_user(email, password)
        if username:
            session['email'] = email
            session['username'] = username
            return redirect(url_for('datos'))
        else:
            flash('Correo o contraseña incorrectos, intenta de nuevo', 'error')
            return render_template('cuenta.html')
    return render_template('cuenta.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    # registrar usuario en BD
    if request.method == 'POST':
        username = request.form['nombreUsuario']
        email = request.form['correoElectronico']
        password = request.form['contraseñaUsuario']
        sign_up_user(username, email, password)
        return render_template('cuenta.html')
    else:
        return render_template('registro.html')

@app.route('/datos')
def datos():
    if 'email' in session and 'username' in session:
        return render_template('datos.html', username=session['username'])
    else:
        return redirect(url_for('cuenta'))

if __name__ == '__main__':
    app.run(debug=True)
