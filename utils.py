"""
Justin Yi
4/22/25
CPSC 222
Description:
This file contains utility functions used for
my Quantified Self Project
"""

import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
import api_token as api

# This function fulfills a get request with a 
# given url and header
def get_response_as_json_with_header(url, header):
    response = requests.get(url=url, headers=header)
    json_object = response.json()
    return json_object

# This function extracts and returns the closest weather
# station's ID from the given json object 
def extract_station_id_from_closest(json_obj):
    data_obj = json_obj["data"][0]
    id_obj = str(data_obj["id"])
    return id_obj

# This function extracts weather data from a given
# json object
def get_weather_data_from_json(json_obj):
    df = pd.DataFrame(json_obj["data"])
    return df

# This function fills in missing values based 
# on other values
def fill_missing_values(df):
    df.interpolate(method="linear", inplace=True)
    df.bfill(inplace=True) # Fill first value if missing
    df.ffill(inplace=True) # Fill last value if missing
    return df

# This function combines some of the functions above
# to create and return a DataFrame of Spokane's
# weather data from 2023-08-26 to 2025-04-16 
def get_spokane_weather_df():
    # NOTE: If you'd like to run this yourself, you'll need your own API token:
    # Replace "api.get_metoeostat_token()" with:
    # {"x-rapidapi-key": (token string here)}
    meteo_headers = api.get_metoeostat_token()
    
    stations_endpt_url = "https://meteostat.p.rapidapi.com/stations/nearby"
    daily_data_endpt_url = "https://meteostat.p.rapidapi.com/stations/daily"
    spokane_lat = str(47.65810637901106)
    spokane_lon = str(-117.42101550597343)
    stations_endpt_url += "?lat=" + spokane_lat + "&lon=" + spokane_lon
    station_json_obj = get_response_as_json_with_header(stations_endpt_url, meteo_headers)
    station_id = extract_station_id_from_closest(station_json_obj)
    daily_data_endpt_url += "?station=" + station_id + "&start=2023-08-26&end=2025-04-16" + "&units=imperial"
    weather_json_obj = get_response_as_json_with_header(daily_data_endpt_url, meteo_headers)
    weather_df = get_weather_data_from_json(weather_json_obj)
    return weather_df

# This function completely removes the
# undesired column
def drop_column(df, column):
    df.drop(columns=column, inplace=True)
    return df

# This function completely removes
# empty columns
def drop_empty_columns(df):
    df.dropna(axis=1,how="all", inplace=True)
    return df

# This function drops rows from the given
# starting index to given ending index
def drop_rows_by_starting_index(df, starting_index, ending_index):
    df.drop(df.index[starting_index:ending_index], inplace=True)
    return df

# This function slices and removes string elements
# from each column element in the given df's column
def remove_string_ends(df, column, starting_index):
    df[column] = df[column].str.slice_replace(start=starting_index)
    return df

# This functions decodes overall sleep scores
# by using the pandas replace function with 
# lists
def decode_sleep_scores(df):
    list_ex = range(90, 101)
    list_good = range(80, 90)
    list_fair = range(60, 80)
    list_poor = range(0, 60)

    df.replace({"overall_score": list_ex}, "Excellent", inplace=True)
    df.replace({"overall_score": list_good}, "Good", inplace=True)
    df.replace({"overall_score": list_fair}, "Fair", inplace=True)
    df.replace({"overall_score": list_poor}, "Poor", inplace=True)

    return df

# This function converts the date column to a 
# datetime object and extracts the day, month,
# and year columns
def create_datetime_columns(df):
    # The date column is the index
    df.index = pd.to_datetime(df.index)

    # Need to reformat each column to the front
    # for easier readability
    df["day"] = df.index.day
    day_column = df.pop("day") 
    df.insert(0, "day", day_column) 

    df['month'] = df.index.month
    month_column = df.pop("month") 
    df.insert(0, "month", month_column) 

    df['year'] = df.index.year
    year_column = df.pop("year") 
    df.insert(0, "year", year_column) 

    return df

# This function creates a line graph with a
# DataFrame's selected columns, title
# and labels
def create_line_graph(x_column, y_column, title, x_label, y_label):
    plt.figure(figsize=(25, 15))
    plt.plot(x_column, y_column)
    plt.xlabel(x_label, fontsize=30)
    plt.ylabel(y_label, fontsize=30)
    plt.title(title, fontsize=40)
    plt.xticks(rotation=45, fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlim(pd.Timestamp('2023-08-26'), pd.Timestamp('2025-04-16'))
    plt.tight_layout()
    title += ".png"
    plt.savefig(title)
    plt.show()

# This function creates a bar chart with a
# DataFrame's selected columns, title,
# and labels
def create_bar_chart(x_column, y_column, title, x_label, y_label):
    plt.figure(figsize=(25, 15))
    plt.bar(x_column, y_column.tolist())
    plt.xlabel(x_label, fontsize=30)
    plt.ylabel(y_label, fontsize=30)
    plt.title(title, fontsize=40)
    plt.xticks(rotation=45, fontsize=20)
    plt.yticks(fontsize=20)
    plt.tight_layout()
    plt.show()

# This function creates a scatter plot with 
# the given arguments; the goal of it is to 
# see possible correlations
def create_scatter_plot(x_pos, y_pos, title, x_label, y_label):
    plt.figure(figsize=(25, 15))
    plt.scatter(x_pos, y_pos)
    plt.xlabel(x_label, fontsize=30)
    plt.ylabel(y_label, fontsize=30)
    plt.title(title, fontsize=40)
    plt.xticks(rotation=45, fontsize=20)
    plt.yticks(fontsize=20)
    plt.tight_layout()
    plt.show()