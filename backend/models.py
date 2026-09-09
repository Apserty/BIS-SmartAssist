from sqlalchemy import Column, Integer, String, Text
from database import Base


class Standard(Base):
    __tablename__ = "standards"

    id = Column(Integer, primary_key=True, index=True)

    is_number = Column(String(100), unique=True, index=True)

    title = Column(String(500))

    category = Column(String(200))

    description = Column(Text)

    status = Column(String(100))

    year = Column(String(20))

    official_url = Column(String(500))


class Laboratory(Base):
    __tablename__ = "laboratories"

    id = Column(Integer, primary_key=True, index=True)

    lab_code = Column(String(100), unique=True, index=True)

    name = Column(String(500))

    location = Column(String(500))

    testing_scope = Column(Text)

    supported_standards = Column(Text)

    official_url = Column(String(500))