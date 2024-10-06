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
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    
    print("URL generada:", url)
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Obtener títulos de trabajos
        results = soup.find_all("a", class_="js-o-link fc_base")
        for result in results:
            hyperlink = f"https://mx.computrabajo.com{result['href']}"
            listJobsTitles.append(result.text.strip())
            hyperlinks.append(hyperlink)

        # Obtener nombres de las empresas
        results = soup.find_all("p", class_="dIB fs16 fc_base mt5")
        for result in results:
            company_link = result.find("a")
            if company_link:
                companies.append(company_link.text.strip())
            else:
                companies.append("Empresa no disponible")

        # Obtener ubicaciones
        results = soup.find_all("p", class_="fs16 fc_base mt5")
        for result in results:
            location_span = result.find("span")
            if location_span:
                workSites.append(location_span.text.strip())
            else:
                workSites.append("Ubicación no disponible")

        # Obtener salarios, tipos de trabajo (modalidad) y fechas de publicación
        salary_results = soup.find_all("div", class_="fs13 mt15")  # Div que contiene salario y modalidad
        for result in salary_results:
            # Obtener salario
            salary_span = result.find("span", class_="icon i_salary")
            if salary_span:
                salary_text = salary_span.find_next_sibling(text=True).strip()  # Obtener el texto que sigue después del icono de salario
            else:
                salary_text = "No disponible"
            salaries.append(salary_text)

            # Obtener modalidad (tipo de trabajo)
            job_type_span = result.find("span", class_="icon i_home")
            if job_type_span:
                job_type_text = job_type_span.find_next_sibling(text=True).strip()  # Obtener el texto que sigue después del icono de modalidad
            else:
                job_type_text = "No disponible"
            jobTypes.append(job_type_text)

            # Fecha de publicación
            posted_time_elem = result.find_next("p", class_="fs13 fc_aux mt15")
            posted_time_text = posted_time_elem.text.strip() if posted_time_elem else "No disponible"
            postedTimes.append(posted_time_text)

        return listJobsTitles, hyperlinks, companies, workSites, salaries, jobTypes, postedTimes
    
    else:
        print("Error en la solicitud:", response.status_code)

# Prueba la función
keyword = "programador"
titles, links, companies, locations, salaries, job_types, posted_times = findJobs(keyword)

# Mostrar los resultados
for title, link, company, location, salary, job_type, posted_time in zip(titles, links, companies, locations, salaries, job_types, posted_times):
    print(f"Título: {title}, Empresa: {company}, Ubicación: {location}, Salario: {salary}, Tipo: {job_type}, Publicado: {posted_time}, Enlace: {link}")
