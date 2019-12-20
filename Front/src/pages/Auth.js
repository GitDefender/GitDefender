import React from "react";
import "antd/dist/antd.css";
import AuthContainer from "../containers/AuthContainer";

const Auth = ({match}) => {
    const {kind} = match.params;
    return (
        <div>
            <AuthContainer kind={kind}/>
        </div>
    );
};

export default Auth;