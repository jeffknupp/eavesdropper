"""Find and record references to a person or brand on the Internet."""

import sys
import pprint

from birdy.twitter import AppClient

from sqlalchemy import create_engine
from models import Source, Mention, Base
from sqlalchemy.orm import sessionmaker

CONSUMER_KEY = 'XCvzOpRBPjKoWFMSYnHqHg'
CONSUMER_SECRET = 'flO2rrzu6xss6ubnJUS8hp0nhgbSYp8cjjCjnaHCzG8'
client = AppClient(CONSUMER_KEY, CONSUMER_SECRET)
access_token = client.get_access_token()

engine = create_engine('sqlite:///sqlite.db')
Session = sessionmaker(bind=engine)

def get_twitter_mentions():
    response = client.api.search.tweets.get(q='jeffknupp.com', count=100)
    statuses = response.data.statuses
    session = Session()
    twitter = session.query(Source).get(1)
    for status in statuses:
        if not session.query(Mention).filter(Mention.domain_id==status.id_str).count():
            m = Mention(text=status.text,
                    associated_user='{} ({})'.format(status.user.screen_name,
                        status.user.followers_count),
                    source=twitter,
                    domain_id=status.id_str)
            session.add(m)
        else:
            print 'Skipping already seen mention'

    session.commit()

def show_mentions():
    session = Session()
    mentions = session.query(Mention).all()
    
def main():
    get_twitter_mentions()

if __name__ == '__main__':
    sys.exit(main())
