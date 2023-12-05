import pandas as pd
import matplotlib.pyplot as plt

# Creating a fictitious dataset
data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'Product A': [50, 60, 45, 55, 70],
    'Product B': [30, 40, 35, 45, 50],
    'Product C': [20, 25, 30, 35, 40],
}

# Converting data to a DataFrame
df = pd.DataFrame(data)

# Converting the 'Date' column to date format
df['Date'] = pd.to_datetime(df['Date'])

# Displaying general information about the data
print("General information about the data:")
print(df.info())

# Displaying the first rows of data
print("\nFirst rows of data:")
print(df.head())

# Describing the statistical summary of the data
print("\nDescriptive statistics:")
print(df.describe())

# Plotting sales over dates
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Product A'], label='Product A', marker='o')
plt.plot(df['Date'], df['Product B'], label='Product B', marker='o')
plt.plot(df['Date'], df['Product C'], label='Product C', marker='o')

plt.title('Product Sales Chart')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.show()
