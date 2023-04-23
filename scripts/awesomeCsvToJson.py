import csv
import json
import uuid
import pandas as pd
import sys

def csv_to_json(input_file):
    data = pd.read_csv(input_file)

    output_data = {
        "version": 4,
        "history": [],
        "folders": [],
        "prompts": []
    }

    for index, row in data.iterrows():
        prompt = {
            "id": str(uuid.uuid4()),
            "name": row[0],
            "description": row[0],
            "content": row[1],
            "model": {
                "id": "gpt-3.5-turbo",
                "name": "GPT-3.5",
                "maxLength": 12000,
                "tokenLimit": 4000
            },
            "folderId": None
        }
        output_data["prompts"].append(prompt)

    with open(f"{input_file.split('.')[0]}.json", "w") as json_file:
        json.dump(output_data, json_file, indent=2)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file.csv>")
        sys.exit(1)

    input_file = sys.argv[1]
    csv_to_json(input_file)