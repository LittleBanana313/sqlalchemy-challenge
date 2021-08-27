# sqlalchemy-challenge
Little victories and hurdles in SQLAlchemy Homework - Surfs Up!
![Alt text](images/surfs-up.png?raw=true "Title")

**Step 1 - Climate Analysis and Exploration**
To begin, use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.


1) Use the provided starter notebook and hawaii.sqlite files to complete your climate analysis and data exploration.


2) Use SQLAlchemy create_engine to connect to your sqlite database.


3) Use SQLAlchemy automap_base() to reflect your tables into classes and save a reference to those classes called Station and Measurement.


4) Link Python to the database by creating an SQLAlchemy session.


Important Don't forget to close out your session at the end of your notebook!



**Precipitation Analysis**


1) Start by finding the most recent date in the data set.


2) Using this date, retrieve the last 12 months of precipitation data by querying the 12 preceding months of data. Note you do not pass in the date as a variable to your query.


3) Select only the date and prcp values.


4) Load the query results into a Pandas DataFrame and set the index to the date column.


5) Sort the DataFrame values by date.


6) Plot the results using the DataFrame plot method.
![Alt text](/images/precip.png?raw=true "Title")

**Station Analysis**


1) Design a query to calculate the total number of stations in the dataset.


2) Design a query to find the most active stations (i.e. which stations have the most rows?).


3) List the stations and observation counts in descending order.


4) Which station id has the highest number of observations?


5) Using the most active station id, calculate the lowest, highest, and average temperature.


Hint: You will need to use a function such as func.min, func.max, func.avg, and func.count in your queries.




6) Design a query to retrieve the last 12 months of temperature observation data (TOBS).


7) Filter by the station with the highest number of observations.


8) Query the last 12 months of temperature observation data for this station.


9) Plot the results as a histogram with bins=12.
![Alt text](images/temp.png?raw=true "Title")
