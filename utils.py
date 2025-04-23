"""
Justin Yi
4/21/25
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

def read_from_file(infile):
    df = pd.read_csv(infile)
    return df
def drop_column(df, column):
    df.drop(column, axis=column)
    return df
def get_response_as_json_with_header(url, header):
    response = requests.get(url=url, headers=header)
    json_object = response.json()
    return json_object
def extract_station_id_from_closest(json_obj):
    data_obj = json_obj["data"][0]
    id_obj = str(data_obj["id"])
    return id_obj
def get_weather_data_from_json(json_obj):
    df = pd.DataFrame(json_obj["data"])
    return df
def fill_missing_values(df):
    df.interpolate(method="linear", limit_direction="forward", axis="columns", inplace=True)
    df.bfill(inplace=True) # Fill first value if missing
    df.ffill(inplace=True) # Fill last value if missing
    return df
def get_spokane_weather_df():
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
    # weather_df = fill_missing_values(weather_df)
    return weather_df
