from prophet import Prophet
import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('simulated_network_logs.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'])   # <-- convert to datetime
df = df.rename(columns={'timestamp': 'ds', 'packets_per_sec': 'y'})

model = Prophet()
model.fit(df)

future = model.make_future_dataframe(periods=60)
forecast = model.predict(future)

# Find last training date
last_train_date = df['ds'].max()

plt.figure(figsize=(12, 6))

# Plot historical data
plt.plot(df['ds'], df['y'], label='Historical Data', color='black')

# Plot forecasted future data
future_forecast = forecast[forecast['ds'] > last_train_date]
plt.plot(future_forecast['ds'], future_forecast['yhat'], label='Forecast', color='blue')

# Plot confidence interval
plt.fill_between(future_forecast['ds'], 
                 future_forecast['yhat_lower'], 
                 future_forecast['yhat_upper'], 
                 color='blue', alpha=0.2, label='Confidence Interval')

# Mark forecast start
plt.axvline(x=last_train_date, color='red', linestyle='--', label='Forecast Start')

# Labels, title, and grid
plt.xlabel('Time')
plt.ylabel('Packets per second')
plt.title('Network Traffic Forecast (Historical + Future)')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig('network_traffic_forecast.png')

print("Forecast plot saved to 'network_traffic_forecast.png'.")
