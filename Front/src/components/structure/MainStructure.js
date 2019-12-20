import React from "react";
import HeaderContainer from "../../containers/HeaderContainer";

const MainStructure = ({children}) => (
    <div>
        <HeaderContainer/>
        <main>{children}</main>
    </div>
);

export default MainStructure;