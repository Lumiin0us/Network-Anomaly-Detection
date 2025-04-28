import pandas as pd 
import numpy as np 
import random

np.random.seed(42)

minutes = 1440 # In a day 
timestamps = pd.date_range(start="2025-04-28", periods=minutes, freq='T')

packets_per_sec_base = 500 + 30*np.sin(np.linspace(0, 10*np.pi, minutes))
bandwidth_base = 50 + 10*np.sin(np.linspace(0, 5*np.pi, minutes))
packet_loss_base = np.clip(np.random.normal(0.2, 0.05, minutes), 0, 5)
latency_base = 40 + 5*np.sin(np.linspace(0, 8*np.pi, minutes))

# Add random noise
packets_per_sec = packets_per_sec_base + np.random.normal(0, 10, minutes)
bandwidth = bandwidth_base + np.random.normal(0, 5, minutes)
packet_loss = packet_loss_base + np.random.normal(0, 0.1, minutes)
latency = latency_base + np.random.normal(0, 2, minutes)

# Clip values to be positive
packets_per_sec = np.clip(packets_per_sec, 0, None)
bandwidth = np.clip(bandwidth, 0, None)
packet_loss = np.clip(packet_loss, 0, 100)
latency = np.clip(latency, 0, None)

# Create DataFrame
network_data = pd.DataFrame({
    'timestamp': timestamps,
    'packets_per_sec': packets_per_sec,
    'bandwidth_mbps': bandwidth,
    'packet_loss_percent': packet_loss,
    'latency_ms': latency
})

# Inject some anomalies (10 random timepoints)
anomaly_indices = random.sample(range(minutes), 10)

for idx in anomaly_indices:
    network_data.loc[idx, 'packets_per_sec'] *= np.random.uniform(1.5, 2.5)
    network_data.loc[idx, 'packet_loss_percent'] *= np.random.uniform(2, 5)
    network_data.loc[idx, 'latency_ms'] *= np.random.uniform(1.5, 2.5)


# Save to CSV
network_data.to_csv('simulated_network_logs.csv', index=False)

print(timestamps)