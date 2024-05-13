# About
This project is Task 1 of the Data Engineering Course at IU. It demonstrates storing collected sensor data in a database and making it usable for other developers (e.g., frontend).

# Requirements
Before starting the application, make sure to install Docker Desktop.


# starting application
1. open a terminal and navigate to the directory.
2. run the command 'docker-compose-up', to run the application
3. the application will start in 2 containers:
- one for the python script
- and the other for the mongoDB server

The container with the python script is responsible for connecting to the port which is hosted
by the container with the mongoDB server. The python script will create a databse and read the data from 'iot_telemetry_data.csv. afterwards it will store the data in batches into the created database.


# Datastructure
pyapp/: this directory contains the python script, Dockerfile and the sensor data.
main.py: this is the main script which creates the database and reads the sensor data.
iot_telemetry_data.csv: this is the file with the sensor data.
Dockerfile: this is the dockerfile for the python application
docker-compose.yml: this is the docker compopse file, which makes the connection between 2 containers possible



