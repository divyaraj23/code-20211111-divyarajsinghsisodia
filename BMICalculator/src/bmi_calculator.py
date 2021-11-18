import pandas as pd


'''
This script takes in weight and dimensional data in the form of a json payload 
and determines the BMI Category and the health risk for each person.
We will be using the dataframes in Pandas to achieve the aforementioned function.
Sequence of code is as follows:
1. Parse the input json and put the data (which is complete and kick out any data that is incomplete) into a dataframe.
2. Populate the three new columns of BMI value, BMI Category and Health risk for each data row in the dataframe.
3. Leverage the data in the dataframe to infer on the overweight persons for their calculated BMI in the dataframe.

'''

json_file_loc = "BMICalculator/data/weightheight.json"




def calculate_bmi(mass, height):
    try:
        return round(mass/(height/100)**2,1)
    except:
        raise Exception("Error while calculating BMI Value mass = "+str(mass)+ " height = "+str(height))

def load_json_to_df(jsonfile):
    try:
        df = pd.read_json(jsonfile)
        return df
    except:
        raise Exception("Issue while loading json into dataframe")

def assign_category_risk(bmi_value):
    bmi_category = ""
    health_risk = ""
    if bmi_value<=18.4:
        bmi_category = "Underweight"
        health_risk = "Malnutrition risk"
    elif bmi_value>=18.5 and bmi_value<=24.9:
        bmi_category = "Normal weight"
        health_risk = "Low risk"
    elif bmi_value>=25 and bmi_value<=29.9:
        bmi_category = "Overweight"
        health_risk = "Enhanced risk"
    elif bmi_value>=30 and bmi_value<=34.9:
        bmi_category = "Moderately obese"
        health_risk = "Medium risk"
    elif bmi_value>=35 and bmi_value<=39.9:
        bmi_category = "Severely obese"
        health_risk = "High risk"
    else:
        bmi_category = "Very severely obese"
        health_risk = "Very high risk"
    return bmi_category,health_risk

def calculate_overweights(bmidataframe):
    return str(bmidataframe[bmidataframe['BMICategory'] == 'Overweight'].shape[0])

def add_bmi_category_risk(bmidataframe):
    bmi_value_op = bmidataframe.apply(
        lambda row: calculate_bmi(row['WeightKg'],row['HeightCm']), axis=1
    )
    bmidataframe['BMIValue'] = bmi_value_op
    bmidataframe[['BMICategory','BMIRisk']] = bmidataframe.apply(
        lambda row: assign_category_risk(row['BMIValue']), axis=1, result_type="expand"
    )
    return bmidataframe

def clean_bmi_dataframe(bmidataframe):
    print("Remove non-numeric values")
    bmidataframe = bmidataframe[bmidataframe['WeightKg'].apply(lambda row: str(row).isdigit())]
    bmidataframe = bmidataframe[bmidataframe['HeightCm'].apply(lambda row: str(row).isdigit())]
    print("Removing rows having null values...")
    bmidataframe = bmidataframe.dropna(how="any", axis=0)
    print("Enforcing range constraints on dataframe columns...")
    # This will remove any row with zero data values
    bmidataframe = bmidataframe.query('HeightCm > 0 and HeightCm < 300 and WeightKg > 0 and WeightKg < 700')
    if bmidataframe.shape[0] == 0:
        raise Exception("Issue with keys in the input json or empty json being loaded")
    return bmidataframe


if __name__ == "__main__":
    # Load the json data to dataframe
    try:
        bmi_df = load_json_to_df(json_file_loc)
    except Exception as e:
        print("Issue encountered : "+str(e))
        exit()

    # Clean the loaded dataframe of any invalid values
    try:
        cleaned_bmi_df = clean_bmi_dataframe(bmi_df)
    except Exception as e:
        print("Issue during cleaning stage : "+str(e))
        exit()

    
    # Calculate and add BMI value and add BMI Category and health risk based on BMI value
    try:
        enriched_bmi_df = add_bmi_category_risk(cleaned_bmi_df)
    except:
        print("Issue while calculating category and risk for each person")
        exit()
    print(enriched_bmi_df)
    overweight_count = calculate_overweights(enriched_bmi_df)
    print("Number of Overweight persons : "+overweight_count)
    



