import React, { Component } from 'react';
import { Layout, Menu, Breadcrumb } from 'antd';
import { Row, Col } from 'antd';
import { Table, Divider, Tag, Icon, Alert, Pagination } from 'antd';

import axios from 'axios';

import { get_repository } from './api.js';

const { Column, ColumnGroup } = Table;

class RepoList extends Component {
    constructor(props) {
        super(props);

        this.state = {
            // just sample data
            data: [
            ],
            server_status : 0,
            repository_index : 1,
            per_page: 5
        }
    }

    componentDidMount() {
        this.GetRepository()
        this.GetRepository(2)
    }

    GetRepository(page_){
        axios.get(get_repository, {
            headers: {
                Authorization: "Token XXXXX" //will be replace to localStorage()
            },
            params: {
                page: page_ ?  page_ : this.state.repository_index,
                per_page: this.state.per_page
            }
        })
            .then((response) => {
                //console.log(response.data)
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
                this.setState({server_status: error.response.status})
                
            })
    }

    paginationChange(page, pageSize){
        if(this.state.repository_index <= page){
            this.setState({
                repository_index: page
            })
            // It must be changed to process likes cached data before Published.
            this.GetRepository()
        }
    }

    render() {
        return (
            this.state.response==200 ? 
            (<Table dataSource={this.state.data} pagination={{pageSize: 5, onChange: this.paginationChange}}>
                <Column title="Repository name" dataIndex="name" key="name" />
                <Column title="Latest Commit Date" dataIndex="recent_commit_date" key="commit_date" />
                <Column title="Commit Message" dataIndex="recent_commit_message" key="commit_message" />
                <Column title="" dataIndex="scan" key="scan" />
                <Column title="" dataIndex="report" key="report" />
                <Column title="Secu-level" dataIndex="secure_level"
                    key="secure_level"
                    render={le => (
                        le=="low" ? <Icon type="check-circle" theme="twoTone" twoToneColor='green'/> : 
                            le=="middle" ? <Icon type="check-circle" theme="twoTone" twoToneColor='orange'/> :
                                le=="high" ? <Icon type="check-circle" theme="twoTone" twoToneColor='red'/> : "0"
                        
                    )}
                     // Security Level Icon set
                />
                <Pagination position='top'/>
            </Table>) : 
            <Alert
                message="Invalid User Authorization"
                description="This is an error message about you are Unauthorized User"
                type="error"
                showIcon closable
            />
        )
    }
}

export default RepoList;