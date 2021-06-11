import csv
import os
from flight_class import Flight
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.engine.reflection import Inspector


PG_USER = os.getenv("POSTGRES_USER")
if not PG_USER:
    PG_USER = "user"
PG_PASS = os.getenv("POSTGRES_PASSWORD")
if not PG_PASS:
    PG_PASS = "pass"
PG_DB = os.getenv("POSTGRES_DB")
if not PG_DB:
    PG_DB = "user"
PG_HOST = os.getenv("POSTGRES_HOST")
if not PG_HOST:
    PG_HOST = "postgres"
NETWORK = os.getenv("NETWORK")
if not NETWORK:
    NETWORK = "aviasales_app-network"

db_url = f"postgresql://{PG_USER}:{PG_PASS}@{PG_HOST}.{NETWORK}:5432/{PG_DB}"
engine = create_engine(db_url, echo=True) #FIXME

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


def get_flight(flight_id):
    return session.query(Flight).filter_by(id=flight_id).first()


def import_csv(csv_path: str):
    with open(csv_path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        for row in reader:
            flight = Flight(id=row[0],
                            origin=row[1],
                            destination=row[2],
                            departure_date=row[3],
                            departure_time=row[4],
                            arrival_date=row[5],
                            arrival_time=row[6],
                            number=row[7])
            session.add(flight)
        session.commit()


inspector = Inspector.from_engine(engine)

if "flights" not in inspector.get_table_names():
    Flight.metadata.create_all(engine, checkfirst=True)
    import_csv("flights.csv")
