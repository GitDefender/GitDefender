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
                {
                    commits_url: "https://api.github.com/repos/roharon/vm-sim-hw/commits",
                    name: "vm-sim-hw",
                    recent_commit_date: "2019-12-08T17:13:40Z",
                    recent_commit_message: "modify: so simply",
                    secure_level: "low",
                    url: "https://github.com/roharon/vm-sim-hw.git"
                },
                {
                    commits_url: "https://api.github.com/repos/roharon/vm-sim-hw/commits",
                    name: "vm-sim-hsdsdsw",
                    recent_commit_date: "2019-12-08T17:13:40Z",
                    recent_commit_message: "modify: so simply",
                    secure_level: "high",
                    url: "https://github.com/roharon/vm-sim-hw.git"
                },
                {
                    commits_url: "https://api.github.com/repos/roharon/vm-sim-hw/commits",
                    name: "vm-sim-hsdsdsw",
                    recent_commit_date: "2019-12-08T17:13:40Z",
                    recent_commit_message: "modify: so simply",
                    secure_level: "middle",
                    url: "https://github.com/roharon/vm-sim-hw.git"
                },
            ],
            server_status: 0,
            repository_index: 1,
            per_page: 5
        }
    }

    componentDidMount() {
        this.GetRepository()
        this.GetRepository(2)
    }

    GetRepository(page_) {
        axios.get(get_repository, {
            headers: {
                Authorization: "Token XXXXX" //will be replace to localStorage()
            },
            params: {
                page: page_ ? page_ : this.state.repository_index,
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
                this.setState({ server_status: error.response.status })

            })
    }

    paginationChange(page, pageSize) {
        if (this.state.repository_index <= page) {
            this.setState({
                repository_index: page
            })
            // It must be changed to process likes cached data before Published.
            this.GetRepository()
        }
    }

    render() {
        return (
            <div>
                {
                    this.state.response == 200 ? '1' : <Alert message="Invalid User Authorization"
                        description="This is an error message about you are Unauthorized User"
                        type="error"
                        showIcon closable />
                }
                <Table dataSource={this.state.data} pagination={{ pageSize: 5, onChange: this.paginationChange }}>
                    <Column title="Repository name" dataIndex="name" key="name" />
                    <Column title="Latest Commit Date" dataIndex="recent_commit_date" key="commit_date" />
                    <Column title="Commit Message" dataIndex="recent_commit_message" key="commit_message" />
                    <Column title="" dataIndex="scan" key="scan" />
                    <Column title="" dataIndex="report" key="report" />
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
            </div>
        )
    }
}

export default RepoList;