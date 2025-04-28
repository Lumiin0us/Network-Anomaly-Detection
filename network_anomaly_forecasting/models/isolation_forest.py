import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest

# Step 1: Load Data
data = pd.read_csv('simulated_network_logs.csv')

# Step 2: Drop timestamp for model training
X = data.drop(columns=['timestamp'])

# Step 3: Train-test split
train_x, test_x = train_test_split(X, test_size=0.2, random_state=42)

# Step 4: Isolation Forest Model
model = IsolationForest(contamination=0.01, random_state=42)
model.fit(train_x)

# Step 5: Predictions
predictions = model.predict(train_x)

# Step 6: Merge predictions back to data
train_x['prediction'] = predictions

# Step 7: Save anomalies to a CSV file
anomalies = train_x[train_x['prediction'] == -1]
anomalies.to_csv('detected_anomalies.csv', index=False)

print(f"Saved {len(anomalies)} anomalies to 'detected_anomalies.csv'.")
