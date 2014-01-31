import datetime

from flask import make_response, render_template, jsonify, send_from_directory
from sqlalchemy import create_engine

from flask.ext.sqlalchemy import SQLAlchemy
from birdy.twitter import AppClient

from models import Source, Mention

engine = create_engine('sqlite+pysqlite:///sqlite.db')
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

CONSUMER_KEY = 'XCvzOpRBPjKoWFMSYnHqHg'
CONSUMER_SECRET = 'flO2rrzu6xss6ubnJUS8hp0nhgbSYp8cjjCjnaHCzG8'
client = AppClient(CONSUMER_KEY, CONSUMER_SECRET)
access_token = client.get_access_token()
QUERIES = ['jeffknupp.com', 'jeffknupp']

def get_twitter_mentions():
    statuses = []
    for query in QUERIES:
        response = client.api.search.tweets.get(q='jeffknupp.com', count=100)
        statuses += response.data.statuses
    session = Session()
    twitter = session.query(Source).get(1)
    new_mentions = 0
    for status in statuses:
        if not session.query(Mention).filter(Mention.domain_id==status.id_str).count():
            created_at = datetime.datetime.strptime(status.created_at, r"%a %b %d %H:%M:%S +0000 %Y")
            m = Mention(text=status.text,
                    associated_user='{} ({})'.format(status.user.screen_name,
                        status.user.followers_count),
                        recorded_at=datetime.datetime.now(),
                        occurred_at=created_at,
                        source=twitter,
                        domain_id=status.id_str)
            new_mentions += 1
            session.add(m)
    session.commit()
    return new_mentions

if __name__ == '__main__':
    mentions = get_twitter_mentions()
    print "{} new Twitter mentions".format(mentions)
