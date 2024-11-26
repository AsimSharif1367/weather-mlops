# src/train_model.py
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle
import os

def train_model():
    # Load processed data
    df = pd.read_csv('data/processed/processed_data.csv')
    
    # Prepare features and target
    X = df[['humidity', 'wind_speed']]
    y = df['temperature']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Save model
    os.makedirs('models', exist_ok=True)
    with open('models/model.pkl', 'wb') as f:
        pickle.dump(model, f)
    print("Model trained and saved to models/model.pkl")

if __name__ == "__main__":
    train_model()