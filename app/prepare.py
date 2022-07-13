# This script contains the pipeline to transform raw data into training data

import argparse

# local imports
from src.utils.dev_utils import load_raw_data


def main():
    print(
        "some_arg_for_data_prep_like_limit = ",
        some_arg_for_data_prep_like_limit,
    )

    load_raw_data(None)
    # split data for train / val / test
    # transform (vectorize, one-hot-encode, etc.)
    # and obtain:
    data_for_training = None
    # save in local /data folder and/or in the cloud
    return data_for_training


if __name__ == "__main__":
    # Parse args
    docstring = """Script for data preparation"""
    parser = argparse.ArgumentParser(
        description=docstring,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "--some_arg_for_data_prep_like_limit",
        default=0,
        type=int,
        help="example of numerical arg",
    )

    args = parser.parse_args()
    some_arg_for_data_prep_like_limit = args.some_arg_for_data_prep_like_limit
    print("=== Data Preparation === ")
    main()
    print("=== Finished ===")
