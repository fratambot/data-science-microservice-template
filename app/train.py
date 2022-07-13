# This script contains the pipeline for train/retrain an existing model

import argparse


def main():
    print(
        "some_arg_for_training_like_epochs = ",
        some_arg_for_training_like_epochs,
    )
    print("data_tag = ", data_tag)
    # retrieve (new?) training data to train/retrain
    print("model_tag = ", model_tag)
    # retrieve the existing model to train/retrain
    print("=== Training === ")
    # train the model
    retrained_model = None
    # save trained model in local /data folder and/or in the cloud

    return retrained_model


if __name__ == "__main__":
    # Parse args
    docstring = """Script for model training"""
    parser = argparse.ArgumentParser(
        description=docstring,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--some_arg_for_training_like_epochs",
        default=10,
        type=int,
        help="example of numerical arg like epochs",
    )
    parser.add_argument(
        "--model_tag",
        required=True,
        type=str,
        help="a string used to retrieve the model to train",
    )
    parser.add_argument(
        "--data_tag",
        required=True,
        type=str,
        help="a string used to retrieve training data",
    )

    args = parser.parse_args()
    some_arg_for_training_like_epochs = args.some_arg_for_training_like_epochs
    model_tag = args.model_tag
    data_tag = args.data_tag
    main()
    print("=== Finished ===")
