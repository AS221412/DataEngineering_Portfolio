FROM python:3.8

# defining the directory for the container
WORKDIR /app

# copies all files from the directory pyapp into /app
COPY . .

# installs required Python packages pandas and pymongo
RUN pip install --no-cache-dir pandas pymongo

# sets the default command to run when the container starts
CMD [ "python", "main.py" ]
