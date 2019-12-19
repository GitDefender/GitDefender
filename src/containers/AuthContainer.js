import React, {Component} from "react";
import {connect} from "react-redux";
import AuthForm from "../components/Auth/AuthForm";
import {withRouter} from "react-router-dom";
import * as authActions from "../modules/auth";
import Header from "../components/structure/Header";

export class AuthContainer extends Component {
    componentDidMount() {
        const {initializeInput} = this.props;
        this.initialize();
    }

    componentDidUpdate(prevProps, prevState) {
        const {history} = this.props;
        if (prevProps.kind !== this.props.kind) {
            this.initialize();
        }

        if (prevProps.logged !== this.props.logged && this.props.logged) {
            localStorage.setItem(
                "userInfo",
                JSON.stringify({
                    id: this.props.userInfo.id,
                    username: this.props.username
                }),
            );

            localStorage.setItem(
                "token",
                JSON.stringify({
                    token: this.props.token
                }),
                console.log(this.props),
            );
            history.push("/");
        }
    }

    handleChangeInput = ({name, value}) => {
        const {changeInput} = this.props;
        changeInput({name, value});
    };

    initialize = () => {
        const {initializeInput, initializeError} = this.props;
        initializeError();
        initializeInput();
    };

    handleLogin = () => {
        const {login} = this.props;
        login();
    };

    handleRegister = () => {
        const {register} = this.props;
        register();
    };

    render() {
        const {kind, username, email, password, error} = this.props;
        const {handleChangeInput, handleLogin, handleRegister} = this;
        return (
            <AuthForm
                kind={kind}
                username={username}
                email={email}
                password={password}
                onChangeInput={handleChangeInput}
                onLogin={handleLogin}
                onRegister={handleRegister}
                error={error}
            />
        );
    }
}

const mapStateToProps = state => ({
    id: state.auth.form.id,
    username: state.auth.form.username,
    email: state.auth.form.email,
    password: state.auth.form.password,
    userInfo: state.auth.userInfo,
    token: state.auth.token,
    logged: state.auth.logged,
    error: state.auth.error
});

const mapDispatchToProps = dispatch => {
    return {
        initializeInput: () => {
            dispatch(authActions.initializeInput());
        },
        changeInput: ({name, value}) => {
            dispatch(authActions.changeInput({name, value}));
        },
        initializeError: () => {
            dispatch(authActions.initializeError());
        },
        register: () => {
            dispatch(authActions.register());
        },
        login: () => {
            dispatch(authActions.login());
        }
    };
};

export default withRouter(
    connect(
        mapStateToProps,
        mapDispatchToProps
    )(AuthContainer)
);