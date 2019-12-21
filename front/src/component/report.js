import React, { Component } from 'react';
import { withRouter } from "react-router";
import {
    Layout, Typography, Descriptions, Card, Row, Col, Button,
    Dropdown, Icon, PageHeader, Menu, message
} from 'antd';
import axios from 'axios';

const { Header, Footer, Content } = Layout;
const { Title } = Typography;

class Report extends Component {
    constructor(props) {
        super(props);
        this.state = {};


    }

    componentDidMount() {
        console.log(this.props.match.params)
        this.setState({
            repo: this.props.match.params.repo,
            branch: this.props.match.params.branch,
            sha: this.props.match.params.sha,
        })
    }

    handleBranchClick = (e) => {
        this.setState({
            set_branch: e.key
        })
    }

    handleCommitClick = (e) => {
        this.setState({
            set_commit: e.key
        })
    }

    branch_menu = (
        <Menu onClick={this.handleBranchClick}>
            <Menu.Item key="wewe">
                <Icon type="user" />
                1st menu item
          </Menu.Item>
            <Menu.Item key="dsds">
                <Icon type="user" />
                2nd menu item
          </Menu.Item>
            <Menu.Item key="wewe23e0pa!">
                <Icon type="user" />
                3rd item
          </Menu.Item>
        </Menu>
    );

    commit_menu = (
        <Menu onClick={this.handleCommitClick}>
            <Menu.Item key="wewe">
                <Icon type="user" />
                1st menu item
          </Menu.Item>
            <Menu.Item key="dsds">
                <Icon type="user" />
                2nd menu item
          </Menu.Item>
            <Menu.Item key="wewe23e0pa!">
                <Icon type="user" />
                3rd item
          </Menu.Item>
        </Menu>
    );

    render() {
        return (
            <div>
                <br />
                <Row>
                    <Col span={8}>
                        <Title level={4}>{this.state.repo} 's Result Report</Title>
                    </Col>

                    <Col span={9} offset={6}>
                        <Dropdown overlay={this.branch_menu}>
                            <Button>
                                Branch | {this.state.set_branch} <Icon type="down" />
                            </Button>
                        </Dropdown>
                        <Dropdown overlay={this.commit_menu}>
                            <Button>
                                Commits | {this.state.set_commit} <Icon type="down" />
                            </Button>
                        </Dropdown>
                    </Col>
                </Row>


                <Card style={{ widht: '100%' }}>

                    <Descriptions title="User Info">
                        <Descriptions.Item label="UserName">Zhou Maomao</Descriptions.Item>
                        <Descriptions.Item label="Telephone">1810000000</Descriptions.Item>
                        <Descriptions.Item label="Live">Hangzhou, Zhejiang</Descriptions.Item>
                        <Descriptions.Item label="Remark">empty</Descriptions.Item>
                        <Descriptions.Item label="Address">
                            No. 18, Wantang Road, Xihu District, Hangzhou, Zhejiang, China
                        </Descriptions.Item>
                    </Descriptions>
                </Card>
            </div>

        )
    }

}

export default Report;