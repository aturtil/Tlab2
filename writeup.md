## Question 1

Take a look at the file labeled `data/data2.txt`. Why might we have missing values or values that state "NO SIGNAL" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

It’s possible the "NO SIGNAL" values occurred due to issues like the heart rate equipment being poorly placed, such as when sensors slipped from movement or the battery died, preventing proper data collection. Additionally, the participant may have intentionally removed the device (e.g., for a shower) or accidentally displaced it. Glitches or technical malfunctions in the device or program could also contribute. Risks of filtering out these values include introducing biased data, as "NO SIGNAL" periods could correspond to specific activities like exercise or sleep positions. Without additional context about the participant's activities, understanding the cause of "NO SIGNAL" becomes challenging. Excluding these values could impact key metrics like rolling averages and standard deviations, potentially skewing the analysis.

## Question 2

While the "averages.png" and "maximums.png" graphs visualize typical values in our time-series data of heart rates and subsequently describe similar trends, the "stdevs.png" graph visualizes the standard deviations, which results in a graph with less apparent trends. In the context of heart rate, what does the standard deviation describe?

The standard deviation represents the variability of the heart rate from the average heart rate over a time period, meaning if there is a higher standard deviation, then there is a greater range of physical activity being performed within the interval (like sleeping to running) and a lesser standard deviation means there is a more consistent level of activity (like just sleeping or just exercising). When examined across intervals, such as 5 minute windows, the standard deviation reveals the variety in activity within those periods. For instance, heart rate variability during 5 minutes highlights transitions between restful states to more active ones. 

## Question 3

Run your `main.py` module and look at the graph labeled "averages.png." Roughly speaking, where do you see the time series experience a significant difference in values along the x-axis? Point out all x-values where you notice a drastic difference in future values.

Dataset 1:
    Significant increase: Around 50 minutes, the average rises from 60 to 90.
    Significant decrease: Between 125 and 150 minutes, the average drops from 90 to 55.
    Other fluctuations: Between 50 and 80 for the remainder of the graph, with more noticeable changes occurring between 175 and 250 minutes.
    Around x = 50 minutes: This is already identified as a point of significant increase. It is reasonable to expect that changes in the data leading up to this point might have influenced this increase. Therefore, values around x = 40-50 minutes could be points of interest.
    Around x = 125-150 minutes: This range marks a significant decrease. Analyzing data around this region might reveal patterns or factors contributing to this drop.
    Around x = 175-250 minutes: This interval is mentioned to have more noticeable changes. It's possible that these changes could indicate trends or shifts that might influence future values.

Dataset 2:
    Greatest increase: Between 20 and 25 minutes, the average jumps from 75 to 115.
    Slight decrease: Between 25 and 30 minutes, the average drops back to 85.
    The average continues to fluctuate between 95 and 85 for a while.
    Another increase: At 125 minutes, the average increases to 105.
    Around x = 20 minutes: This is already identified as a point of significant increase. It is reasonable to expect that changes in the data leading up to this point might have influenced this increase. Therefore, values around x = 15-20 minutes could be points of interest.
    Around x = 25 minutes: A point where the average drops back down. This sudden change could be a signal of a trend reversal or a shift in the underlying factors influencing the data.
    Around x = 125 minutes: This point marks another increase. Analyzing data around this region might reveal patterns or factors contributing to this rise.

Dataset 3:
    Initial rise: The average starts around 65 and then soars to 95, beginning around 25 minutes and ending by 50 minutes.
    Range: After that, the values fluctuate between 95 and 80 up to around 200 minutes, where it starts to drop.
    Around x = 25 minutes: This is where the initial rise begins. It is reasonable to expect that changes in the data leading up to this point might have influenced this increase. Therefore, values around x = 20-25 minutes could be points of interest.
    Around x = 50 minutes: This is the end of the initial rise. Analyzing data around this region might reveal patterns or factors contributing to the change in trend.
    Around x = 200 minutes: This is where the average might start to drop after a period of fluctuation. This change in direction could be a signal of a new trend or shift in the underlying factors influencing the data.

## Question 4

Do you also notice a corresponding difference in values in the "stdevs.png" graph? If so, do these differences align with the "averages.png" graph? 

When the average fluctuates rapidly or experiences noticeable changes, the standard deviation tends to be higher, indicating greater variability in the data. A low standard deviation suggests that the data points are closely clustered around the average, making it more stable and less likely to change dramatically. Significant increases or decreases in the average typically result in a higher standard deviation, reflecting greater fluctuations in the data.
