import React from "react";
import styles from "./Header.css";
import {Link} from "react-router-dom";
import {MdLock} from "react-icons/md";

const Header = ({onLogout}) => (
    <div className={"header"}>
        <Link to={"/"} className={"logo"}>
            GitDefender
        </Link>
        <div className={"logout"}>
            <Link to={"/auth/login"}>
                <MdLock onClick={onLogout}/>
            </Link>
        </div>
    </div>
);

export default Header;