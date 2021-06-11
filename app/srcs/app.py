from flask import Flask, jsonify
import db

app = Flask(__name__)


@app.route("/flights/<int:flight_id>", methods=["GET"])
def get_flight(flight_id):
    flight = db.get_flight(flight_id)
    if flight:
        response = {
            "number": flight.number,
            "departure_time": flight.departure_time,
            "arrival_time": flight.arrival_time
        }
        status = 200
    else:
        response = {
            "error": "Flight not found"
        }
        status = 404
    return jsonify(response), status


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
