# Surfs Up

## Overview
The purpose of this analysis is to understand the temperature trends in Oahu, so we may determine if opening a surf and ice cream shop is sustainable for the year. In this analysis, I am looking specifically at temperature trends in June and December to compare weather patterns in two halves of the year.

## Analysis

This analysis tested our familiarty with using sqlite and sqlalchemy. I used both to extract data from the weather database and determine the summary statistics for temperatures first in June and then in December.  Turning the data into a list, I converted it to a dataframe and used .describe() to pull the summary statistics.  I used the same code below to pull the December data utilized "12" as the filter date.

```
# 1. Write a query that filters the Measurement table to retrieve the temperatures for the month of June. 
june_temps = session.query(Measurement.tobs).\
    filter(func.strftime ("%m", Measurement.date) == "06").all()

# 2. Convert the June temperatures to a list.
june_temps = list(np.ravel(june_temps))

# 3. Create a DataFrame from the list of temperatures for the month of June. 
june_temps_df = pd.DataFrame(june_temps, columns=["June_Temps"])
june_temps_df.head(10)

```
With the descriptive statistics in separate cells, I wanted to be able to compare them more closely, so I turned each of them into a dataframe and combined them using the following code, which produces the combined dataframe below.
```
dec_info = dec_temps_df.describe()
june_info = june_temps_df.describe()

temps_summary_df = june_info.merge(dec_info, left_index=True, right_index=True)
temps_summary_df
```

![temps_summary]()

Since the data is spread between different stations, I plotted both June and December into histograms to better visualize the spread of the data and summarize the findings.

![june_temps_hist]()
![dec_temps_hist]()

## Results

- As expected, the average temperature is higher for June compared to December.
  - Average temperature only varies between the months by approximately 4 degrees.
  - The high temperature is in fact only 2 degrees more in June than December.

- Temperatures are more variable in December.
  - The lowest temperature is 8 degrees lower than June meaning there is a wider range of varying temperatures.
  - Looking at the histograms, we can see the tighter bell curve of June compared to December showing that temperatures tend to be more stable during that month.

- Despite some variance, both months have an acceptable range of temperatures for both surfing & ice cream.
  - The majority of days fall between the mid 60s to the low 80s for both months.


## Summary

Overall, the statistics on temperatures for June and December on Oahu show that weather does not vary drastically throughout the year. Temperatures may be more consistent in warmer seasons, but the average daily temperatures still range mostly in the 70s, an acceptable temperature for surfing. This means there will be a draw for customers for any beach business promoting surfing and probably ice cream as well.

To better understand this temperature, I took an average of the temperatures by day of the month. Since this data is over several years, it does not show the dramatic highs and lows of the summary statistics, but it further supports the conclusion that the temperatures are consistent.  Though December is expectedly lower on average than June, the average temperatures day to day are still within the ideal range of the 70s.

![avg_temp_plot]()

A comparison of precipitation would also benefit our understanding of weather that impacts potential sales for our business. A quick look at the average by day of the month shows us that the average precipitation is fairly low for both months with a spike in mid-December. This further supports our conclusion that weather is ideal for our proposed beach business.  Plotting precipitation in a histogram by day rather than a "day of the month average" would give us a better visual on outliers for precipitation.

![avg_prcp_plot]()

In conclusion, the data shows us that with little variance in weather and low average precipitation, the island of Oahu is a great choice for our proposed surf and ice cream shop.  To help us choose a more specific location, I suggest comparing temperature and precipitation based on weather station id. This will help us focus in on the areas of the island that will best support the proposed business.


