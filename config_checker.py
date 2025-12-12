import json
import argparse
from jsonschema import validate

#Define function to load config file
#Note: Output is a Dictionary
def load_config(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        return json.load(file)

def main():
    parser = argparse.ArgumentParser(description="Check configuration file for required fields.")
    parser.add_argument("filename", help="Path to the configuration file")
    parser.add_argument("schema", help="Path to the JSON schema file")

    args = parser.parse_args()

    filename = args.filename
    schema_name = args.schema

    config_data = load_config(filename)
    schema = load_config(schema_name)

    validate(instance=config_data, schema=schema)
    print("Configuration file is valid according to the schema.")

if __name__ == "__main__":
    main()
