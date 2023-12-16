import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define the S&P 500 ETF ticker symbol (SPY)
ticker_symbol = "SPY"

# Define the start and end dates for the full existence of the S&P 500
start_date = "1950-01-01"
end_date = "2023-01-01"

# Fetch historical data from Yahoo Finance
data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Function to calculate annualized growth rate
def calculate_annual_growth_rate(df):
    start_price = df.iloc[0]['Adj Close']
    end_price = df.iloc[-1]['Adj Close']
    num_years = len(df) / 252  # Assuming 252 trading days in a year
    annual_growth_rate = ((end_price / start_price) ** (1 / num_years)) - 1
    return annual_growth_rate * 100  # Convert to percentage

# Function to calculate average growth rates for different time periods
def calculate_average_growth_rates(data, delta_years):
    num_years = len(data) / 252  # Assuming 252 trading days in a year
    max_delta_years = int(num_years) - delta_years + 1  # Adjusted the range here
    average_growth_rates = []

    for delta in range(max_delta_years):
        start_index = delta * 252
        end_index = (delta + delta_years) * 252
        subset_data = data.iloc[start_index:end_index]
        annual_growth_rate = calculate_annual_growth_rate(subset_data)
        average_growth_rates.append(annual_growth_rate)

    return average_growth_rates

# Ask the user for the range of the time period (e.g., 10 years)
delta_years = int(input("Enter the range of time period (in years): "))

# Calculate average growth rates for different time periods
average_growth_rates = calculate_average_growth_rates(data, delta_years)

# Create a date range for x-axis starting from the end of the first delta_years
x_values = pd.date_range(start=data.index[delta_years * 252 - 1], periods=len(average_growth_rates), freq='D')

# Create a DataFrame with date index and average growth rates
growth_df = pd.DataFrame({'Date': x_values, 'Avg Growth Rate': average_growth_rates})

# Create a figure with subplots to display price feed and average growth rate
fig, ax1 = plt.subplots(figsize=(12, 6))
ax2 = ax1.twinx()

# Plot price feed on the first axis
ax1.plot(data.index, data['Adj Close'], label='Price', color='blue')
ax1.set_xlabel('Date')
ax1.set_ylabel('Price', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Plot average growth rate on the second axis
ax2.plot(growth_df['Date'], growth_df['Avg Growth Rate'], label=f'Avg Growth Rate ({delta_years}-year period)', color='green')
ax2.set_ylabel(f'Annual Growth Rate ({delta_years}-year period) (%)', color='green')
ax2.tick_params(axis='y', labelcolor='green')

# Add title and legend
plt.title(f"Price Feed and Average Annual Growth Rate (ΔT = {delta_years} years)")
fig.legend(loc='upper left')

plt.show()


#this is nothing
#really nothing
#new 2