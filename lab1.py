import pandas as pd 
import numpy as np 

# Load the dataset 
file_name = r"C:\Users\anila\OneDrive\Desktop\Algo_Lab_Exam\AQI_Data.csv"   
data = pd.read_csv(file_name)  

# a) Display the first 5 rows 
print("First 5 rows of the dataset:") 
print(data.head())  

# b) Display the last 6 rows 
print("\nLast 6 rows of the dataset:") 
print(data.tail(6))  

# c) Summary statistics for all numeric columns 
print("\nSummary statistics for numeric columns:") 
print(data.describe())  

# d) Compute the mean AQI, PM2.5, and PM10 values for each city 

cities = data['City'].values
aqi = data['AQI'].values
pm25 = data['PM2.5'].values
pm10 = data['PM10'].values

unique_cities = np.unique(cities)

for city in unique_cities:
    city_mask = cities == city
    mean_aqi = np.mean(aqi[city_mask])
    mean_pm25 = np.mean(pm25[city_mask])
    mean_pm10 = np.mean(pm10[city_mask])

    print(f"city: {city}, Mean AQI: {mean_aqi}, Mean PM2.5: {mean_pm25}, Mean PM10: {mean_pm10}")


# Group the data by 'City' and calculate the mean AQI for each city 
city_aqi_means = data.groupby('City')['AQI'].mean()  
city_aqi_dict = city_aqi_means.to_dict()  

# Find the city with the highest and lowest average AQI 
highest_aqi_city = max(city_aqi_dict, key=city_aqi_dict.get) 
lowest_aqi_city = min(city_aqi_dict, key=city_aqi_dict.get)  

# Get the AQI values for the highest and lowest cities 
highest_aqi_value = city_aqi_dict[highest_aqi_city] 
lowest_aqi_value = city_aqi_dict[lowest_aqi_city]  

# Print the results 
print("\n\nCity with the highest average AQI:") 
print(f"{highest_aqi_city} with AQI {highest_aqi_value}")  

print("\nCity with the lowest average AQI:") 
print(f"{lowest_aqi_city} with AQI {lowest_aqi_value}")  
