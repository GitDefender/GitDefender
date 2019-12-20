import React, { Component } from 'react';
import {Redirect} from 'react-router-dom';
import { Form, Icon, Input, Button, Checkbox, Alert } from 'antd';
import {
    Tooltip, notification,
} from 'antd';
import axios from 'axios';

import { auth_login, auth_register } from './api.js';

class Login extends Component {
    constructor(props) {
        super(props);

        this.state = {
            login_status: NaN
        }
    }

    handleSubmit = e => {
        e.preventDefault();
        this.props.form.validateFields((err, values) => {
            if (!err) {
                console.log('Received values of form: ', values.username, values.password);
                //Login
                axios.post(auth_login, {
                    username: values.username,
                    password: values.password
                })
                    .then((response) => {
                        console.log(response)
                        this.setState({ login_status: response.data.token })
                        sessionStorage.setItem('GdfToken', "Token " + response.data.token)
                        sessionStorage.setItem('name', response.data.user.username)

                        this.setState({login_status: 200})
                    })
                    .catch((err) => {
                        console.log(err.response)
                        this.setState({ login_status: err.response.status })
                    })

            }
        });
    };

    LoginFailedNotify = () => {
        notification.info({
            message: `Login Failed`,
            description:
                "Login has been failed. Check your username & password",
            placement: "bottomLeft",
            duration: 1.5
        });
        this.setState({ login_status: NaN })
    };


    render() {
        const { getFieldDecorator } = this.props.form;

        return (

            <div>
                {this.state.login_status == 200 ? <Redirect to='/'/> : ''}
                {this.state.login_status == 400 ? this.LoginFailedNotify() : ''}

                <Form onSubmit={this.handleSubmit} className="login-form">
                    <Form.Item>
                        {getFieldDecorator('username', {
                            rules: [{ required: true, message: 'Please input your username!' }],
                        })(
                            <Input
                                prefix={<Icon type="user" style={{ color: 'rgba(0,0,0,.25)' }} />}
                                placeholder="Username"
                            />,
                        )}
                    </Form.Item>
                    <Form.Item>
                        {getFieldDecorator('password', {
                            rules: [{ required: true, message: 'Please input your Password!' }],
                        })(
                            <Input
                                prefix={<Icon type="lock" style={{ color: 'rgba(0,0,0,.25)' }} />}
                                type="password"
                                placeholder="Password"
                            />,
                        )}
                        <a className="login-form-forgot" href="">
                            Forgot password
                        </a>
                    </Form.Item>
                    <Form.Item>
                        <Button type="primary" htmlType="submit" className="login-form-button">
                            Log in
                        </Button>
                        &nbsp; Or <a href="/register">register now!</a>
                    </Form.Item>
                </Form>
            </div>
        )
    }
}

class Register extends Component {
    constructor(props) {
        super(props);

        this.state = {
        }
    }

    handleSubmit = e => {
        e.preventDefault();
        this.props.form.validateFieldsAndScroll((err, values) => {
            if (!err) {
                console.log('Received values of form: ', values);

                axios.post(auth_register, {
                    username: values.username,
                    email: values.email,
                    password: values.password
                })
                    .then((response) => {
                        console.log(response)
                        this.setState({ login_status: response.data.token })
                        sessionStorage.setItem('GdfToken', "Token " + response.data.token)
                        sessionStorage.setItem('name', response.data.user.username)


                    })
                    .catch((err) => {
                        console.log(err.response)
                        this.setState({ login_status: err.response.status })
                    })
            }
        });
    };

    handleConfirmBlur = e => {
        const { value } = e.target;
        this.setState({ confirmDirty: this.state.confirmDirty || !!value });
    };

    compareToFirstPassword = (rule, value, callback) => {
        const { form } = this.props;
        if (value && value !== form.getFieldValue('password')) {
            callback('Two passwords that you enter is inconsistent!');
        } else {
            callback();
        }
    };

    validateToNextPassword = (rule, value, callback) => {
        const { form } = this.props;
        if (value && this.state.confirmDirty) {
            form.validateFields(['confirm'], { force: true });
        }
        callback();
    };

    handleWebsiteChange = value => {
        let autoCompleteResult;
        if (!value) {
            autoCompleteResult = [];
        } else {
            autoCompleteResult = ['.com', '.org', '.net'].map(domain => `${value}${domain}`);
        }
        this.setState({ autoCompleteResult });
    };

    render() {
        const { getFieldDecorator } = this.props.form;
        const { autoCompleteResult } = this.state;

        const formItemLayout = {
            labelCol: {
                xs: { span: 24 },
                sm: { span: 8 },
            },
            wrapperCol: {
                xs: { span: 24 },
                sm: { span: 16 },
            },
        };

        const tailFormItemLayout = {
            wrapperCol: {
                xs: {
                    span: 24,
                    offset: 0,
                },
                sm: {
                    span: 16,
                    offset: 8,
                },
            },
        };

        return (
            <Form {...formItemLayout} onSubmit={this.handleSubmit}>
                <Form.Item
                    label={
                        <span>
                            Username&nbsp;
                            <Tooltip title="It will be your ID">
                                <Icon type="question-circle-o" />
                            </Tooltip>
                        </span>
                    }>
                    {getFieldDecorator('username', {
                        rules: [
                            {
                                required: true,
                                message: 'Please input your Username!',
                            },
                            {
                                pattern: new RegExp("[a-zA-Z0-9@/./+/-/_]{1,150}"),
                                message: 'Must Contain Alphanumerics!',
                            }
                        ],
                    })(<Input />)}
                </Form.Item>
                <Form.Item label="E-mail">
                    {getFieldDecorator('email', {
                        rules: [
                            {
                                type: 'email',
                                message: 'The input is not valid E-mail!',
                            },
                            {
                                required: true,
                                message: 'Please input your E-mail!',
                            },

                        ],
                    })(<Input />)}
                </Form.Item>
                <Form.Item label="Password" hasFeedback>
                    {getFieldDecorator('password', {
                        rules: [
                            {
                                required: true,
                                message: 'Please input your password!',
                            },
                            {
                                validator: this.validateToNextPassword,
                            },
                            {
                                pattern: new RegExp("^.*(?=^.{8,15}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&+=]).*$"),
                                message: 'Can contain Alphanumeric, !@#$%^&+=',
                            }

                        ],
                    })(<Input.Password />)}
                </Form.Item>
                <Form.Item label="Confirm Password" hasFeedback>
                    {getFieldDecorator('confirm', {
                        rules: [
                            {
                                required: true,
                                message: 'Please confirm your password!',
                            },
                            {
                                pattern: new RegExp("^.*(?=^.{8,15}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&+=]).*$"),
                                message: 'Can contain Alphanumeric, !@#$%^&+=',
                                validator: this.compareToFirstPassword,
                            },
                        ],
                    })(<Input.Password onBlur={this.handleConfirmBlur} />)}
                </Form.Item>

                <Form.Item {...tailFormItemLayout}>
                    {getFieldDecorator('agreement', {
                        valuePropName: 'checked',
                    })(
                        <Checkbox>
                            I have read the <a href="">agreement</a>
                        </Checkbox>,
                    )}
                </Form.Item>
                <Form.Item {...tailFormItemLayout}>
                    <Button type="primary" htmlType="submit">
                        Register
          </Button>
                </Form.Item>
            </Form>
        )
    }
}
const LoginForm = Form.create()(Login);
const RegisterForm = Form.create()(Register);

export {
    LoginForm,
    RegisterForm
};