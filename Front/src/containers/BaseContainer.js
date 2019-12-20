import React, {Component} from "react";
import {connect} from "react-redux";
import * as authActions from "../store/modules/auth";
import {withRouter} from "react-router-dom";

export class BaseContainer extends Component {/*
  componentDidMount() {
    this.props.checkUser();
  }*/
    componentDidUpdate(prevProps, prevState) {
        if (prevProps.logged !== this.props.logged && !this.props.logged) {
            window.location.href = "/auth/login";
        }
    }/*
  checkUser = () => {
    const {checkUser, setUserTemp, history} = this.props;

    if (localStorage.getItem("userInfo")) {
      const userInfo = JSON.parse(localStorage.getItem("userInfo"));
      setUserTemp({
        id: userInfo.id,
        username: userInfo.username,
        token: userInfo.token
      });
      return;
    }

    checkUser();

    if (!this.props.logged && !window.location.pathname.includes("auth")) {
      history.push("http://test.gitdefender.com:8080/api/v1/auth/login");
    }
  };*/

    render() {
        return <div/>;
    }
}

const mapStateToProps = state => ({
    logged: state.auth.logged
});

const mapDispatchToProps = dispatch => {
    return {/*
    checkUser: () => {
      dispatch(authActions.checkUser());
    },*/
        setUserTemp: ({id, username}) => {
            dispatch(authActions.setUserTemp({id, username}));
        }
    };
};

export default withRouter(
    connect(
        mapStateToProps,
        mapDispatchToProps
    )(BaseContainer)
);