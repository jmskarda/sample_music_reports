import pandas as pd
from pathlib import Path


SOURCE_FILE = r"basicnames.csv"
SOURCE_FOLDER = Path(__file__).parent.as_uri()


# Generate the output filename
filename_base = Path(SOURCE_FILE).stem
output_filename = ".".join([filename_base,"json"])

# Load the CSV file
# source_path = Path.joinpath([SOURCE_FOLDER, SOURCE_FILE])
df = pd.read_csv("/".join([SOURCE_FOLDER, SOURCE_FILE]))
# df = pd.read_csv(source_path)

# Write each record as JSON to a text file
with open(output_filename, "w",) as outfile:
    for index, row in df.iterrows():
        outfile.write(row.to_json() + "\n")
