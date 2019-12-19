import React from "react";
import MainStructure from "../components/structure";
import "antd/dist/antd.css";
import axios from 'axios';
import { Tabs, List, Button } from "antd";
//import Tabs from "../components/Tab/tabs"
import RepoInfoList from "../components/List/RepoInfoList";
import RepoListForm from "../components/List/RepoListForm";

const { TabPane } = Tabs;

const Main = () => {
    return (
        <MainStructure>
            <RepoListForm/>
        </MainStructure>
    )
};

export default Main;