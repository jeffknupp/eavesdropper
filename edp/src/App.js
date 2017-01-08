import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import MentionList from './MentionList.js';

var MENTIONS = [
    {read: false, associated_user: 'jeffknupp', text:'That was soooo helpful'},
    {read: false, associated_user: 'erknupp', text:'No it wasn\'t'},
    {read: true, associated_user: 'coolguy', text:'Love iT!'}
];


class App extends Component {
  render() {
    return (
      <div className="App">
            <MentionList items={MENTIONS} />
      </div>
    );
  }
}


export default App;
