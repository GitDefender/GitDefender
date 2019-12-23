import React, { Component } from 'react';
import { Row, Col, Typography } from 'antd';
import { LoginForm } from './authForm'

const { Title } = Typography;

class LoginLayout extends Component {
    constructor(props) {
        super(props);
        this.state = {

        }
    }

    render() {
        return (
            <div>
                <br/>
                <br/>
                <Row style={{justifyContent:'center'}}>
                    <Col span={12}>
                        <Title level={3}>
                            Git Defender를 통해 당신의 Repository를 지키세요
                            <br/>
                            개발자의 실수로 나타나는 중요정보유출을 막아드립니다
                        </Title>
                    </Col>

                    <Col span={8} offset={4}>
                        <LoginForm />

                    </Col>
                </Row>
            </div>
        )
    }
}

export default LoginLayout;