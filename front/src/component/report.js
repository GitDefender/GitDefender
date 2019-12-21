import React, { Component } from 'react';
import { withRouter } from "react-router";
import { Layout, Typography, Descriptions, Card, Row, ol } from 'antd';
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

    render() {
        return (
            <div>
                <br />
                <Title level={3}>{this.state.repo} 's Result Report</Title>

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