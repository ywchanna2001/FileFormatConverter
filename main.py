#!/usr/bin/env python
# coding: utf-8

# Import necessary libraries
from transformers import pipeline
from spellchecker import SpellChecker
import pandas as pd
import json
import re

# ## Loading the pretrained model
# Loading GPT-2 model using Hugging Face pipeline
model = pipeline('text-generation', model='gpt2')  # You can choose other models too

# Initialize the SpellChecker
spell = SpellChecker()

# Function to correct spelling using SpellChecker
def correct_spelling(column_name):
    """
    Correct spelling errors in the column name.
    """
    # Split the column name into words
    words = column_name.split()
    # Correct each word if it is not in the spellchecker's dictionary
    corrected_words = [
        spell.correction(word) if spell.correction(word) is not None else word for word in words
    ]
    # Join the corrected words back into a single string
    corrected = ' '.join(corrected_words)
    return corrected

# Function to standardize column names: Capitalize each word and replace spaces with underscores
def standardize_column_name(column_name):
    """
    Standardize column names by correcting spelling, removing special characters, 
    and replacing spaces with underscores.
    """
    # Correct spelling first
    corrected_name = correct_spelling(column_name)
    
    # Remove any special characters and normalize spacing
    cleaned_name = re.sub(r'[^a-zA-Z0-9\s]', '', corrected_name)
    
    # Split by space and capitalize each word, then join with an underscore
    standard_name = '_'.join([word.capitalize() for word in cleaned_name.split()])
    
    return standard_name

# Function to load an Excel file and standardize column names
def load_and_standardize_excel(file_path, sheet_name=0):
    """
    Load an Excel file, transpose it to make the first column the header,
    and standardize the column names.
    """
    # Load the Excel file
    df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)

    # Transpose the DataFrame so that the first column becomes headers
    df = df.set_index(0).transpose()

    # Get the column names (after transposing)
    original_columns = df.columns

    # Standardize each column name
    standardized_columns = [standardize_column_name(col) for col in original_columns]

    # Create a mapping of original to standardized column names
    column_mapping = dict(zip(original_columns, standardized_columns))

    # Update the DataFrame's columns with the standardized names
    df = df.rename(columns=column_mapping)

    return df

# Function to convert the DataFrame to a JSON file
def save_dataframe_to_json(df, output_file):
    """
    Save the standardized DataFrame to a JSON file.
    """
    # Convert the DataFrame to a list of dictionaries (JSON objects)
    json_data = df.to_dict(orient='records')

    # Save the JSON data to a file
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)

# Main function
if __name__ == "__main__":
    # Specify the file paths
    file_path = 'sample_correct_format.xlsx'  # Path to the input Excel file
    output_file = 'test_result.json'          # Path to the output JSON file

    # Load and standardize the Excel data
    df = load_and_standardize_excel(file_path)

    # Save the standardized data as JSON
    save_dataframe_to_json(df, output_file)

    print(f"JSON data has been saved to {output_file}")
 