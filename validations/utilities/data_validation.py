"""
Script Name: data_validation.py
DataValidation Class
Description: This module defines the DataValidation class,
            which provides utilities to perform different validation(duplicate).
Author: B S
Date : 16.12.2023
"""
import pandas as pd


# A class has been established to facilitate future enhancements in the data validation section. 
# Duplicate checks can be executed without the need for introducing a class.
class DataValidation:
    def __init__(self, df):
        self.df = df

    def check_df(self):
        # Check if the DataFrame is defined and not None
        if self.df is None or self.df.empty:
            raise ValueError("DataFrame is None or empty. Cannot perform operation.")

    def check_columns(self, input_columns, actual_columns):
        # Check if the list of columns in input matches with the actual columns
        validate_columns = set(input_columns) - set(actual_columns)
        if validate_columns:
            raise ValueError(f"columns: {', '.join(validate_columns)} are not available")

    def check_duplicates(self, input_columns, mark_duplicates='first'):
        """
        checks for duplicates in a dataset for list of input columns

        input:
        df : input dataframe
        columns : list of columns on which duplicate check take places
        mark_duplicates : Mark duplicates as True for all or except  first or except last occurrence
                            By default, I assume the first occurrence is unique
                            to keep latest occurrence and mark rest as duplicates

        Return:
        result: dictionary {'count': sum of duplicates, 'samples': duplicate Dataframe}
        """
        try:
            # Check if the DataFrame is defined
            self.check_df()

            # Check if the list of input columns matches with the defined dataframe columns
            self.check_columns(input_columns, self.df.columns)

            # identify duplicates based on list of columns
            duplicate = self.df.duplicated(subset=input_columns, keep=mark_duplicates)
            # number of cases where duplicates occur.
            dup_count = duplicate.sum()

            # Verify duplicate count and generate dataframe with group count of duplicate rows for the input columns.
            if dup_count > 0:
                samples = self.df[duplicate].groupby(input_columns).size().reset_index(
                    name='number_of_duplicates')
            # no duplicate generate below message. This session is for improve readable
            else:
                samples = f"combinations of columns: {', '.join(input_columns)} have no duplicates"

            # create dictionary with duplicate count and samples
            result = {'count': dup_count, 'samples': samples}
            # create dictionary
            return result

        except Exception as e:
            return {'error': str(e)}
