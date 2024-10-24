import Navbar from "./components/Navbar";
import EmpleosTabla from "./components/EmpleosTabla";

function App() {
  return (
    // estructura de pagina job
    <>
      <Navbar />
      <div>
        <div className="content">
          <h1 className="text-center m-4">
            Mejores ofertas de trabajo en México
          </h1>
          <form className="mt-4 mb-4" method="GET" action="/">
            <div className="row mb-3">
              <div className="col-md-4">
                <input
                  type="text"
                  name="keyword"
                  className="form-control"
                  placeholder="Buscar empleo"
                  required
                />
              </div>
              <div className="col-md-4">
                <select name="location" className="form-control">
                  <option value="">Seleccione un estado</option>
                  <option value="Aguascalientes">Aguascalientes</option>
                  <option value="Baja California">Baja California</option>
                  <option value="Baja California Sur">
                    Baja California Sur
                  </option>
                  <option value="Campeche">Campeche</option>
                  <option value="Chiapas">Chiapas</option>
                  <option value="Chihuahua">Chihuahua</option>
                  <option value="Coahuila">Coahuila</option>
                  <option value="Colima">Colima</option>
                  <option value="Durango">Durango</option>
                  <option value="Guanajuato">Guanajuato</option>
                  <option value="Guerrero">Guerrero</option>
                  <option value="Hidalgo">Hidalgo</option>
                  <option value="Jalisco">Jalisco</option>
                  <option value="México">México</option>
                  <option value="Michoacán">Michoacán</option>
                  <option value="Morelos">Morelos</option>
                  <option value="Nayarit">Nayarit</option>
                  <option value="Nuevo León">Nuevo León</option>
                  <option value="Oaxaca">Oaxaca</option>
                  <option value="Puebla">Puebla</option>
                  <option value="Querétaro">Querétaro</option>
                  <option value="Quintana Roo">Quintana Roo</option>
                  <option value="San Luis Potosí">San Luis Potosí</option>
                  <option value="Sinaloa">Sinaloa</option>
                  <option value="Sonora">Sonora</option>
                  <option value="Tabasco">Tabasco</option>
                  <option value="Tamaulipas">Tamaulipas</option>
                  <option value="Tlaxcala">Tlaxcala</option>
                  <option value="Veracruz">Veracruz</option>
                  <option value="Yucatán">Yucatán</option>
                  <option value="Zacatecas">Zacatecas</option>
                </select>
              </div>
              <div className="col-md-4">
                <select name="job_type" className="form-control">
                  <option value="">Seleccione modalidad</option>
                  <option value="presencial">Presencial</option>
                  <option value="remoto">Remoto</option>
                  <option value="híbrido">Híbrido</option>
                </select>
              </div>
            </div>
            <button
              type="submit"
              className="btn btn-primary header-button w-10"
            >
              Buscar empleos
            </button>
          </form>
          <div className="vistaBotones">
            <div className="text-end mb-4">
              <button
                id="btn-table"
                className="btn btn-secondary me-2"
                title="Ver en Tabla"
              >
                <i className="fas fa-table"></i>
              </button>
              <button
                id="btn-card"
                className="btn btn-secondary"
                title="Ver en Tarjetas"
              >
                <i className="fas fa-th"></i>
              </button>
            </div>
          </div>
          <div className="tablaContainer">
            <div className="container-fluid">
              <div className="table-responsive" id="jobs-table">
                <table className="table mt-4 mb-4">
                  <thead>
                    <tr>
                      <th>#</th>
                      <th>
                        Título <i className="fas fa-briefcase icon"></i>
                      </th>
                      <th>
                        Empresa <i className="fas fa-building icon"></i>
                      </th>
                      <th>
                        Ubicación <i className="fas fa-map-marker-alt icon"></i>
                      </th>
                      <th>
                        Salario <i className="fas fa-money-bill-wave icon"></i>
                      </th>
                      <th>
                        Tipo de Trabajo{" "}
                        <i className="fas fa-clipboard-check icon"></i>
                      </th>
                      <th>
                        Publicado <i className="fas fa-clock icon"></i>
                      </th>
                      <th>
                        Enlace <i className="fas fa-link icon"></i>
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <EmpleosTabla />
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default App;
