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
Development happens locally (meaning also on-premise if you have a cluster to which you can ssh) or in the cloud via scripts.

### Installation
It depends on which machine you're developing but in general you want to create a virtual environment with the appropriate python version and run `pip install -r requirements_dev.txt`

### Usage
I like to keep the development steps separated because I don't necessarily iterate the same on all of them, all the time.

If you need a single end-to-end pipeline you can always make a script in which you import the `main` function of each step and pass the output of one step as input for the next step.

#### 🧹 Data preparation
You can play with the `args` depending on where's your raw data is and on where the data ready for training will be (e.g. by passing filepaths, AWS S3 ARNs, etc.)

#### 🎛 Tuning
If you use an MLOps platform (AWS Sagemaker, Valohai, etc.), they usually have their own way of letting you perform hyperparameters tuning and you have to write a specific code with their sdk.

Otherwise, for local tuning, you will run this script for keras tuning your neural network or to tune the hyper-parameters of your scikit-learn estimator

#### 🤖 Train
This script is useful if you just want to train an existing tuned best model (if, for example, the data has changed or if you want to retrain the best model on the whole dataset)

## Disclaimer on Notebooks
I love Jupyter notebooks but I don't like the idea of using a state machine once the task is defined. I use notebooks a lot, locally, for exploration, experimentation and reporting. Once I have a final definition of one of the task, I trascribe the code in the appropriate part of the project and use the scripts instead.
