import React from "react";
import "antd/dist/antd.css";
import MainStructure from "../components/structure";
import RepoListForm from "../components/List/RepoListForm";


const Main = () => {
    return (
        <MainStructure>
            <RepoListForm/>
        </MainStructure>
    )
};

export default Main;