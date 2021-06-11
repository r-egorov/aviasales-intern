import csv
from flight_class import Flight
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.engine.reflection import Inspector


#engine = create_engine("sqlite:///./database.db", echo=True)
engine = create_engine("postgresql://user:pass@192.168.99.105:5432/user", echo=True)

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


if __name__ == "__main__":
    flight = session.query(Flight).filter_by(id=4).first()
    print(flight)