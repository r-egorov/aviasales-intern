from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Flight(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True)
    origin = Column(String)
    destination = Column(String)
    departure_date = Column(String)
    departure_time = Column(String)
    arrival_date = Column(String)
    arrival_time = Column(String)
    number = Column(String)

    def __repr__(self):
        return "<Flight(id={}, number=\"{}\")>".format(self.id, self.number)
