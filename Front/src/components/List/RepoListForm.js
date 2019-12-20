import React, {Component} from 'react';
import axios from 'axios';
import "antd/dist/antd.css";
import {Tabs, Button, Table} from "antd";

const {TabPane} = Tabs;

class RepoListForm extends Component {
    constructor(props) {
        super(props);
        this.state = {
            token: localStorage.getItem("token"),
            repositories: [{
                latest_commit: '2019-09-12',
                latest_scan: '2019-09-15',
                name: 'dogproject',
                url: 'https://github.com/listExample.git'
            },{
                latest_commit: '2019-09-12',
                latest_scan: '2019-09-15',
                name: 'dogproject',
                url: 'https://github.com/listExample.git'
            },{
                latest_commit: '2019-09-12',
                latest_scan: '2019-09-15',
                name: 'dogproject',
                url: 'https://github.com/listExample.git'
            },{
                latest_commit: '2019-09-12',
                latest_scan: '2019-09-15',
                name: 'dogproject',
                url: 'https://github.com/listExample.git'
            },{
                latest_commit: '2019-09-12',
                latest_scan: '2019-09-15',
                name: 'dogproject',
                url: 'https://github.com/listExample.git'
            },{
                latest_commit: '2019-09-12',
                latest_scan: '2019-09-15',
                name: 'dogproject',
                url: 'https://github.com/listExample.git'
            }],
            repositories_size: 1
        }
        this.gitOauth = this.gitOauth.bind(this);
        this.gitTokenCheck = this.gitTokenCheck.bind(this);
        this.getRepsotories = this.getRepsotories.bind(this);
        this.handleScan = this.handleScan.bind(this);
    }

    gitTokenCheck() {
        const token_str = this.state.token;
        const token = token_str.substring(10, token_str.length - 2);

        const url = '/api/v1/auth/user';
        axios.defaults.baseURL = "http://test.gitdefender.com:8080"
        const headers = {/*
            "Access-Control-Allow-Headers": ["*"],
            //"Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept",
            "Access-Control-Allow-Origin": '*',
            "Access-Control-Allow-Methods": '*',
            "Access-Control-Allow-Credentials": "true",
            'Content-Type': 'application/jsonp',*/
            'Authorization': "Token" + " " + token
        };

        console.log("UserCheck Start")
        axios.get(url,
            {
                headers
            }
        )
            .then(function (response) {
                    console.log("gitTokenCheck Success");
                    console.log(response);
                }
            )
            .catch(function (error) {
                    console.log("gitTokenCheck Fail");
                    console.log(error);
                }
            );
    }

    getRepsotories() {
        const token_str = this.state.token;
        const token = token_str.substring(10, token_str.length - 2);

        const headers = {
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Origin": "*",
            'Content-Type': 'application/json',
            'Authorization': "Token" + " " + token
        };

        console.log("GitHub_Token_Get_Start")
        axios.get('http://test.gitdefender.com:8080/api/v1/get_repository',
            {
                headers
            }
        )
            .then(function (response) {
                    this.state.repositories = JSON.parse(response).repositories;
                    console.log("getRepsotories_Success");
                    console.log(response);
                }
            )
            .catch(function (error) {
                    console.log("getRepsotories_Fail");
                    console.log(error);
                }
            );
    }

    getBranch() {
        const token_str = this.state.token;
        const token = token_str.substring(10, token_str.length - 2);

        const headers = {
            'Content-Type': 'application/json',
            'Authorization': "Token" + " " + token,
            "page": "1",
            "per_page": "10"
        };

        console.log("GitHub_Token_Get_Start")
        axios.get('http://test.gitdefender.com:8080/api/v1/get_branch',
            {
                headers
            }
        )
            .then(function (response) {
                    this.state.repositories = JSON.parse(response).repositories;
                    console.log("getBranch_Success");
                    console.log(response);
                }
            )
            .catch(function (error) {
                    console.log("getBranch_Fail");
                    console.log(error);
                }
            );
    }

    getCommit() {
        const token_str = this.state.token;
        const token = token_str.substring(10, token_str.length - 2);

        const headers = {
            'Content-Type': 'application/json',
            'Authorization': "Token" + " " + token
        };

        console.log("GitHub_Token_Get_Start")
        axios.get('http://test.gitdefender.com:8080/api/v1/get_commit',
            {
                headers
            }
        )
            .then(function (response) {
                    this.state.repositories = JSON.parse(response).repositories;
                    console.log("getCommit_Success");
                    console.log(response);
                }
            )
            .catch(function (error) {
                    console.log("getCommit_Fail");
                    console.log(error);
                }
            );

    }

    handleScan() {
        const token_str = this.state.token;
        const token = token_str.substring(10, token_str.length - 2);

        const headers = {
            'Content-Type': 'application/json',
            'Authorization': "Token" + " " + token
        };

        console.log("GitHub_Token_Get_Start")
        axios.get('http://test.gitdefender.com:8080/api/v1/get_code_detect',
            {
                headers
            }
        )
            .then(function (response) {
                    this.state.repositories = JSON.parse(response).repositories;
                    console.log("handleScan_Success");
                    console.log(response);
                }
            )
            .catch(function (error) {
                    console.log("handleScan_Fail");
                    console.log(error);
                }
            );
    }

    gitOauth() {
        const token_str = this.state.token;
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
        console.log("gitOauthTestFinish")


    }

    render() {
        const column = [
            {
                title: 'Repository Name',
                dataIndex: 'name',
                render: text => <a>{text}</a>,
            },
            {
                title: 'Latest Commit',
                dataIndex: 'latest_commit',
            },
            {
                title: 'Latest Scan',
                dataIndex: 'latest_scan',
            },
            {
                title: 'Repository URL',
                dataIndex: 'url',
            },
            {
                title: 'SCAN',
                dataIndex: '',
                render: (text, record) => (
                    <span>
                        <a>Scan</a>
                    </span>
                ),
            },
            {
                title: 'Report',
                dataIndex: '',
                render: (text, record) => (
                    <span>
                        <a href={"/Report"}>Report</a>
                    </span>
                ),
            }
        ];

        return (
            <form>
                <Tabs type="card">
                    <TabPane tab="GitHub" key="1">
                        <div label="GitHub">
                            <Button size="large" type="primary"
                                    className={"GitHub OAuth"}
                                    onClick={this.gitOauth}>GitHub OAuth
                            </Button>
                            <Button size="large" type="primary"
                                    className={"GitHub check"}
                                    onClick={this.gitTokenCheck}>
                                GitHub Token Check
                            </Button>
                            <Button size="large" type="primary"
                                    className={"GitHub check"}
                                    onClick={this.getRepsotories}>
                                GitHub Get Repository
                            </Button>
                            <Table
                                columns={column}
                                dataSource={this.state.repositories}
                            />
                        </div>
                    </TabPane>

                    <TabPane tab="GitLab" key="2">
                        <div label="GitLab">
                            <Button size="large" type="primary"
                                    className={"GitLab OAuth"}
                                    onClick={this.gitOauth}>GitLab OAuth
                            </Button>
                            <Button size="large" type="primary"
                                    className={"GitHub check"}
                                    onClick={this.gitTokenCheck}>
                                GitLab Token Check
                            </Button>
                            <Button size="large" type="primary"
                                    className={"GitHub check"}
                                    onClick={this.getRepsotories}>
                                GitLab Get Repository
                            </Button>
                            <Table
                                columns={column}
                                dataSource={this.state.repositories}
                            />
                        </div>
                    </TabPane>

                    <TabPane tab="BitBucket" key="3">
                        <div label="BitBucket">
                            <Button size="large" type="primary"
                                    className={"BitBucket OAuth"}
                                    onClick={this.gitOauth}>BitBucket OAuth
                            </Button>
                            <Button size="large" type="primary"
                                    className={"BitBucket check"}
                                    onClick={this.gitTokenCheck}>
                                BitBucket Token Check
                            </Button>
                            <Button size="large" type="primary"
                                    className={"BitBucket check"}
                                    onClick={this.getRepsotories}>
                                BitBucket Get Repository
                            </Button>
                            <Table
                                columns={column}
                                dataSource={this.state.repositories}
                            />
                        </div>
                    </TabPane>
                </Tabs>
            </form>
        );
    }
}

/*
<Row>
    <Col span={6}>Repository Name</Col>
    <Col span={6}>Latest Commit</Col>
    <Col span={6}>Latest Scan</Col>
    <Col span={6}>URL</Col>
</Row>
<List size="large"
      itemLayout="vertical"
      dataSource={this.state.repositories}
      renderItem={item =>
          <div>
              <List.Item
                  style={{
                      fontSize: 20,
                      marginTop: 12,
                      height: 200,
                      lineHeight: '32px',
                  }}>
                  {item.name}<br/>
                  {item.latest_commit}
                  {item.latest_scan}
                  {item.url}
                  <div>
                      <Button
                          onClick={this.handleScan}
                          type="primary"
                          size="large">Scan</Button>
                  </div>
              </List.Item>
          </div>
      }/>*/
export default RepoListForm;