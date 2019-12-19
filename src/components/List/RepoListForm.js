import React, {Component} from 'react';
import {Redirect} from "react-router-dom";
import axios from 'axios';
import "antd/dist/antd.css";
import {Tabs, List, Button} from "antd";
import RepoInfoList from "./RepoInfoList";
import MainStructure from "../structure";

const {TabPane} = Tabs;

class RepoListForm extends Component {
    constructor(props) {
        super(props);
        this.state = {
            repositories: [
                'https://github.com/khj0209/pcap_HW.git',
                'https://github.com/khj0209/gitdifender.git',
            ]
        }
        this.handleClick = this.handleClick.bind(this);
        this.handleCheck = this.handleCheck.bind(this);
        this.handleGet = this.handleGet.bind(this);
    }

    handleCheck() {
        const headers = {
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Origin": "*",
            'Content-Type': 'application/json',
            'Authorization': localStorage.getItem("token"),
        };

        console.log("UserCheck Start")
        axios.get('http://test.gitdefender.com:8080/api/v1/user',
            {
                headers
            }
        )
            .then(function (response) {
                    console.log("UserCheck Success");
                    console.log(response);
                }
            )
            .catch(function (error) {
                    console.log("UserCheck Fail");
                    console.log(error);
                }
            );
    }

    handleGet() {
        this.handleCheck();

        const headers = {
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Origin": "*",
            'Content-Type': 'application/json',
            'Authorization': localStorage.getItem("token"),
        };

        console.log("GitHub_Token_Get_Start")
        axios.get('http://test.gitdefender.com:8080/api/v1/get_repository',
            {
                headers
            }
        )
            .then(function (response) {
                    this.state.repositories = JSON.parse(response).repositories;
                    console.log("GitHub_Token_Get_Success");
                    console.log(response);
                }
            )
            .catch(function (error) {
                    console.log("GitHub_Token_Get_Fail");
                    console.log(error);
                }
            );
    }

    handleClick() {
        const token_str = localStorage.getItem("token");
        const token = token_str.substring(10, token_str.length - 2);
        window.location.assign(
            "https://github.com/login/oauth/authorize?" +
            "scope=repo%20read:repo_hook%20read:org%20read:user%20user:email%20&&" +
            "client_id=d220f1ce704075b77610&&" +
            "state=" + token)
        /*
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

         */
        console.log("handleClickTestFinish")


    }

    render() {

        return (
            <form>
                <Tabs type="card">
                    <TabPane tab="GitHub" key="1">
                        <div label="GitHub">
                            <Button size="large" type="primary"
                                    className={"GitHub OAuth"}
                                /*onClick={this.handleClick}>*/
                                    onClick={this.handleClick}>GitHub OAuth
                            </Button>
                            <br/>
                            <br/>
                            <Button size="large" type="primary"
                                    className={"GitHub check"}
                                /*onClick={this.handleClick}>*/
                                    onClick={this.handleCheck}>GitHub Token Check
                            </Button>
                            <br/>
                            <br/>
                            <Button size="large" type="primary"
                                    className={"GitHub check"}
                                /*onClick={this.handleClick}>*/
                                    onClick={this.handleGet}>GitHub Get Repository
                            </Button>
                            <List size="large" dataSource={this.state.repositories}
                                  renderItem={item => (
                                      <List.Item>
                                          {item}
                                      </List.Item>
                                  )}
                            >
                            </List>
                        </div>
                    </TabPane>

                    <TabPane tab="GitLab" key="2">
                        <div label="GitLab">
                            <Button size="large" type="primary"
                                    className={"GitLab OAuth"}>
                                GitLab OAuth2
                            </Button>
                            <List size="large">
                            </List>
                        </div>
                    </TabPane>

                    <TabPane tab="BitBucket" key="3">
                        <div label="BitBucket">
                            <List/>
                            <RepoListForm/>
                            <RepoInfoList/>
                        </div>
                    </TabPane>
                </Tabs>
            </form>
        );
    }
}

export default RepoListForm;