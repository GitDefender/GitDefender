import React from "react";
import "antd/dist/antd.css";
import ReportForm from "../components/Report/ReportForm";
import ReportStructure from "../components/structure/Report/ReportStructure";

const Report = () => {
    return (
        <ReportStructure>
            <ReportForm/>
        </ReportStructure>
    )
};

export default Report;