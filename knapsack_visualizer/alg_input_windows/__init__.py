
# This lets us do internal imports form the same directory
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__)))
sys.path.append("..") # Adds higher directory to python modules path, so we can import knapsack in our window files

# Add other input windows here.
import knapsack_input_window, lcs_input_window