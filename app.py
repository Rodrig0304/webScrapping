from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

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
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        results = soup.find_all("a", class_="js-o-link fc_base")
        for result in results:
            hyperlink = f"https://mx.computrabajo.com{result['href']}"
            listJobsTitles.append(result.text.strip())
            hyperlinks.append(hyperlink)

        results = soup.find_all("p", class_="dIB fs16 fc_base mt5")
        for result in results:
            company_link = result.find("a")
            if company_link:
                companies.append(company_link.text.strip())
            else:
                companies.append("Empresa no disponible")

        results = soup.find_all("p", class_="fs16 fc_base mt5")
        for result in results:
            location_span = result.find("span")
            if location_span:
                workSites.append(location_span.text.strip())
            else:
                workSites.append("Ubicación no disponible")

        salary_results = soup.find_all("div", class_="fs13 mt15")
        for result in salary_results:
            salary_span = result.find("span", class_="icon i_salary")
            if salary_span:
                salary_text = salary_span.find_next_sibling().string.strip() if salary_span.find_next_sibling() else "No disponible"
            else:
                salary_text = "No disponible"
            salaries.append(salary_text)

            job_type_span = result.find("span", class_="icon i_home")
            if job_type_span and job_type_span.find_next_sibling():
                job_type_text = job_type_span.find_next_sibling().string.strip()
            else:
                job_type_text = "No disponible"
            jobTypes.append(job_type_text)

            posted_time_elem = result.find_next("p", class_="fs13 fc_aux mt15")
            posted_time_text = posted_time_elem.string.strip() if posted_time_elem else "No disponible"
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

    # Inicializar una lista con todos los trabajos
    all_jobs = []
    
    for i in range(len(listJobsTitles)):
        # Asegurarse de que todas las listas tengan la misma longitud
        if i < len(companies) and i < len(workSites) and i < len(salaries) and i < len(jobTypes) and i < len(postedTimes):
            all_jobs.append((listJobsTitles[i], hyperlinks[i], companies[i], workSites[i], salaries[i], jobTypes[i], postedTimes[i]))

    # Filtrar resultados según la ubicación y el tipo de trabajo solo si se han especificado
    filtered_jobs = all_jobs 

    if location or job_type:
        filtered_jobs = []
        for i in range(len(all_jobs)):
            # Filtrar por ubicación
            if location and location.lower() not in all_jobs[i][3].lower(): 
                continue
            
            # Filtrar por tipo de trabajo
            if job_type and job_type.lower() != all_jobs[i][5].lower():  
                continue
            
            filtered_jobs.append(all_jobs[i])

    return render_template('jobs.html', jobs=filtered_jobs)

@app.route('/somos')
def somos():
    return render_template('quienes_somos.html')

@app.route('/cuenta')
def cuenta():
    return render_template('cuenta.html')

if __name__ == '__main__':
    app.run(debug=True)
