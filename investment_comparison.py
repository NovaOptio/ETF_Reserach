# Investment Comparison Script

# This Python script compares the growth of two investment funds over a set number of years,
# considering different annual costs for each fund. It calculates and visualizes
# the future values of the investments, showcasing the impact of varying costs.

# The code generates two plots:
# 1. Investment Growth Comparison: Shows how Fund 1 and Fund 2 evolve over time.
# 2. Annual Cost Differences (Positive): Illustrates the absolute annual difference in
#    value between the two funds due to costs.

import matplotlib.pyplot as plt
import numpy as np
import os


# Constants
initial_investment = 10000
annual_growth_rate = 0.10
cost_fund1_percentage = 0.5  # %
cost_fund2_percentage = 0.05  # %
years = 30

# Convert percentages to decimal
cost_fund1 = cost_fund1_percentage / 100
cost_fund2 = cost_fund2_percentage / 100

# Function to calculate future value with cost
def calculate_future_value(initial_investment, growth_rate, cost, years):
    future_values = []
    for year in range(1, years+1):
        future_value = initial_investment * ((1 + growth_rate - cost) ** year)
        future_values.append(future_value)
    return future_values

# Calculate future values for both funds
fund1_values = calculate_future_value(initial_investment, annual_growth_rate, cost_fund1, years)
fund2_values = calculate_future_value(initial_investment, annual_growth_rate, cost_fund2, years)

# Calculate the absolute annual difference due to costs
annual_differences = np.abs(np.array(fund1_values) - np.array(fund2_values))

# Calculate the final values for both funds
final_value_fund1 = fund1_values[-1]
final_value_fund2 = fund2_values[-1]
difference_due_to_costs = final_value_fund1 - final_value_fund2

# Print the results
print(f'Final value after {years} years for Fund 1: €{final_value_fund1:.2f}')
print(f'Final value after {years} years for Fund 2: €{final_value_fund2:.2f}')
print(f'Difference due to costs: €{difference_due_to_costs:.2f}')


# Plot 1: Investment Growth Comparison
plt.figure(figsize=(14, 5))

plt.subplot(1, 2, 1)
plt.plot(fund1_values, label=f'Fund 1 ({cost_fund1_percentage}% Costs)', color='blue')
plt.plot(fund2_values, label=f'Fund 2 ({cost_fund2_percentage}% Costs)', color='red')
plt.title('Investment Growth')
plt.xlabel('Years')
plt.ylabel('Future Value (€)')
plt.legend()

# Plot 2: Annual Difference Due to Costs (Positive)
plt.subplot(1, 2, 2)
plt.bar(range(1, years+1), annual_differences, color='orange')
plt.title('Annual Difference Due to Costs')
plt.xlabel('Years')
plt.ylabel('Absolute Difference in €')
plt.tight_layout()

# Save the chart with the specified filename in the same folder as the script
filename = f"Investment_Chart_{cost_fund1_percentage}%_vs_{cost_fund2_percentage}%.png"
save_path = os.path.join(os.path.dirname(__file__), filename)  # Get the script's directory
plt.savefig(save_path)

# Show the plots
plt.show()
