import React, {Component} from 'react';

class RepoInfo extends Component {
    static defaultProps = {
        info: {
            name: '',
            url: '',
            latest_commit: '',
            latest_scan: ''
        }
    }

    render() {
        const style = {
            border: '1px solid black',
            padding: '8px',
            margin: '8px'
        };

        const {
            name, url, latest_commit, latest_scan
        } = this.props.info;

        return (
            <div style={style}>
                <div><b>{name} | {url} | {latest_commit} | {latest_scan}</b>
                    <button>Scan</button>
                    <button>Report</button>
                </div>

            </div>
        );
    }
}

export default RepoInfo;