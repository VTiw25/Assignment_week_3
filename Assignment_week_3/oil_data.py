import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('oil.csv')

data['date'] = pd.to_datetime(data['date'])

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
