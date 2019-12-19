import React, {Component} from "react";
import RepoListForm from "../components/List/RepoListForm";
import * as listAction from "../modules/list";
import axios from "axios";

export class ListContainer extends Component {

    handleOauth = () => {
        console.log("handleClickTestStart")
        axios.get({
            url: 'http://test.gitdefender.com:8080/api/v1/auth/oauth2"',
            header: {
                token: localStorage.getItem("token")
            }
        })
            .then(function (response) {
                console.log("handleClickTestSuccess");
                console.log(response);
            })
            .catch(function (error) {
                console.log("handleClickTestFail");
                console.log(error);
            });
        console.log("handleClickTestFinish")
    }

    render() {
        const {token, logged } = this.props;
        const {handleOauth} = this;
        return (
            <RepoListForm
                token={token}
                logged={logged}
                onOauth={handleOauth}
            />
        );
    }
}