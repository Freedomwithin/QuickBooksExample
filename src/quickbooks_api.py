import json

def get_quickbooks_data(query):
    """Retrieves data from QuickBooks Online (MOCK version)."""
    mock_data_file = "data/sample_customer_data.json"
    try:
        with open(mock_data_file, 'r') as f:
            mock_data = json.load(f)
        return mock_data
    except FileNotFoundError:
        print(f"Error: Mock data file '{mock_data_file}' not found. Create the file in the data/ folder. ")
        return None
    except json.JSONDecodeError:  # Handle JSON parsing errors
        print(f"Error: Invalid JSON format in '{mock_data_file}'.")
        return None