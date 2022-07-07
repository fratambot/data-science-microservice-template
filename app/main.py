# This is the API for inference
# (usually with Basic Auth and sentry integration)

from fastapi import FastAPI

# local import
from src.predict import predictor

app = FastAPI()


@app.get("/status")
def status():
    return {"status": "Ok"}


loaded_model = None


@app.get("/predict")
def predict(
    input: str,
    model_tag: str,
):

    # load model
    global loaded_model

    if not loaded_model:
        # load the model using the model_tag
        loaded_model = None

    prediction = predictor(loaded_model, input)

    return prediction
