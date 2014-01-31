"""Find and record references to a person or brand on the Internet."""

import sys
import json
import pprint
import argparse

from flask import Flask, make_response, render_template, jsonify, send_from_directory
from flask.ext.sqlalchemy import SQLAlchemy
from birdy.twitter import AppClient

from models import Source, Mention, Base
from twitter import get_twitter_mentions

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///sqlite.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/partials/<name>')
def partials(name):
    return send_from_directory('partials', name)

@app.route('/update/<source>', methods=['POST'])
def get_updates_for_source(source):
    if source == 'twitter':
        updates = get_twitter_mentions()
        return jsonify({'updates': updates})


@app.route('/read/<id>', methods=['POST'])
def read(id):
    session = db.session()
    mention = session.query(Mention).get(id)
    mention.seen = True
    session.add(mention)
    session.commit()
    return jsonify({})

@app.route('/mentions')
def show_mentions():
    session = db.session()
    mentions = session.query(Mention).all()
    values = [mention.to_json() for mention in mentions]
    response = make_response()
    response.data = json.dumps(values)
    return response
    
def main():
    app.run(host="0.0.0.0", port=8080, debug=True)
if __name__ == '__main__':
    sys.exit(main())
