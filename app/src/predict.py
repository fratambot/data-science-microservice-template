from src.utils.prod_utils import some_data_transformation_for_inference


def predictor(model, input):
    some_data_transformation_for_inference(input)
    # model.predict() your input and obtain:
    prediction = "42"

    results = {
        "prediction": prediction,
    }

    return results
