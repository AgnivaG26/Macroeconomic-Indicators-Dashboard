import pandas as pd
import os

def load_and_clean_data():
    """
    Loads, cleans, and combines all World Bank CSV files into a single DataFrame.
    Returns the combined DataFrame.
    """
    try:
        dataframes = {}
        files = {
            'GDP Growth (%)': 'gdp_growth.csv',
            'Exports (USD)': 'exports.csv',
            'Imports (USD)': 'imports.csv',
            'Agriculture (%)': 'agriculture.csv',
            'Industry (%)': 'industry.csv',
            'Services (%)': 'services.csv'
        }

        for key, filename in files.items():
            df = pd.read_csv(filename, skiprows=4)
            df = df.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code'])
            df = df.loc[:, ~df.columns.str.startswith('Unnamed')]
            df = df.set_index('Country Name').T
            # The key fix: Fill NaN values with the last valid observation
            df = df.ffill() 
            df.index = df.index.astype(int)
            dataframes[key] = df
        
        # Combine all data into a single, multi-level DataFrame
        combined_data = pd.concat(list(dataframes.values()), keys=list(dataframes.keys()), axis=1)
        combined_data = combined_data.astype(float)
        combined_data.index.name = 'Year'

        return combined_data

    except FileNotFoundError:
        print("Error: One or more data files not found. Please check your CSV files.")
        return None

if __name__ == "__main__":
    cleaned_data = load_and_clean_data()
    if cleaned_data is not None:
        cleaned_data.to_pickle("cleaned_data.pkl")
        print("Data successfully cleaned and saved to cleaned_data.pkl")