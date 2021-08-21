import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
meas = Base.classes.measurement
stat = Base.classes.station

# Flask Setup
app = Flask(__name__)

# Flask Routes

# Calculate the date one year from the last date in data set.
minus_year = dt.date(2017,8,23) - dt.timedelta(days=365)

# Create precipitation query and route
@app.route("/api/v1.0/precipitation")
def precipitation():
    sess = Session(engine)

    precip = sess.query(meas.date, meas.prcp).\
    filter(meas.date >= minus_year).\
    order_by(meas.date).all()

    sess.close()
    return jsonify([{date:value} for date, value in precip])

# Create station query and route
@app.route("/api/v1.0/stations")
def stations():
    sess = Session(engine)

    station = sess.query(stat.station, stat.name).all()
    sess.close()
    return jsonify([{ID:name} for ID, name in station])

# Create temp observation query and route
minus_year = dt.date(2017,8,23) - dt.timedelta(days=365)
@app.route("/api/v1.0/tobs")
def tobs():
    sess = Session(engine)

    temp_obs = sess.query(meas.tobs).\
    filter(meas.date >= minus_year).\
    filter(meas.station == "USC00519281").\
    order_by(meas.date).all()

    sess.close()
    return jsonify(temperatures = [item for t in temp_obs for item in t])

# Create start query and route
@app.route("/api/v1.0/<start>")
def start(start):
    sess = Session(engine)

    select = [func.min(meas.tobs), func.max(meas.tobs), func.avg(meas.tobs)]
    min_max = sess.query(*select).\
        filter(meas.date > start).all()
    sess.close()
    return jsonify(list(min_max[0]))

# Create start-end query and route
@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    sess = Session(engine)
    select = sess.query(meas.date, func.min(meas.tobs), func.avg(meas.tobs), func.max(meas.tobs)).\
    start_end = sess.query(*select).\
        filter(meas.date >= start).\
            group_by(meas.date).all()
    sess.close()
    return jsonify(list(start_end[0]))

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

# treat like an app
if __name__ == '__main__':
    app.run(debug=True)
