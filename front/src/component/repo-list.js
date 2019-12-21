import React, { Component } from 'react';
import { Redirect } from 'react-router-dom';
import { Layout, Menu, Breadcrumb } from 'antd';
import { Row, Col } from 'antd';
import { Table, Button, Icon, Alert, Pagination, Card } from 'antd';

import axios from 'axios';

import { get_repository } from './api.js';
import Report from './report';

const { Column, ColumnGroup } = Table;

class RepoList extends Component {
    constructor(props) {
        super(props);

        this.state = {
            // just sample data
            data: [
            ],
            server_status: 0,
            repository_index: 1,
            per_page: 5
        }
    }

    componentDidMount() {
        this.setState(this.state)
        this.GetRepository(1)
        this.GetRepository(2)

    }

    tabList = [
        {
            key: 'Github',
            tab: 'Github',
        },
        {
            key: 'Gitlab',
            tab: 'Gitlab',
        },
        {
            key: 'BitBucket',
            tab: 'BitBucket',
        },
    ];

    GetRepository(page_) {
        axios.get(get_repository, {
            headers: {
                Authorization: sessionStorage.getItem('GdfToken')
            },
            params: {
                page: page_ ? page_ : this.state.repository_index,
                per_page: this.state.per_page
            }
        })
            .then((response) => {
                console.log(response)

                if (response.data.error_message == "Unvalid User Token") {
                    return ''
                }

                this.setState({
                    server_status: response.status,
                    repository_index: this.repository_index + 1
                })

                response.data.repositories.map(
                    repo => (
                        this.setState({
                            data: [...this.state.data,
                                repo
                            ]
                        }
                        )
                    )
                )
                console.log(this.state.data)
            }
            )
            .catch((error) => {
                console.log(error)
                this.setState({ server_status: error.response.status })

            })
    }

    paginationChange(page, pageSize) {
        if (Number(this.state.repository_index) <= Number(page)) {
            this.setState({
                repository_index: page
            })
            // It must be changed to process likes cached data before Published.
            this.GetRepository()
        }
    }


    url(){
        try {
            let user_token = sessionStorage.getItem('GdfToken').replace("Token ", "");
            let oauth2_url = "https://github.com/login/oauth/authorize?scope=repo%20read:repo_hook%20read:org%20read:user%20user:email%20\
                &client_id=d220f1ce704075b77610&state=" + this.user_token;

            this.setState({
                oauth2_url: this.oauth2_url
            })
        } catch (error) {
        }
        
    }
    
    


    scan_process(props){
        console.log(props)
        let path = '/report' + ''

        //return <Redirect to={path}/>
    }

    render() {
        
        return (
            <div>
                <Card
                    style={{ width: '100%' }}
                    title={sessionStorage.getItem('name') + "'s Repository List"}
                    tabList={this.tabList}
                    activeTabKey={this.state.key}
                    onTabChange={key => {
                        '';
                    }}>
                    {sessionStorage.getItem('GdfToken') ? <div>
                        {
                            this.state.response == 200 ? '' : <Alert message="Invalid User Authorization"
                                description={<p>This is an error message about you are Unauthorized User.
                                    <a href={this.oauth2_url ? this.oauth2_url : ''} >
                                        &nbsp; Authorize Again</a>
                                </p>}
                                type="error"
                                showIcon closable />
                        }

                        <Table dataSource={this.state.data} pagination={{ pageSize: 5, onChange: this.paginationChange() }}>
                            <Column title="Repository name" dataIndex="name" key="name" />
                            <Column title="Latest Commit Date" dataIndex="recent_commit_date" key="commit_date" />
                            <Column title="Commit Message" dataIndex="recent_commit_message" key="commit_message" />
                            <Column title="" dataIndex="button" key="button" 
                                render={(data, row) => 
                                (
                                    <div><Button href={'/report/'+row.name}>Scan</Button> <Button href={'/report/'+row.name}>Report</Button></div>
                                )}/>
                            <Column title="Secu-level" dataIndex="secure_level"
                                key="secure_level"
                                render={le => (
                                    le == "low" ? <Icon type="check-circle" theme="twoTone" twoToneColor='green' /> :
                                        le == "middle" ? <Icon type="check-circle" theme="twoTone" twoToneColor='orange' /> :
                                            le == "high" ? <Icon type="check-circle" theme="twoTone" twoToneColor='red' /> : "0"
                                )}
                            // Security Level Icon set
                            />
                            <Pagination position='top' />
                        </Table>
                    </div> : <Redirect to='/login' />}
                </Card>


            </div>

        )
    }
}

export default RepoList;