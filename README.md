# About
This project is Task 1 of the Data Engineering Course at IU. It demonstrates storing collected sensor data in a database and making it usable for other developers (e.g., frontend).

# Requirements
Before starting the application, make sure to install Docker Desktop.

# starting application
1. Open a terminal and navigate to the directory.
2. Run the command docker-compose up to start the application.

The application will start in two containers:
- One for the Python script.
- Another for the MongoDB server.

The container with the Python script is responsible for connecting to the port hosted by the container with the MongoDB server. The Python script will create a database and read data from 'iot_telemetry_data.csv'. Afterward, it will store the data in batches into the created database.

# Datastructure
pyapp/: this directory contains the python script, Dockerfile and the sensor data.
main.py: this is the main script which creates the database and reads the sensor data.
iot_telemetry_data.csv: this is the file with the sensor data.
Dockerfile: this is the dockerfile for the python application
docker-compose.yml: this is the docker compopse file, which makes the connection between 2 containers possible

