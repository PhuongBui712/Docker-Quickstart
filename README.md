# Docker Quickstart

## **Introduction**

Welcome to our Docker Quickstart project! This project is designed to simplify the process of getting started with Docker, a popular containerization platform. Our goal is to provide a comprehensive guide for beginners to quickly set up and start using Docker for their projects. This document will walk you through the necessary steps to get started, including the required prerequisites, installation instructions, and additional learning resources to help you master Docker.

## **Table of Contents**

1. [Introduction](#introduction)
2. [Table of Contents](#table-of-contents)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [How to Learn](#how-to-learn)

## **Prerequisites**

Before you begin, make sure you have the following:

**1. Docker**

To get started with Docker, you can install the *Docker Engine*. However, we highly recommend installing *Docker Desktop* instead, as it provides a more comprehensive and user-friendly experience. Docker Desktop includes Docker Engine, along with other tools like Docker Compose, Docker Machine, and Kitematic, making it easier to manage your Docker environment and streamline your development workflow.

- [Docker Engine](https://docs.docker.com/engine/install/)
- [Docker Desktop](https://docs.docker.com/desktop/)

**2. Python**

The code in this repository is written in Python. Therefore, it is necessary to have Python installed on your system in order to run and understand the code.

**Option 1: Install Python only**

To install Python, follow the instructions for your operating system:

- [Python Installation for Windows](https://www.python.org/downloads/windows/)
- [Python Installation for macOS](https://www.python.org/downloads/mac-osx/)
- [Python Installation for Linux](https://www.python.org/downloads/source/)

**Option 2: Install Python with Anaconda**

- [Anaconda Installation](https://www.anaconda.com/products/distribution#download-section)

## **Installation**

**Clone this project**

```bash
git clone https://github.com/PhuongBui712/Docker-Quickstart.git
```

**Create Python virtual environment and activate it.**

Create Python virtual environment

```bash
cd Docker-Quickstart
python -m venv <ENVIRONMENT NAME>
```

Activating the Virtual Environment

- **For Windows:**
```bash
.\<ENVIRONMENT NAME>\Scripts\activate
```

- **For macOS/Linux:**
```bash
source <ENVIRONMENT NAME>/bin/activate
```


## **How to Learn**

**1. Running program locally**

To run the Flask app, execute the following command:

```bash
python app.py
```

**Important:** Make sure you are in the same directory as the `app.py` file before running the command.

To access the Flask app, open your web browser and navigate to `http://localhost:8081`.

If the browser show *Hello, World! This is an example Flask app!*, you successfully run it.

**2. Create your `Dockerfile`**

Learn how to containerize this application by Dockerfile. Here is an [example](https://docs.docker.com/guides/workshop/02_our_app/)

Then compare with my [`Dockerfile`](https://github.com/PhuongBui712/Docker-Quickstart/blob/main/Dockerfile).

**3. Build Docker Image**

To build the Docker image, execute the following command in the terminal from the project directory:
```bash
docker build -t <IMAGE NAME> .
```

After building the image, you can check if the image is successfully created by running:
```bash
docker images
```
This command lists all the Docker images on your system. You should see `<IMAGE_NAME>` in the list.

**4. Run Docker container**

To run the Docker container, execute the following command in the terminal from the project directory:
```bash
docker run -p <LOCAL PORT>:<CONTAINER EXPOSE PORT> -v $(pwd)/data:/data <IMAGE_NAME>
```
This command maps the container's port 8081 to the host's port 8081 and binds the current directory's `data` folder to the container's `/data` directory.

**5. Testing container app**

To access the Flask app running in the Docker container, open your web browser and navigate to `http://localhost:<LOCAL PORT>`.

- Write data to the Flask app using the following command:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"data": "I love Docker"}' http://localhost:8081/write
```
- Read the data from the Flask app using the following command:
```bash
curl http://localhost:8081/read
```
- If the Flask app is running correctly, the response should be:
```json
{'data': ['I love Docker\n']}
```

**6. Docker-compose**

Learning Docker compose at [here](https://docs.docker.com/compose/gettingstarted/)

Then containerize the app with `docker-compose` and test it like the above steps.