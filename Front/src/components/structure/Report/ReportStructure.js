import React from "react";
import HeaderContainer from "../../../containers/HeaderContainer";

const ReportStructure = ({children}) => (
    <div>
        <HeaderContainer/>
        <amin>{children}</amin>
    </div>
);

export default ReportStructure;