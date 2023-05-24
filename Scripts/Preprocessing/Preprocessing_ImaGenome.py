import pandas as pd
import json
import glob
import re
import os

def process_json_files(folder_path):
    # Get a list of all JSON files in the specified folder
    json_files = glob.glob(folder_path + '/*.json')

    # Concatenate all dataframes into a single dataframe
    df_long = pd.concat(
        [pd.json_normalize(json.load(open(file, 'r'))['attributes']).assign(
            image_id=lambda x: json.load(open(file, 'r'))['image_id'],
            patient_id=lambda x: json.load(open(file, 'r'))['patient_id'],
            study_id=lambda x: json.load(open(file, 'r'))['study_id'],
            gender=lambda x: json.load(open(file, 'r'))['gender'],
            age_decile=lambda x: json.load(open(file, 'r'))['age_decile'],
            reason_for_exam=lambda x: json.load(open(file, 'r'))['reason_for_exam'],
            StudyDateTime=lambda x: json.load(open(file, 'r'))['StudyDateTime']
        ) for file in json_files],
        ignore_index=True
    )

    def get_attribute_category(attributes):
        # create a list of attributes containing "anatomicalfinding"
        af_attributes = [attr for attr in attributes.split(",") if "anatomicalfinding" in attr]

        # check if there are any "yes" in the anatomicalfinding attributes
        yes_attributes = [attr.split("|")[2] for attr in af_attributes if attr.split("|")[1] == "yes"]

        # if there are no "yes" attributes, return "normal"
        if len(yes_attributes) == 0:
            return "normal"
        else:
            # if there is one "yes" attribute, return its value
            if len(yes_attributes) == 1:
                return yes_attributes[0]
            # if there are multiple "yes" attributes, concatenate them with commas
            else:
                return ", ".join(yes_attributes)

    # apply the function to the "attributes" column and create a new column called "attribute_category"
    df_long["attribute_category"] = df_long["attributes"].apply(get_attribute_category)

    # remove ' from the column
    df_long["attribute_category"] = df_long["attribute_category"].str.replace("'", "")

    # Remove duplicates in attribute_category column
    df_long["attribute_category"] = df_long["attribute_category"].apply(lambda x: ", ".join(set(x.split(", "))))

    def get_disease_category(attributes):
        # create a list of attributes containing "disease"
        d_attributes = [attr for attr in attributes.split(",") if "disease" in attr]

        # check if there are any "yes" in the disease attributes
        yes_attributes = [attr.split("|")[2] for attr in d_attributes if attr.split("|")[1] == "yes"]

        # if there are no "yes" attributes, return "no disease"
        if len(yes_attributes) == 0:
            return "no disease"
        else:
            # if there is one "yes" attribute, return its value
            if len(yes_attributes) == 1:
                return yes_attributes[0]
            # if there are multiple "yes" attributes, concatenate them with commas
            else:
                return ", ".join(yes_attributes)

    # apply the function to the "attributes" column and create a new column called "disease_category"
    df_long["disease_category"] = df_long["attributes"].apply(get_disease_category)

    # remove ' from the column
    df_long["disease_category"] = df_long["disease_category"].str.replace("'", "")

    # Remove duplicates in disease_category column
    df_long["disease_category"] = df_long["disease_category"].apply(lambda x: ", ".join(set(x.split(", "))))

    # define the text patterns to remove
    patterns = ["___F", "___M", "F", "M", "Male", "Man", "male", "man",
                "Female", "female", "woman", "Woman", "___ year old man",
                "___ year old", "___ year old woman", "___-year-old female",
                "___-year-old male", "___-year-old female", "___-year-old",
                "___", "A ___-year-old", "year old", "-year-old", "years old"]

    # create a regular expression pattern to match the text patterns
    pattern = re.compile("|".join(patterns))

    # define function to remove patterns
    def remove_patterns(text):
        if type(text) == str:
            return pattern.sub("", text)
        else:
            return ""

    # fill null values with empty strings
    df_long["reason_for_exam"] = df_long["reason_for_exam"].fillna("")

    # apply the function to the reason_for_exam column and save the result to a new column called reason_clean
    df_long["reason_clean"] = df_long["reason_for_exam"].apply(remove_patterns)

    return df_long


def save_df_to_csv(dataframe, output_folder):
    # Save the dataframe as a CSV file in the specified output folder
    dataframe.to_csv(os.path.join(output_folder, "Scene_Graph_Disease_Only.csv"), index=False)


def create_dataframes(input_folder, output_folder):
    # Process JSON files and create the dataframe
    df = process_json_files(input_folder)

    # Save the dataframe as a CSV file
    save_df_to_csv(df, output_folder)

    # Create lung_attribute_mapping.csv
    df_attr_lungr = df[["image_id", "patient_id", "study_id", "gender", "age_decile", "StudyDateTime", "attribute_category", "disease_category", "reason_clean"]].drop_duplicates()
    df_attr_lungr["disease_category"] = df_attr_lungr["disease_category"].str.lower()
    df_attr_lungr["attribute_category"] = df_attr_lungr["attribute_category"].str.lower()
    df_attr_lungr = df_attr_lungr.dropna(subset=['disease_category'])
    df_attr_lungr = df_attr_lungr[df_attr_lungr['disease_category'].str.contains("copd/emphysema|fluid overload/heart failure")]
    df_attr_lungr = df_attr_lungr.sort_values(by=["patient_id", "StudyDateTime"])
    df_attr_lungr["visits"] = df_attr_lungr.groupby("patient_id").cumcount() + 1
    df_attr_lungr.to_csv(os.path.join(output_folder, "lung_attribute_mapping.csv"), index=False)

    # Create hf_copd_df_topic_model.csv
    hf_copd_df = df[["disease_category", "reason_clean", "patient_id", "study_id", "gender", "age_decile", "StudyDateTime"]].drop_duplicates()
    hf_copd_df["disease_category"] = hf_copd_df["disease_category"].str.lower()
    hf_copd_df = hf_copd_df[hf_copd_df['disease_category'].str.contains("copd/emphysema|fluid overload/heart failure")]
    hf_copd_df = hf_copd_df.sort_values(by=["patient_id", "StudyDateTime"])
    hf_copd_df.to_csv(os.path.join(output_folder, "hf_copd_df_topic_model.csv"), index=False)


# Example usage
input_folder = "../CXR_Dataset/scene_graph"
output_folder = "../Data"

create_dataframes(input_folder, output_folder)