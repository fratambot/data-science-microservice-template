# Data science microservice template
This is my go-to template for developing and pushing to production my data science microservices.

## Production
In production the API for inference is dockerized.

### Prerequisites
Install [Docker](https://docs.docker.com/engine/install/)

### Installation
Build the image and start the container with:
```
make start
```

### Usage
The API run on [http://localhost:8883/](http://localhost:8883/).

You can interact with it from your browser using the FastAPI UI on [http://localhost:8883/docs](http://localhost:8883/docs)

## Development
Development happens locally or in the cloud via scripts.

### Installation
It depends on which machine you're developing but in general you want to create a virtual environment with python 3.9 and run `pip install -r requirements_dev.txt`

### Usage
I like to keep the development steps separated because I iterate differently on each one of them.
#### Data preparation

#### Tuning

#### Train
