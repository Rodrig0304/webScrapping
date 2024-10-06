from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def find_jobs(keyword):
    # Listas para almacenar los datos de las ofertas de trabajo
    titles = []
    links = []
    companies = []
    locations = []
    salaries = []
    job_types = []
    posted_times = []

    # Genera la URL de búsqueda
    keyword = keyword.lower().replace(" ", "-")
    url = f"https://mx.computrabajo.com/trabajo-de-{keyword}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }

    print("URL generada:", url)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        # Obtener títulos y enlaces de trabajos
        results = soup.find_all("a", class_="js-o-link fc_base")
        for result in results:
            hyperlink = f"https://mx.computrabajo.com{result['href']}"
            titles.append(result.text.strip())
            links.append(hyperlink)

        # Obtener nombres de las empresas
        company_results = soup.find_all("p", class_="dIB fs16 fc_base mt5")
        for result in company_results:
            company_link = result.find("a")
            companies.append(company_link.text.strip() if company_link else "Empresa no disponible")

        # Obtener ubicaciones
        location_results = soup.find_all("p", class_="fs16 fc_base mt5")
        for result in location_results:
            location_span = result.find("span")
            locations.append(location_span.text.strip() if location_span else "Ubicación no disponible")

        # Obtener salarios, tipos de trabajo y fechas de publicación
        salary_results = soup.find_all("div", class_="fs13 mt15")  # Ajusta según la estructura actual
        for result in salary_results:
            salary_span = result.find("span", class_="icon i_salary")
            salary_text = salary_span.find_next_sibling(text=True).strip() if salary_span else "No disponible"
            salaries.append(salary_text)

            job_type_span = result.find("span", class_="icon i_home")
            job_type_text = job_type_span.find_next_sibling(text=True).strip() if job_type_span else "No disponible"
            job_types.append(job_type_text)

            posted_time_elem = result.find_next("p", class_="fs13 fc_aux mt15")
            posted_time_text = posted_time_elem.text.strip() if posted_time_elem else "No disponible"
            posted_times.append(posted_time_text)

        return titles, links, companies, locations, salaries, job_types, posted_times

    else:
        print("Error en la solicitud:", response.status_code)
        return [], [], [], [], [], [], []  # Retorna listas vacías en caso de error

@app.route('/')
def home():
    keyword = "programador"  # Cambia esto o hazlo dinámico con un formulario
    titles, links, companies, locations, salaries, job_types, posted_times = find_jobs(keyword)

    return render_template('jobs.html', jobs=zip(titles, links, companies, locations, salaries, job_types, posted_times))

if __name__ == '__main__':
    app.run(debug=True)
