from sqlalchemy import create_engine, Column, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import uuid
from datetime import date

user_base = declarative_base()

class user(user_base):
    __tablename__ = "users"
    userid = Column("id", String, primary_key=True, default=str(uuid.uuid4()))
    username =  Column("name", String)
    usersurname = Column("surname", String)
    userbirth = Column("birthday", Date)
    def __init__(self, username, usersurname, userbirth):
        self.username = username
        self.surname = usersurname
        #userid generate id????????????????????////
        self.userbirth = userbirth
    
 