"""
Script Name: main_script.py
Description: script uses the DataValidation utility to check for duplicates in specified columns.
Author: B S
Date : 16.12.2023

"""
import pandas as pd
from utilities.data_validation import DataValidation


def main():
    try :
        # Test the class with the provided dataset
        df_1 = pd.DataFrame(
            data=[
                ['A', 'a', 'x', 1],
                ['A', 'b', 'x', 1],
                ['A', 'c', 'x', 1],
                ['B', 'a', 'x', 1],
                ['B', 'b', 'x', 1],
                ['B', 'c', 'x', 1],
                ['A', 'a', 'y', 1],
            ],
            columns=['col_1', 'col_2', 'col_3', 'col_4']
        )
        # Initialize DataValidation with the dataframe
        duplicate_checker = DataValidation(df_1)
        # Test duplicates for different combination of columns
        columns_list = [['col_1'], ['col_1', 'col_2'], ['col_1', 'col_2', 'col_3']]

        # loop to print duplicates for each combination of columns
        for col in columns_list:
            result = duplicate_checker.check_duplicates(col)
            print(result)
            # better visibility
            print("-" * 50)

    except Exception as e:
        print({'error': str(e)})


if __name__ == "__main__":
    main()
