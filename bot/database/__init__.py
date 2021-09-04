from sqlalchemy import create_engine
from sqlalchemy import Column, String, BigInteger, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import Boolean

from config import config as CONFIG

Base = declarative_base()

class Sticker(Base):
    __tablename__ = 'sticker'
    telegram_user_id = Column(BigInteger)
    telegram_sticker_name = Column(String(64))
    telegram_sticker_title = Column(String(64))
    telegram_sticker_url = Column(String(255))
    line_sticker_id = Column(String(32), primary_key=True)
    status = Column(Integer) # 0: processing, 1: available

    def __init__(self, user_id, name, title, url, sticker_id):
        self.telegram_user_id = user_id
        self.telegram_sticker_name = name
        self.telegram_sticker_title = title
        self.telegram_sticker_url = url
        self.line_sticker_id = sticker_id

    def __repr__(self):
        return f'<Sticker(title={self.telegram_sticker_title}, id={self.line_sticker_id}>)'

engine = create_engine(f'sqlite:///{CONFIG.APP.DATABASE}', echo=True)
Base.metadata.create_all(engine, checkfirst=True)
Session = sessionmaker(bind=engine)

def insert(user_id, name, title, url, line_sticker_id):
    with Session() as session:
        session.begin()
        try:
            session.add(Sticker(user_id, name, title, url, line_sticker_id))
        except:
            session.rollback()
            raise
        else:
            session.commit()
    return session.query(Sticker).filter_by(line_sticker_id=line_sticker_id).first()

def delete(line_sticker_id):
    with Session() as session:
        session.begin()
        try:
            session.query(Sticker).filter_by(line_sticker_id=line_sticker_id).delete()
        except:
            session.rollback()
            raise
        else:
            session.commit()

def search(line_sticker_id):
    with Session() as session:
        return session.query(Sticker).filter_by(line_sticker_id=line_sticker_id).first()
