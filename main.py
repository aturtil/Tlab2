import os
import matplotlib.pyplot as plt
from metrics import window_max, window_average, window_stddev
from cleaner import filter_nondigits, filter_outliers




def run(filename: str) -> list:
   """
   Process heart rate data from the specified file, clean it, calculate metrics,
   and save visualizations.


   Args:
       filename (str): The path to the data file (e.g., 'data/data1.txt').


   Steps:
       1. Read the file into a list of strings.
       2. Use `filter_nondigits` to clean the data and remove invalid entries.
       3. Use `filter_outliers` to remove unrealistic heart rate samples (<30 or >250).
       4. Calculate rolling maximums, averages, and standard deviations using functions from `metrics.py`.
       5. Save the plots to the `images/` folder:
          - Rolling maximums -> 'images/maximums_{filename}.png'
          - Rolling averages -> 'images/averages_{filename}.png'
          - Rolling standard deviations -> 'images/stdevs_{filename}.png'


   Returns:
       list[int], list[int], list[int]: You will return the maximums, averages, and stdevs (in this order).
   """
   # Ensure the images directory exists
   if not os.path.exists("images"):
       os.makedirs("images")


   # Read and clean the data
   with open(filename, 'r') as file:
       data = file.readlines()


   cleaned_data = filter_nondigits(data)
   cleaned_data = filter_outliers(cleaned_data)


   # Calculate metrics
   max_values = window_max(cleaned_data, n=6)
   avg_values = window_average(cleaned_data, n=6)
   stddev_values = window_stddev(cleaned_data, n=6)


   # Extract the dataset name without extension to use in image filenames
   base_filename = os.path.basename(filename).replace('.txt', '')


   # Plot and save max values
   plt.plot(max_values, label="Max Values")
   plt.title(f"Rolling Maximums for {filename}")
   plt.xlabel("Window")
   plt.ylabel("Maximum")
   plt.legend()
   plt.savefig(f"images/maximums_{base_filename}.png")  # Save with the base filename
   plt.clf()


   # Plot and save average values
   plt.plot(avg_values, label="Average Values")
   plt.title(f"Rolling Averages for {filename}")
   plt.xlabel("Window")
   plt.ylabel("Average")
   plt.legend()
   plt.savefig(f"images/averages_{base_filename}.png")  # Save with the base filename
   plt.clf()


   # Plot and save standard deviation values
   plt.plot(stddev_values, label="Standard Deviation")
   plt.title(f"Rolling Standard Deviations for {filename}")
   plt.xlabel("Window")
   plt.ylabel("Standard Deviation")
   plt.legend()
   plt.savefig(f"images/stdevs_{base_filename}.png")  # Save with the base filename
   plt.clf()


   print(f"Plots saved successfully in the 'images' folder for {filename}.")
   return max_values, avg_values, stddev_values




if __name__ == "__main__":
   # Process all `.txt` files in the 'data/' directory
   for filename in os.listdir('data'):
       if filename.endswith('.txt'):
           filepath = os.path.join('data', filename)  # Create full path for each file
           run(filepath)  # Call run() for each file