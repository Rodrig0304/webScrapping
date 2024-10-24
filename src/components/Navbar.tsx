// imports para los iconos de fontawesome
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faSearch } from "@fortawesome/free-solid-svg-icons";
import { faUsers } from "@fortawesome/free-solid-svg-icons";
import { faUser } from "@fortawesome/free-solid-svg-icons";

function Navbar() {
  return (
    <>
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <a className="navbar-brand" href="#">
          EmpleosAllInstante
        </a>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav ml-auto">
            <li className="nav-item">
              <a className="nav-link">
                Busqueda <FontAwesomeIcon icon={faSearch} />
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link">
                Quienes Somos <FontAwesomeIcon icon={faUsers} />
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link">
                Cuenta <FontAwesomeIcon icon={faUser} />
              </a>
            </li>
          </ul>
        </div>
      </nav>
    </>
  );
}

export default Navbar;
