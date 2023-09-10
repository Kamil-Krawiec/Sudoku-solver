import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file into Pandas DataFrames
df = pd.read_csv("sudoku_solver_results.csv")

# Separate the data into advanced and base versions
df_advanced = df[df["IS Advanced Version"]]
df_base = df[df["IS Advanced Version"]]

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df_advanced["Test Case"], df_advanced["Time (s)"], label="Advanced Version", marker="o")
plt.scatter(df_base["Test Case"], df_base["Time (s)"], label="Base Version", marker="x")
plt.xlabel("Test Case Index")
plt.ylabel("Time (s)")
plt.title("Sudoku Solver Performance Comparison")
plt.legend()
plt.yscale("log")  # Set the y-axis to a logarithmic scale
plt.grid(True)

# Show the plot
plt.show()
