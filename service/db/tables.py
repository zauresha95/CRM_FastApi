from sqlalchemy import create_engine
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

# Create sqlite engine instance
engine = create_engine("sqlite:///crm.sqlite")
# engine = create_engine("postgresql+psycopg2://postgres@127.0.0.1:5432/postgres")
# Create declaritive base meta instance
Base = declarative_base()
# Create session local class for session maker
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


class ClientCabinet(Base):
    """ Table client_cabinet """
    __tablename__ = 'client_cabinet'
    client_id = Column(Integer, primary_key=True)
    name = Column(String(200))
    surname = Column(String(200))
    email = Column(String(200))
    phone = Column(Integer)
    date_of_birth = Column(String(200))
    created = Column(DateTime(), server_default=func.now())
    updated = Column(DateTime(), server_default=func.now())


class AdminCabinet(Base):
    """ Table admin_cabinet """
    __tablename__ = 'admin_cabinet'
    admin_id = Column(Integer, primary_key=True)
    name = Column(String(200))
    surname = Column(String(200))
    email = Column(String(200))
    phone = Column(Integer)
    date_of_birth = Column(String(200))
    created = Column(DateTime(), server_default=func.now())
    updated = Column(DateTime(), server_default=func.now())


class Deals(Base):
    """ Table deals between admins and clients """
    __tablename__ = 'deals'
    id = Column(Integer, primary_key=True)
    deal_id = Column(Integer)
    admin_id = Column(Integer)
    client_id = Column(Integer)
    status = Column(String(200))
    created = Column(DateTime(), server_default=func.now())
    updated = Column(DateTime(), server_default=func.now())


class DealsInfo(Base):
    """ Table deals_description contains additional info about deals """
    __tablename__ = 'deals_info'
    id = Column(Integer, primary_key=True)
    status = Column(String(200))
    purch_amount = Column(Integer)
    created = Column(DateTime(), server_default=func.now())
    updated = Column(DateTime(), server_default=func.now())


class AdminInfo(Base):
    """ Table admin info """
    __tablename__ = 'admin_info'
    admin_id = Column(Integer, primary_key=True)
    cnt_success_deals = Column(Integer)
    reputation = Column(Integer)
    created = Column(DateTime(), server_default=func.now())
    updated = Column(DateTime(), server_default=func.now())


class ClientHot(Base):
    """ Table contains hot clients """
    __tablename__ = 'client_hot'
    client_id = Column(Integer, primary_key=True)
    created = Column(DateTime(), server_default=func.now())
    updated = Column(DateTime(), server_default=func.now())