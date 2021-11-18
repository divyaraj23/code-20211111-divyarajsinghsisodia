import pytest
from src import bmi_calculator
import numpy as np
import pandas as pd

"""Test data"""
input_d_nan = {'Gender': ['Male','Male','Male','Female','Female','Female'], 
                'HeightCm': [171, str(np.NaN), 180, 166, 150, 167],
                'WeightKg': [95, 85, 77, 62, 70, 82]}
input_df_nan = pd.DataFrame(input_d_nan)
    


output_d_nan = {'Gender': ['Male','Male','Female','Female','Female'], 
                'HeightCm': [171, 180, 166, 150, 167],
                'WeightKg': [95, 77, 62, 70, 82]}
output_df_nan = pd.DataFrame(output_d_nan)


input_d_zero = {'Gender': ['Male','Male','Male','Female','Female','Female'], 
                'HeightCm': [171, 181, 180, 166, 150, 167],
                'WeightKg': [95, 85, 77, 0, 70, 82]}
input_df_zero = pd.DataFrame(input_d_zero)


output_d_zero = {'Gender': ['Male','Male','Male','Female','Female'], 
                'HeightCm': [171, 181, 180, 150, 167],
                'WeightKg': [95, 85, 77, 70, 82]}
output_df_zero = pd.DataFrame(output_d_zero)

input_cat_risk = {'Gender': ['Male','Male','Male','Female'], 
                'HeightCm': [171, 161, 180, 166],
                'WeightKg': [95, 85, 77, 62]}
input_df_cat_risk = pd.DataFrame(input_cat_risk)

output_cat_risk = {'Gender': ['Male','Male','Male','Female'], 
                'HeightCm': [171, 161, 180, 166],
                'WeightKg': [95, 85, 77, 62],
                'BMIValue': [32.5, 32.8, 23.8, 22.5],
                'BMICategory': ['Moderately obese', 'Moderately obese', 'Normal weight', 'Normal weight'],
                'BMIRisk':['Medium risk','Medium risk','Low risk','Low risk']}
output_df_cat_risk = pd.DataFrame(output_cat_risk)

"""Test cases"""
# To test BMI value calculation
def test_calculate_bmi():
    bmivalue = bmi_calculator.calculate_bmi(60,140)
    assert bmivalue == 30.6

# To test assignment of correct category and risk as per BMI value supplied
def test_assign_category_risk():
    category,risk_value = bmi_calculator.assign_category_risk(30)
    assert (category == 'Moderately obese' and  risk_value == 'Medium risk')

# To test removal of rows containing NaN values
def test_clean_bmi_dataframe_nan():
    op_df = bmi_calculator.clean_bmi_dataframe(input_df_nan)
    expected_df = output_df_nan
    diff = pd.concat([op_df,expected_df]).drop_duplicates(keep=False)
    assert diff.shape[0] == 0

# To test removal of rows containing zeros
def test_clean_bmi_dataframe_zero():
    op_df = bmi_calculator.clean_bmi_dataframe(input_df_zero)
    expected_df = output_df_zero
    diff = pd.concat([op_df,expected_df]).drop_duplicates(keep=False)
    assert diff.shape[0] == 0

# To test correct assignment of risk and category to each row supplied
def test_bmi_category_risk():
    op_df = bmi_calculator.add_bmi_category_risk(input_df_cat_risk)
    expected_df = output_df_cat_risk
    diff = pd.concat([op_df,expected_df]).drop_duplicates(keep=False)
    assert diff.shape[0] == 0