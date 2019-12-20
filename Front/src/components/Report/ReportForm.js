import React, {Component} from "react";
import "./reportform.css";
import {Link} from "react-router-dom";
import {Menu, Dropdown, Button, Icon, message} from "antd";
import "antd/dist/antd.css";


class ReportForm extends Component {
    constructor(props) {
        super(props);
        this.handleMenuClick = this.handleMenuClick.bind(this);
        this.handleButtonClick = this.handleButtonClick.bind(this);
    }

    handleButtonClick() {
        message.info('Click on left button.');
        console.log('click left button');
    }

    handleMenuClick() {
        message.info('Click on menu item.');
        console.log('click');
    }

    render() {
        const menu = (
            <Menu onClick={this.handleMenuClick}>
                <Menu.Item key="1">
                    <Icon type="user"/>
                    1st menu item
                </Menu.Item>
                <Menu.Item key="2">
                    <Icon type="user"/>
                    2nd menu item
                </Menu.Item>
                <Menu.Item key="3">
                    <Icon type="user"/>
                    3rd item
                </Menu.Item>
            </Menu>
        )
        return (
            <form>
                <Dropdown overlay={menu}/>
                <div id="components-dropdown-demo-dropdown-button">
                    <Dropdown.Button onClick={this.handleButtonClick} overlay={menu}>
                        Dropdown
                    </Dropdown.Button>
                    <Dropdown.Button overlay={menu} icon={<Icon type="user"/>}>
                        Dropdown
                    </Dropdown.Button>
                    <Dropdown.Button onClick={this.handleButtonClick} overlay={menu} disabled>
                        Dropdown
                    </Dropdown.Button>
                    <Dropdown overlay={menu}>
                        <Button>
                            Button <Icon type="down"/>
                        </Button>
                    </Dropdown>
                </div>
            </form>
        );
    }
}
;

export default ReportForm;