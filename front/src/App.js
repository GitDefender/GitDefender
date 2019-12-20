import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

import { Layout, Menu, Breadcrumb } from 'antd';
import { Row, Col } from 'antd';

import 'antd/dist/antd.css'

import RepoList from './component/repo-list';
import LoginLayout from './component/LoginLayout';
import {RegisterForm} from './component/authForm';


const { Header, Content, Footer } = Layout;

const App = () => {
  return (
    <Layout className="layout">

    <Header>
      <Row>
        <Col span={12} style={{color:'white'}}><a href='/'>GitDefender</a></Col>
        <Col span={2} offset={10} style={{align:'right', color:'white'}}>Login</Col>
      </Row>
        
    </Header>

    <Content style={{ padding: '0 50px' }}>
        <BrowserRouter>
          <Switch>
            <Route exact path="/" component={RepoList} />
            <Route path="/login" component={LoginLayout} />
            <Route path="/register" component={RegisterForm} />
            <Route path="/user" component={RepoList} />
          </Switch>
        </BrowserRouter>



      <div style={{ background: '#FFFFFF', padding: 24, minHeight: 280 }}>Content</div>
    </Content>

    <Footer style={{ textAlign: 'center' }}>
      Footer Area
    </Footer>
  </Layout>
  );
}

export default App;
