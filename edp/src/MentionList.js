import React, { Component } from 'react';
import './MentionList.css';
import Mention from './Mention.js';

class MentionList extends Component {
    render() {
        var items = [];
        this.props.items.forEach(function(mention) {
            items.push(<Mention mention={mention} />);
        });
        return (
            <div className="MentionList">
                <ul> 
                    {items}
                </ul>
            </div>
        );
    }
}

export default MentionList;
