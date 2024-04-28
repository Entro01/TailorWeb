import React from 'react'
import "./navbar.css";
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <header>
      <div className="navbar">
        <div className="left">
          <h1 className='logo'><Link to="/">TailorWeb</Link></h1>
        </div>
        <div className="middle">
          <ul className="links">
            {/* <li className="link"><Link to="/about">About</Link></li> */}
            <li className="link"><Link to="/product">Products</Link></li>
            <li className="link"><Link to="/fabrics">Fabrics</Link></li>
          </ul>
        </div>
        <div className="right">
          <ul className="links">
            <li className="link"><Link to="/login">Login/Signup</Link></li>
            <li className="link"><Link to="/cart">Cart</Link></li>
          </ul>
        </div>
      </div>
    </header>
  )
}

export default Navbar;
