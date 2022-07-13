# Data science microservice template
This is my go-to template for developing my data science projects and pushing them to production as microservices.

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
The API runs on [http://localhost:8883/](http://localhost).

You can interact with it from your browser using the FastAPI UI on [http://localhost/docs](http://localhost/docs)

![alt text](https://github.com/fratambot/static/blob/main/images/FastAPI_UI.png?raw=True)

## Development
Development happens locally/on-premise or in the cloud via scripts in the `\app` folder.

### Installation
It depends on which machine you're developing but in general you want to create a virtual environment with the appropriate python version and run `pip install -r requirements_dev.txt`

### Usage
I like to keep the development steps separated because I don't necessarily iterate the same on all of them, all the time.

If you need a single end-to-end pipeline you can always make a script in which you import the `main` function of each step and pass the output of one step as input for the next step.

#### 🚧 Data preparation
You can play with the `args` depending on where's your raw data is and on where the data ready for training will be (e.g. by passing filepaths, AWS S3 ARNs, etc.).
```
python app/prepare.py -h
```

#### 🎛 Tuning
If you use an MLOps platform (AWS Sagemaker, Valohai, etc.), they usually have their own way of letting you perform hyperparameters tuning and you have to write a specific code with their sdk.

Otherwise, for local tuning, you will run this script for tuning your neural network or scikit-learn estimator.
```
python app/tune.py -h
```

#### 🤖 Train
This script is useful if you just want to train/retrain an existing model on new data
```
python app/train.py -h
```

#### 🌐 API
To test the inference API during development you can move in the `\app` folder and type:
```
uvicorn --reload main:app
```
The interactive API UI run on [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Disclaimer on Notebooks
I love Jupyter notebooks and I use them a lot for exploration, experimentation and reporting but I prefer performing defined task with python scripts rather than using a state machine.
