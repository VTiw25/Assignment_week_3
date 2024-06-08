import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
data = pd.read_csv('oil.csv')

# Convert 'date' column to datetime format for better handling in plots
data['date'] = pd.to_datetime(data['date'])

# Plotting the data
plt.figure(figsize=(12, 6))
plt.plot(data['date'], data['dcoilwtico'], label='Oil Price')
plt.xlabel('Date')
plt.ylabel('Oil Price (dcoilwtico)')
plt.title('Oil Price Over Time')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)  # Rotate date labels for better readability
plt.tight_layout()  # Adjust layout for better fit
plt.show()
