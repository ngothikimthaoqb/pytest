import json
import os

from jsonschema import validate
from jsonschema.exceptions import ValidationError

def load_json_data(file_path):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, file_path), "r") as f:
        return json.load(f)
   

def verify_json_schema(response_data, expected_schema):
    try:
        validate(instance=response_data, schema=expected_schema)
        print("JSON Schema validation passed.")
    except ValidationError as ve:
        print("JSON Schema validation failed.")
        raise AssertionError(f"JSON Schema Validation Error: {ve.message}")