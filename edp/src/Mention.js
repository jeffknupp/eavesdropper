import React, { Component } from 'react';
import './Mention.css';

class Mention extends Component {
    render() {
        var is_read = this.props.mention.read ? 'unread' : 'read';
        return (
        <li>
            <div className={is_read}>
                <p className="user">{this.props.mention.associated_user}</p>
                <p className="text">{this.props.mention.text}</p>
            </div>
        </li>
        );
    };
}

export default Mention;
                
