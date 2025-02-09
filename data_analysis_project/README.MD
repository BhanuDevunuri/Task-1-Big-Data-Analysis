# COVID-19 Data Analysis with Dask and Matplotlib

## Project Overview
This project analyzes COVID-19 data using **Dask** for efficient data handling and **Matplotlib** for visualization. It focuses on calculating **Recovery Rate (%)** and **Death Rate (%)**, and visualizing the top 5 countries with the highest confirmed cases.

## Dataset
The project uses a CSV file named `country_wise_latest.csv`, which contains COVID-19 data categorized by country/region. The key columns used in this analysis are:
- `Country/Region`
- `Confirmed`
- `Deaths`
- `Recovered`
- `Active`

## Requirements
Ensure you have the following Python libraries installed:

```bash
pip install dask matplotlib pandas
```

## Code Explanation
1. **Load Data Efficiently with Dask:**
   - The dataset is read using `dask.dataframe.read_csv` for better performance on large datasets.
   
2. **Data Processing:**
   - Select relevant columns.
   - Compute `Recovery Rate (%)` and `Death Rate (%)`.
   
3. **Find Top 5 Countries by Confirmed Cases:**
   - `nlargest(5, "Confirmed")` is used to filter the top 5 countries.
   
4. **Visualization with Matplotlib:**
   - A bar chart is created to display confirmed cases for the top 5 countries.

## Running the Script
Execute the script using:

```bash
python script.py
```

Make sure `country_wise_latest.csv` is present in the same directory as the script.

## Output
- A printed table displaying the top 5 countries by confirmed cases.
- A bar chart visualizing the confirmed cases for these countries.



