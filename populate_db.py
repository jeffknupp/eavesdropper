from sqlalchemy import create_engine
from models import Source, Mention, Base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///sqlite.db')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine) 
session = Session()

s = Source(id=1, name='Twitter')
m = Mention(id=1, source=s, text='jeffknupp.com is the best website ever!')
session.add(s)
session.add(m)
session.commit()
