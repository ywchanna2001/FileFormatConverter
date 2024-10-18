# File Format Transformer

This project aims to automate the process of standardizing column names in Excel files and converting the data into a JSON format. It uses the GPT-2 model for text generation (optional) and the SpellChecker library to correct spelling errors in column names. The processed data is saved as a JSON file for further use. This project is especially useful for preprocessing Excel data for machine learning models or data analytics.

## Features
- Standardizes column names in Excel files (corrects spelling, removes special characters, capitalizes words, replaces spaces with underscores).
- Converts the cleaned data to a JSON file format.
- Easy-to-use and customizable for various data cleaning tasks.

## Requirements
- Python 3.8 or later
- `transformers` (for GPT-2 text generation)
- `spellchecker` (for spell correction)
- `pandas` (for data handling)
- `openpyxl` (for reading Excel files)

## Getting Started

### Prerequisites

Before cloning the project, ensure you have Git installed on your machine. You can download it from [Git's official website](https://git-scm.com/).

### Clone the Repository

To clone this repository, run the following command in your terminal or command prompt:

```bash
git clone https://github.com/ywchanna2001/FileFormatConverter.git
```

### Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies for this project. To create a virtual environment, follow these steps:

1. Navigate to the project directory:
   
   ```bash
   cd FileFormatTransformer
   ```
2. Create a virtual environment:

   ```bash
   python -m venv env
   ```

3. Activate the virtual environment:

   on Windows:

   ```bash
   .\env\Scripts\activate
   ```

   on macOS and Linux:

   ```bash
   source env/bin/activate
   ```


### Install Required Packages

With the virtual environment activated, install the required packages using the requirements.txt file:

```bash
pip install -r requirements.txt
```

This will install all the necessary libraries, including transformers, spellchecker, pandas, and openpyxl.


### Prepare Your Data

1.Place the Excel file you want to process in the FileFormatTransformer directory.
2.Update the file_path variable in main.py to match the name of your Excel file (e.g., sample_correct_format.xlsx).


## Running the Project

To run the program and convert the Excel file into a JSON file, use the following command in the terminal:

```bash
python main.py
```

## Output

1.The program will load the specified Excel file, standardize the column names, and save the resulting data in JSON format.
2.The output JSON file will be saved in the same directory with the name specified in main.py (e.g., test_result.json).

You should see a message like this upon successful execution:

#### "JSON data has been saved to test_result.json"

## Example

If you want to process a file named sample_correct_format.xlsx, ensure that the file_path variable in main.py is set as follows:

```bash
file_path = 'sample_correct_format.xlsx'
```

Then, run the script:

```bash
python main.py
```

The standardized data will be saved in test_result.json.


## Troubleshooting


### Common Warnings

When running the project, you may encounter the following warnings:

#### oneDNN Custom Operations Warning:

```bash
oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
```

This is a TensorFlow warning that can generally be ignored. It relates to the use of oneDNN operations that optimize performance.

#### FutureWarning about torch:

```bash
FutureWarning: `torch.utils._pytree._register_pytree_node` is deprecated. Please use `torch.utils._pytree.register_pytree_node` instead.
```

This is a warning about upcoming changes in the torch library. The current implementation should work without issues, but be aware of this for future versions of the library.

## Contributing

Contributions are welcome! If you have any suggestions or find any issues, feel free to create a pull request or open an issue in this repository.
