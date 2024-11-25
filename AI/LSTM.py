import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Generate some dummy energy consumption data
np.random.seed(0)
data = np.random.normal(0, 1, 1000)  # Example time-series data, replace this with your actual data
data = pd.DataFrame(data, columns=["EnergyConsumption"])

# Prepare the data for the LSTM model
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data)

# Define a function to create sequences for time-series
def create_sequences(data, seq_length):
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i:i+seq_length])
        y.append(data[i + seq_length])
    return np.array(X), np.array(y)

# Parameters
sequence_length = 50  # Use 50 previous timesteps to predict the next
X, y = create_sequences(scaled_data, sequence_length)

# Split the data into training and testing sets
split_ratio = 0.8
split = int(len(X) * split_ratio)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Reshape data for LSTM input
X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))

# Build the LSTM model
model = Sequential()
model.add(LSTM(units=50, return_sequences=False, input_shape=(sequence_length, 1)))
model.add(Dense(units=1))  # Predict the next energy consumption value

model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32)

# Make predictions
predicted_energy_consumption = model.predict(X_test)
predicted_energy_consumption = scaler.inverse_transform(predicted_energy_consumption)

# Visualize the results
plt.plot(data.index[split + sequence_length:], data["EnergyConsumption"].values[split + sequence_length:], label="True Energy Consumption")
plt.plot(data.index[split + sequence_length:], predicted_energy_consumption, label="Predicted Energy Consumption")
plt.legend()
plt.show()
