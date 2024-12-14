import statistics
def window_max(data: list, n: int) -> list:
   maximums = []
   for i in range(0, len(data), n):   
      maximums.append(round(max(data[i:i +n]), 2))
   return maximums

import statistics
def window_average(data: list, n: int) -> list:
   averages = []  # List to store the averages
   for i in range(0, len(data), n):
      averages.append(round(statistics.mean(data[i:i +n]), 2))
   return averages

import statistics

def window_stddev(data: list, n: int) -> list:
    stddevs = []  # Rename to clarify purpose
    if not data or n <= 0:
        return stddevs

    # Loop through non-overlapping windows
    for i in range(0, len(data), n):
        window = data[i:i + n]
        if len(window) > 1:  # Ensure enough data for standard deviation
            std_dev = statistics.stdev(window)  # Compute standard deviation
            stddevs.append(round(std_dev, 2))  # Append rounded value

    return stddevs
