from sqlalchemy import create_engine, Column, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
music_base = declarative_base()


class artist(music_base): 
    __tablename__ = "artist"
    artistid = Column("artistid", String, primary_key=True)
    artistname = Column("artistname", String)
    def __init__(self, artistname):
        self.artistname = artistname
class album(music_base):
    __tablename__ = "album"
    albumid = Column("albumid", String, primary_key=True)
    albumname = Column("albumname", String)
    albumartist = Column("artistid", String, ForeignKey("artist.artistid"))
    released = Column("released", Date)

    def __init__(self, albumname, released, artistid):
        self.albumname = albumname
        self.released = released
        self.artistid = artistid


class Track(music_base):
    '''track'''
    __tablename__ = "track"
    trackid = Column("trackid", String, primary_key=True)
    trackname = Column("trackname", String)

    def __init__(self, trackname, albumid):
        self.trackname = trackname
        self.albumid = albumid

class ListeningHistory(music_base):
    __tablename__ = "listening_history"
    userid = Column("userid", String, ForeignKey("users.userid"))
    trackid = Column("trackid", String, ForeignKey("track.trackid"))
    listened_at = Column("listened_at", datetime, default=datetime.datetime.now())
    
MDB = "sqlite:///music_base.db"
engine = create_engine(MDB)
music_base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
