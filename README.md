# Justin's Sleep Analysis Project
This project aims to analyze my personal sleep data from during my time here at Gonzaga University and includes Spokane's weather data to examine possible correlations between my sleep quality and the weather. The primary goal is to see changes in my sleep quality and decide if major habit changes are necessary.  

The project is organized in a logical manner:
1. Intro and overview
1. Cleaning and Preparation
1. Exploratory Data Analysis including stats, visualizations, and hypothesis tests
1. Classification Modeling
1. Conclusion

This project utilizes the following:
* Python 3.12.7 provided by Anaconda
* Jupyter Notebook
* Python utility file
* My sleep data in a csv file titled "sleep_score.csv"
* MeteoStat API: Daily Data Endpoint
    * You will need your own API key from [RapidAPI](https://rapidapi.com/meteostat/api/meteostat) to run this project
        * Subscribe to the basic plan and click "Open Playground" on the left. Your API key will be under "X-RapidAPI-Key"
        * Copy and paste your key under `get_spokane_weather_df()` in utils.py to replace `api.get_metoeostat_token()` as described there
