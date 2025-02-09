import dask.dataframe as dd
import matplotlib.pyplot as plt 

file_path = "country_wise_latest.csv"
data = dd.read_csv(file_path)

data = data[["Country/Region", "Confirmed", "Deaths", "Recovered", "Active"]]
data["Recovery Rate (%)"] = (data["Recovered"] / data["Confirmed"]) * 100
data["Death Rate (%)"] = (data["Deaths"] / data["Confirmed"]) * 100

top_countries = data.nlargest(5, "Confirmed").compute()
print(top_countries)

plt.bar(top_countries["Country/Region"], top_countries["Confirmed"], color="skyblue")
plt.title("Top 5 Countries by Confirmed Cases")
plt.xlabel("Countries")
plt.ylabel("Confirmed Cases")
plt.show()
