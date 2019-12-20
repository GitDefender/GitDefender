import React, {Component} from 'react';
import RepoInfo from './RepoInfo';

class RepoInfoList extends Component {
    static defaultProps = {
        data: []
    }

    render() {
        const {data} = this.props;
        const list = data.map(
            info => (<RepoInfo key={info.name} info={info}/>)
        );

        return (
            <div>
                {list}
            </div>
        );
    }
}

export default RepoInfoList;