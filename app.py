"""Find and record references to a person or brand on the Internet."""

import sys
import json
import pprint

from flask import Flask, make_response, render_template, jsonify, send_from_directory
from flask.ext.sqlalchemy import SQLAlchemy
from birdy.twitter import AppClient

from models import Source, Mention, Base

CONSUMER_KEY = 'XCvzOpRBPjKoWFMSYnHqHg'
CONSUMER_SECRET = 'flO2rrzu6xss6ubnJUS8hp0nhgbSYp8cjjCjnaHCzG8'
client = AppClient(CONSUMER_KEY, CONSUMER_SECRET)
access_token = client.get_access_token()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///sqlite.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/partials/<name>')
def partials(name):
    return send_from_directory('partials', name)

def get_twitter_mentions():
    response = client.api.search.tweets.get(q='jeffknupp.com', count=100)
    statuses = response.data.statuses
    session = db.session()
    twitter = session.query(Source).get(1)
    for status in statuses:
        if not session.query(Mention).filter(Mention.domain_id==status.id_str).count():
            m = Mention(text=status.text,
                    associated_user='{} ({})'.format(status.user.screen_name,
                        status.user.followers_count),
                    source=twitter,
                    domain_id=status.id_str)
            session.add(m)
    session.commit()

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
    app.run(debug=True)

if __name__ == '__main__':
    sys.exit(main())
