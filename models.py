from datetime import datetime, timedelta, timezone
from database import Base
from sqlalchemy import DATE, DATETIME, Boolean, Column, Date, DateTime, ForeignKey, Integer, String, Sequence, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id_seq = Sequence('USER_ID_SEQ', metadata=Base.metadata, start=1)
    ROLE_USER, ROLE_COUNSELOR = 0, 1
    id = Column(Integer, id_seq, primary_key=True)
    email = Column(String(100), nullable=False, unique=True)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    role = Column(Integer, default=ROLE_USER, nullable=False)
