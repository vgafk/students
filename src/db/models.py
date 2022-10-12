from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship
from .base import Base, init_models


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    surname = Column(String(length=255), nullable=False)
    name = Column(String(length=255), nullable=False)
    middle_name = Column(String(length=255), nullable=True)
    snils = Column(String(length=20), nullable=True, unique=True)
    inn = Column(String(length=20), nullable=True)
    email = Column(String(length=255), nullable=True)
    phone = Column(String(length=15), nullable=True)
    study_year = Column(Integer, nullable=False)
    student_data = relationship('StudentData', backref='user')
    absenteeism = relationship('Absenteeism', backref='user')


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String(length=20), nullable=False, unique=True)
    full_name = Column(String(length=255), nullable=True)
    student_data = relationship('StudentData', backref='group')


class StudentData(Base):
    __tablename__ = "student_data"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    user_id = Column(ForeignKey("users.id"))
    group_id = Column(ForeignKey("groups.id"))
    degree_doc = Column(String(), nullable=False)
    graduation_date = Column(Date, nullable=True)


class Absenteeism(Base):
    __tablename__ = 'absenteeism'
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    user_id = Column(ForeignKey("users.id"))
    date = Column(DateTime)
    class_number = Column(Integer)
