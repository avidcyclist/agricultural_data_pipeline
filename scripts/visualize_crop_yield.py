import pandas as pd
import matplotlib.pyplot as plt

# Load the crop yield data
csv_file_path = "C:/Users/Mitch/Desktop/agricultural_data_pipeline/data/crop_yield_data.csv"
data = pd.read_csv(csv_file_path)

# Convert 'yield' column to numeric, forcing errors to NaN and then dropping them
data['yield'] = pd.to_numeric(data['yield'], errors='coerce')
data.dropna(subset=['yield'], inplace=True)

# Filter data for the year 2021
data_2021 = data[data['year'] == 2021]

# Plot the crop yield data for 2021
plt.figure(figsize=(12, 8))
plt.bar(data_2021['county'], data_2021['yield'], color='skyblue')
plt.xlabel('County')
plt.ylabel('Yield')
plt.title('Crop Yield by County for the Year 2021')
plt.xticks(rotation=90)  # Rotate county names for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()