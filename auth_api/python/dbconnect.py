from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from config import CFG
from model import User

dbengine = CFG["database"]["engine"]
dbuser = CFG["database"]["user"]
dbhost = CFG["database"]["host"]
dbpass =  CFG["database"]["password"]
dbname = CFG["database"]["name"]

# Create a database engine
engine = create_engine(f'{dbengine}+pymysql://{dbuser}:{dbpass}@{dbhost}/{dbname}')
# Create a session object
Session = sessionmaker(bind=engine)

def get_userdata(username):
    query = select(User).where(User.username == username)

    with Session() as session:
        user_data = session.scalars(query).first() or User(username="", password="", salt="", role="")

    return user_data