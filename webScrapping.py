import requests
from bs4 import BeautifulSoup

def findJobs(keyword):
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
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    
    print("URL generada:", url)
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error en la solicitud:", e)
        return None
    
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Obtener títulos de trabajos y enlaces
    results = soup.find_all("a", class_="js-o-link fc_base")
    for result in results:
        hyperlink = f"https://mx.computrabajo.com{result['href']}"
        listJobsTitles.append(result.text.strip())
        hyperlinks.append(hyperlink)

    # Obtener nombres de las empresas y ubicaciones
    results = soup.find_all("p", class_="dIB fs16 fc_base mt5")
    for result in results:
        company_link = result.find("a")
        if company_link:
            companies.append(company_link.text.strip())
        else:
            companies.append("Empresa no disponible")

        location_span = result.find("span")
        if location_span:
            workSites.append(location_span.text.strip())
        else:
            workSites.append("Ubicación no disponible")

    # Obtener salarios, tipos de trabajo (modalidad) y fechas de publicación
    salary_results = soup.find_all("div", class_="fs13 mt15")
    for result in salary_results:
        # Obtener salario
        salary_span = result.find("span", class_="icon i_salary")
        if salary_span:
            salary_text = salary_span.find_parent().text.strip()  # Obtener el texto del padre
        else:
            salary_text = "No disponible"
        salaries.append(salary_text)

        # Obtener modalidad (tipo de trabajo)
        job_type_span = result.find("span", class_="icon i_home")
        if job_type_span:
            job_type_text = job_type_span.find_parent().text.strip()  # Obtener el texto del padre
        else:
            job_type_text = "No disponible"
        jobTypes.append(job_type_text)

        # Obtener la fecha de publicación
        posted_time_elem = result.find_next("p", class_="fs13 fc_aux mt15")
        posted_time_text = posted_time_elem.text.strip() if posted_time_elem else "No disponible"
        postedTimes.append(posted_time_text)

    return listJobsTitles, hyperlinks, companies, workSites, salaries, jobTypes, postedTimes

# Prueba la función
keyword = "programador"
jobs_data = findJobs(keyword)

if jobs_data:
    titles, links, companies, locations, salaries, job_types, posted_times = jobs_data

    # Mostrar los resultados
    for title, link, company, location, salary, job_type, posted_time in zip(titles, links, companies, locations, salaries, job_types, posted_times):
        print(f"Título: {title}, Empresa: {company}, Ubicación: {location}, Salario: {salary}, Tipo: {job_type}, Publicado: {posted_time}, Enlace: {link}")
