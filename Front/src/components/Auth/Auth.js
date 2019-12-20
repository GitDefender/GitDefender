import React from "react";
import AuthForm from "./";

const Auth = ({match}) => {
    const {kind} = match.params;
    return (
        <div>
            <AuthForm kind={kind}/>
        </div>
    );
};

export default Auth;