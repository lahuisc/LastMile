import pandas as pd

# Function to read a CSV file
def read_csv_file(file_path):
    try:
        # Read the CSV file into a DataFrame
        data = pd.read_csv(file_path)
        # Display the first few rows of the DataFrame
        print(data.head())
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Replace 'your_file.csv' with the path to your CSV file
    csv_file_path = 'Weather.csv'
    read_csv_file(csv_file_path)