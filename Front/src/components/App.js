import React, {Component} from "react";
import "antd/dist/antd.css";
import {Switch, Route} from "react-router-dom";
import {Main, Auth, NotFound, Report} from "../pages";
import BaseContainer from "../containers/BaseContainer";

class App extends Component {
    render() {
        return (
            <div>
                <Switch>
                    <Route path="/auth/:kind" exact={true} component={Auth}/>
                    <Route path="/report" exact={true} component={Report}/>
                    <Route path="/" exact={true} component={Main}/>
                    <Route component={NotFound}/>
                </Switch>
                <BaseContainer/>
            </div>
        )
    }
}

export default App;