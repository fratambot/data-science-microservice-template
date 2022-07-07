# This script contains the pipeline for building, tuning and evaluate the model

import argparse

# local imports
from src.model import some_tuner, some_pipe
from src.utils.dev_utils import model_performance_plot


def main():
    print(
        "some_arg_for_tuning_like_max_epochs = ",
        some_arg_for_tuning_like_max_epochs,
    )
    print("data_tag = ", data_tag)
    # load training data from /data folder or cloud using data_tag
    # get your tuner..
    some_tuner()
    # ..or pipe to tune
    some_pipe()
    print("=== Tuning === ")
    # define search space / param_grid
    # perform your favourite search of parameters specific to your model
    # obtain :
    best_model = None
    print("=== Evaluation === ")
    # evaluate the model on the validaiton set
    # produce some plots for reporting
    history_or_confusion_matrix = None
    model_performance_plot(history_or_confusion_matrix)
    # save best model in local /data folder and/or in the cloud

    return best_model


if __name__ == "__main__":
    # Parse args
    docstring = """Script for data tuning and evaluation"""
    parser = argparse.ArgumentParser(
        description=docstring,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--some_arg_for_tuning_like_max_epochs",
        default=5,
        type=int,
        help="example of numerical arg like max_epochs",
    )
    parser.add_argument(
        "--data_tag",
        required=True,
        type=str,
        help="a string used to retrieve training data",
    )

    args = parser.parse_args()
    some_arg_for_tuning_like_max_epochs = (
        args.some_arg_for_tuning_like_max_epochs
    )
    data_tag = args.data_tag

    main()
    print("=== Finished ===")
