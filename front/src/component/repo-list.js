import React, { Component } from 'react';
import { Layout, Menu, Breadcrumb } from 'antd';
import { Row, Col } from 'antd';
import { Table, Divider, Tag, Icon } from 'antd';

import axios from 'axios';

import { get_repository } from './api.js';

const { Column, ColumnGroup } = Table;

class RepoList extends Component {
    constructor(props) {
        super(props);

        this.state = {
            data: [

            ]
        }
    }

    componentDidMount() {
        
        axios.get(get_repository, {
            headers: {
                Authorization: "Token XXXXX" //will be replace to localStorage('token')
            }
        })
            .then((response) => {
                console.log(response.data)
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
            })
            
    }

    render() {
        return (
            <Table dataSource={this.state.data}>
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
            </Table>
        )
    }
}

export default RepoList;