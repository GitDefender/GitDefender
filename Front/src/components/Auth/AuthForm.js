import React from "react";
import {Link} from "react-router-dom";
import {Form, Input, Button} from "antd";
import "antd/dist/antd.css";
import "./auth.css"

const FormItem = Form.Item;

const AuthForm = (
    {
        kind,
        onChangeInput,
        username,
        email,
        password,
        onLogin,
        onRegister,
        error
    }) => {
    const handleChange = e => {
        const {name, value} = e.target;
        onChangeInput({name, value});
    };

    const handleKeyPress = e => {
        if (e.key === "Enter") {
            switch (kind) {
                case "register":
                    onRegister();
                    return;
                case "login":
                    onLogin();
                    return;
                default:
                    return;
            }
        }
    };
    return (
        <div className={"limiter"}>
            <div className={"container-login100"}>
                <div className={"login100-form validate-form"}>
                    <div className={"title"}>{kind.toUpperCase()}</div>
                    <div className={"line-wrapper"}>
                        <div className={"input-title"}>username</div>
                        <Input
                            type="text"
                            name="username"
                            value={username}
                            onChange={handleChange}
                            onKeyPress={handleKeyPress}
                        />
                    </div>
                    <div className={"line-wrapper"}>
                        <div className={"input-title"}>password</div>
                        <Input
                            type="password"
                            name="password"
                            value={password}
                            onChange={handleChange}
                            onKeyPress={handleKeyPress}
                        />
                    </div>
                    {kind === "register" ? (
                        <div>
                            <div className={"line-wrapper"}>
                                <div className={"input-title"}>email</div>
                                <Input
                                    type="email"
                                    name="email"
                                    value={email}
                                    onChange={handleChange}
                                    onKeyPress={handleKeyPress}
                                />
                            </div>
                            <Button className={"register-button"} onClick={onRegister}>
                                {kind.toUpperCase()}
                            </Button>
                        </div>
                    ) : (
                        <Button className={"login-button"} onClick={onLogin}>
                            {kind.toUpperCase()}
                        </Button>
                    )}
                    <br/>
                    {kind === "register" ? (
                        <Link to={`/auth/login`} className={"description"}>
                            if you already have account...
                        </Link>
                    ) : (
                        <Link to={`/auth/register`} className={"description"}>
                            if you don't have an account...
                        </Link>
                    )}
                </div>
                <div className={"login100-more"}>
                </div>
            </div>
        </div>
    );
};

export default AuthForm;