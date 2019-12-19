import React from "react";
import "antd/dist/antd.css";
import HeaderContainer from "../containers/HeaderContainer";
import ReportForm from "../components/Report/ReportForm";

const Report = () => {
    return (
        <div>
            <HeaderContainer>
                <ReportForm/>
            </HeaderContainer>
        </div>
    )
};

export default Report;