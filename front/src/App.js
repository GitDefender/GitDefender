import React, { Component } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

import { Layout, Icon } from 'antd';
import { Row, Col } from 'antd';

import 'antd/dist/antd.css'

import RepoList from './component/repo-list';
import LoginLayout from './component/LoginLayout';
import { RegisterForm, LogIn, LogOut } from './component/authForm';
import Report, {rere} from './component/report';

const { Header, Content, Footer } = Layout;

class App extends Component {

  constructor(props) {
    super(props);
    
    this.state = {

    }
  }

  render() {
    return (
      <Layout className="layout">

        <Header>
          <Row>
            <Col span={12} style={{ color: 'white' }}><a href='/'>GitDefender</a></Col>
            <Col span={2} offset={10} style={{ align: 'right', color: 'white' }}>{sessionStorage.getItem('GdfToken') ? <LogOut/> : ''}</Col>
          </Row>

        </Header>

        <Content style={{ padding: '0 50px' }}>
          <BrowserRouter>
            <Switch>
              <Route exact path="/" component={RepoList} />
              <Route path="/login" component={LoginLayout} />
              <Route path="/register" component={RegisterForm} />
              <Route path="/user" component={RepoList} />
              <Route path="/report/:repo/:branch/:sha" component={Report} />
              <Route path="/report/:repo" component={Report} />
              
            </Switch>
          </BrowserRouter>

          
        </Content>

        <Footer style={{ textAlign: 'center' }}>
        <Icon type="copyright" /> UginHack-GitDefender
    </Footer>
      </Layout>
    );
  }
}

export default App;
