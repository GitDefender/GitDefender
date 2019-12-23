import React, { Component } from 'react';
import {
    Layout, Typography, Descriptions, Card, Row, Col, Button,
    Dropdown, Icon, Menu, Divider, Popover
} from 'antd';
import axios from 'axios';
import { get_branch, get_commit, get_code_detect } from './api.js';


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
            temp: 1
        })

        this.get_branch()
        this.get_commit()

        setTimeout(()=>{this.setState({temp: 0})},
            2300);
    }

    get_branch = () => {
        axios.get(get_branch, {
            headers: {
                Authorization: sessionStorage.getItem('GdfToken')
            },
            params: {
                repository_name: this.state.repo
            }
        })
    }

    get_commit = () => {
        axios.get(get_branch, {
            headers: {
                Authorization: sessionStorage.getItem('GdfToken')
            },
            params: {
                repository_name: this.state.repo,
                repository_branch: this.state.branch
            }
        })
            .then((res) => {
                console.log("commit===")
                console.log(res)
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
            <Menu.Item key="develop">
                develop
          </Menu.Item>
            <Menu.Item key="master">
                master
          </Menu.Item>
            <Menu.Item key="feature/user">
                feature/user
          </Menu.Item>
        </Menu>
    );

    commit_menu = (
        <Menu onClick={this.handleCommitClick}>
            <Menu.Item key="893a5cb1135b8acbf747ed65e3c3d84c3b7e83b1">
                893a5cb1135b8acbf747ed65e3c3d84c3b7e83b1
          </Menu.Item>
            <Menu.Item key="4143d209ea422128091e0e90b4b275f5c69f0d3e">
                4143d209ea422128091e0e90b4b275f5c69f0d3e
          </Menu.Item>
            <Menu.Item key="1c19249621798315c2772d7bd0738cffbc68a77e">
                1c19249621798315c2772d7bd0738cffbc68a77e
          </Menu.Item>
            <Menu.Item key="1c19249621798315c2772d7bd0738cffbc68a77e">
                2odeqk2311798315c2772d7bd0738cffbc68a77e
          </Menu.Item>
            <Menu.Item key="1c19249621798315c2772d7bd0738cffbc68a77e">
                1c19249621798315c2772d7bd0738cffbc68a77e
          </Menu.Item>
        </Menu>
    );

    render() {
        
        return (
            <div>
                
                {(this.state.temp == 1) ? <div style={{justifyContent:'center', margin:'300px', height:'500px', textAlign:'center'}}>
                    <Icon type="loading" style={{ fontSize: 100}} spin />
                    </div>:
            <div>
                <br />
                <Row>
                    <Col span={8}>
                        <Title level={4}>{this.state.repo} <br/>Result Report</Title>
                    </Col>

                    <Col span={9} offset={6}>
                        <Dropdown overlay={this.branch_menu}>
                            <Button>
                                Branch | {this.state.set_branch ? this.state.set_branch : "master"} <Icon type="down" />
                            </Button>
                        </Dropdown>
                        <Dropdown overlay={this.commit_menu}>
                            <Button>
                                Commits | {this.state.set_commit ? this.state.set_commit : "893a5cb1135b8acb"} <Icon type="down" />
                            </Button>
                        </Dropdown>
                    </Col>
                </Row>


                <Card style={{ widht: '100%'}} >
                    <Descriptions title={'API Key'} column={1} size={'medium'} >

                        <Row>
                            <Col span={24} offset={1} style={{ display:'flex', flexDirection:'row'}}>
                                <div>
                                Detail
                                </div>
                                <div>
                                    &nbsp;&nbsp;
                                    /tts.js
                                </div>
                            </Col>

                            <Col span={20} offset={2} style={{ background: '#f6f6f6', height:'70px', width:'400px', display:'flex', flexDirection:'row'}}>
                                <div style={{fontSize:'10px' ,margin:'5px', paddingTop:'5px'}}>
                                    Line. 30&nbsp;&nbsp;&nbsp;&nbsp;var client_id = 'mndf5m4qeu';<br/>
                                    <div>Line. 31&nbsp;&nbsp;&nbsp;&nbsp;var client_secret = 
                                    <Popover content={<div><p>Use os.envrion instead of plain text code</p></div>}>
                                        <a style={{color:'#DB0000'}}>'RDchLs9M6iW3RtkjP3GMOnz87H8Pmz7IXhBjNCqF';</a>
                                    </Popover>
                                    <br/></div>
                                    Line. 32&nbsp;&nbsp;&nbsp;&nbsp;var fs = require('fs');<br/>
                                </div>
                            </Col>
                        </Row>
                        <Row>
                            <Col span={24} offset={1} style={{ display:'flex', flexDirection:'row'}}>
                                <div>
                                Detail
                                </div>
                                <div>
                                    &nbsp;&nbsp;
                                    /package.json.js
                                </div>
                            </Col>

                            <Col span={20} offset={2} style={{ background: '#f6f6f6', height:'70px', width:'400px', display:'flex', flexDirection:'row'}}>
                                <div style={{fontSize:'10px' ,margin:'5px', paddingTop:'5px'}}>
                                    Line. 30&nbsp;&nbsp;&nbsp;&nbsp;var client_id = 'mndf5m4qeu';<br/>
                                    <div>Line. 31&nbsp;&nbsp;&nbsp;&nbsp;var client_secret = 
                                    <Popover content={<div><p>Use os.envrion instead of plain text code</p></div>}>
                                        <a style={{color:'#DB0000'}}>'RDchLs9M6iW3RtkjP3GMOnz87H8Pmz7IXhBjNCqF'; </a>
                                    </Popover>
                                    <br/></div>
                                    Line. 32&nbsp;&nbsp;&nbsp;&nbsp;var fs = require('fs');<br/>
                                </div>
                            </Col>
                        </Row>
                        
                    </Descriptions>
                    
                    <Divider />
                   
                    <Descriptions title={'URL'} column={1} size={'medium'} >

                        <Row>
                            <Col span={24} offset={1} style={{ display:'flex', flexDirection:'row'}}>
                                <div>
                                Detail
                                </div>
                                <div>
                                    &nbsp;&nbsp;
                                    /src/main.js
                                </div>
                            </Col>

                            <Col span={20} offset={2} style={{ background: '#f6f6f6', height:'70px', width:'400px', display:'flex', flexDirection:'row'}}>
                                <div style={{fontSize:'10px' ,margin:'5px', paddingTop:'5px'}}>
                                    Line. 276&nbsp;&nbsp;&nbsp;&nbsp;<br/>
                                    <div>Line. 277&nbsp;&nbsp;&nbsp;&nbsp;axios.get(
                                    <Popover content={<p>Is it IP that you intend?</p>}>
                                    <a style={{color:'#DB0000'}}>'http://221.231.10.7:3030'</a>)</Popover><br/></div>
                                    
                                    Line. 278&nbsp;&nbsp;&nbsp;&nbsp;.then( res => \<br/>
                                </div>
                            </Col>
                        </Row>

                        <Row>
                            <Col span={24} offset={1} style={{ display:'flex', flexDirection:'row'}}>
                                <div>
                                Detail
                                </div>
                                <div>
                                    &nbsp;&nbsp;
                                    /package.json
                                </div>
                            </Col>

                            <Col span={20} offset={2} style={{ background: '#f6f6f6', height:'70px', width:'400px', display:'flex', flexDirection:'row'}}>
                                <div style={{fontSize:'10px' ,margin:'5px', paddingTop:'5px'}}>
                                    Line. 5&nbsp;&nbsp;&nbsp;&nbsp;[<br/>
                                    <div>Line. 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'proxy' = 
                                    <Popover content={<p>Is it IP that you intend?</p>}>
                                    <a style={{color:'#DB0000'}}>'pserver.hoho.co.kr'</a><br/></Popover></div>
                                    Line. 7&nbsp;&nbsp;&nbsp;&nbsp;]<br/>
                                </div>
                            </Col>
                        </Row>

                        <Row>
                            <Col span={24} offset={1} style={{ display:'flex', flexDirection:'row'}}>
                                <div>
                                Detail
                                </div>
                                <div>
                                    &nbsp;&nbsp;
                                    /src/component/route.js
                                </div>
                            </Col>

                            <Col span={20} offset={2} style={{ background: '#f6f6f6', height:'70px', width:'400px', display:'flex', flexDirection:'row'}}>
                                <div style={{fontSize:'10px' ,margin:'5px', paddingTop:'5px'}}>
                                    Line. 191&nbsp;&nbsp;&nbsp;&nbsp;#*#*#*#*#*#<br/>
                                    <div>Line. 192&nbsp;&nbsp;&nbsp;&nbsp;Redirect to=
                                    <Popover content={<p>Is it IP that you intend?</p>}>
                                    <a style={{color:'#DB0000'}}>'http://11.101.253.7'</a><br/></Popover></div>
                                    Line. 193&nbsp;&nbsp;&nbsp;&nbsp;#*#*#*#*#*#<br/>
                                </div>
                            </Col>
                        </Row>
                        
                    </Descriptions>

                    <Divider />
                    <Descriptions title={'Comment'} column={1} size={'medium'} >

                        <Row>
                            <Col span={24} offset={1} style={{ display:'flex', flexDirection:'row'}}>
                                <div>
                                Detail
                                </div>
                                <div>
                                    &nbsp;&nbsp;
                                    /src/components/main/set.js
                                </div>
                            </Col>

                            <Col span={20} offset={2} style={{ background: '#f6f6f6', height:'70px', width:'400px', display:'flex', flexDirection:'row'}}>
                                <div style={{fontSize:'10px' ,margin:'5px', paddingTop:'5px'}}>
                                    Line. 5&nbsp;&nbsp;&nbsp;&nbsp;let b_pwd = sessionStorage('gfwg') <br/>
                                    <div>Line. 6&nbsp;&nbsp;&nbsp;&nbsp;
                                    <Popover content={<p>exposed password comment</p>}>
                                    <a style={{color:'#DB0000'}}>//password default 11001100</a><br/></Popover></div>
                                    Line. 7&nbsp;&nbsp;&nbsp;&nbsp;<br/>
                                </div>
                            </Col>
                        </Row>
                        
                    </Descriptions>

                    <Divider />
                </Card>

            </div>}
        </div>
        )
    }

}

export default Report;