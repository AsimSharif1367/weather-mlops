import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

def preprocess_data():
    # Read raw data
    df = pd.read_csv('data/raw/raw_data.csv')
    
    # Handle missing values
    df = df.fillna(df.mean(numeric_only=True))
    
    # Convert datetime
    df['datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'])
    
    # Normalize numerical fields
    scaler = StandardScaler()
    numerical_columns = ['temperature', 'humidity', 'wind_speed']
    df[numerical_columns] = scaler.fit_transform(df[numerical_columns])
    
    # Save processed data
    os.makedirs('data/processed', exist_ok=True)
    df.to_csv('data/processed/processed_data.csv', index=False)
    print("Data preprocessed and saved to data/processed/processed_data.csv")

if __name__ == "__main__":
    preprocess_data()