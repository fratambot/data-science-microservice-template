# This script contains the pipeline for building, tuning and evaluate the model

import argparse

# local imports
from src.model import some_tuner, some_pipe
from src.utils.dev_utils import model_performance_plot


def main():
    print("higher_level_optional_arg = ", higher_level_optional_arg)
    print("prepare_data = ", prepare_data)
    print("data_tag = ", data_tag)
    print("prepare_data_arg = ", prepare_data_arg)
    if not prepare_data:
        if not data_tag:
            raise Exception(
                "you need to pass --data_tag to retrieve the existing data"
            )
        else:
            # retrieve the data with the data_tag
            print("loading data...")
    else:
        # prepare the data using prepare_data_arg, if passed
        print("preparing data...")

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

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--higher_level_optional_arg",
        default=5,
        type=int,
        help="some optional arg",
    )
    parser.add_argument(
        "--prepare_data",
        dest="prepare_data",
        default=False,
        action="store_true",
        help="wether you want to prepare data or not",
    )
    parser.add_argument(
        "--data_tag",
        # required=True,
        type=str,
        help="if prepare_data is false, this should be required \
        to retrieve existing data",
    )
    parser.add_argument(
        "--prepare_data_arg",
        default=10,
        type=int,
        help="if prepare_data is true you can pass this if you want",
    )

    args = parser.parse_args()
    higher_level_optional_arg = args.higher_level_optional_arg
    prepare_data = args.prepare_data
    data_tag = args.data_tag
    prepare_data_arg = args.prepare_data_arg

    main()
    print("=== Finished ===")
