FROM python:3

# Set the working directory in DOCKER CONTAINER
WORKDIR /code/app

# copy the LOCAL DIRECTORY to DOCKER CONTAINER WORKING DIRECTORY
COPY . /code/app/

# install python packages
RUN pip install --no-cache-dir -r requirements.txt

# set up port
EXPOSE 8081

# setup volume
VOLUME [ "/data" ]

# Run app
CMD [ "python", "app.py"]