from google.cloud import bigquery
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
sns.set_palette("muted")
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')

def get_raw(sql):
    
    """
    get Chicago taxi fare raw data from BigQuery public dataset
    """
    client = bigquery.Client()
    raw = client.query(sql).to_dataframe()
    return raw


def map_visualization(dataframe, long, lat, name, divisor):
    
    """
    discover between location and frequency, via Chicago map

    green:less frequent
    yellow: more frequent than green, but less frequent than orange
    orange: more frequent than yellow, but less frequent than red
    red: most frequent => popular location

    """
    
    if name == 'count':
        df = dataframe.groupby([long, lat]).size().reset_index(name=name)
    else:
        df = dataframe.groupby([long, lat])['fare'].mean().reset_index(name=name)

    
    import folium

    map_viz = folium.Map(location=[41.895140898, -87.624255632],
                            zoom_start=10,
                            tiles="Stamen Toner") 

    for i in range(df.shape[0]):
        long = df.iloc[i, 0]
        lat = df.iloc[i, 1]
        radius = df[name].iloc[i]/divisor

        if df[name][i] < df[name].quantile(q=0.25):
            color = "green"   
        elif df[name][i] >= df[name].quantile(q=0.25) and df[name][i] < df[name].quantile(q=0.5):
            color = "yellow" 
        elif df[name][i] >= df[name].quantile(q=0.5) and df[name][i] < df[name].quantile(q=0.75):
            color = "orange"
        else:
            color = "red" 

        popup_text = """Latitude : {}<br>
                    Longitude : {}<br>
                    frequency : {}<br>"""
        popup_text = popup_text.format(lat,
                                   long,
                                   df[name].iloc[i]
                                   )
        
        folium.CircleMarker(location = [lat, long], popup= popup_text,radius = radius, color = color, fill = True).add_to(map_viz)

    return map_viz


def dist_plot(dataframe, col):
    
    """
    reveal pattern through distribution plot
    """
    
    plt.figure(figsize=(12,5))
    for i in range(len(col)):
        sns.distplot(dataframe[col[i]], hist=False, label=col[i])
    plt.show()


def dayofweek(weekday):
    
    """
    convert string to number
    """
    
    if weekday == 'Mon':
        return 1
    elif weekday == 'Tue':
        return 2
    elif weekday == 'Wed':
        return 3
    elif weekday == 'Thu':
        return 4
    elif weekday == 'Fri':
        return 5
    elif weekday == 'Sat':
        return 6
    else:
        return 7


def dayofyear(timestamp):
    
    """
    order the date in a year order
    """
    
    import datetime

    return (timestamp - datetime.datetime(timestamp.year, 1, 1)).days + 1


def priceVSday(data_by_year, year):
    
    import matplotlib as mpl

    temp = data_by_year[['trip_start_timestamp']]
    temp['trip_start_timestamp'] = pd.to_datetime(temp['trip_start_timestamp'].astype(str).map(lambda x: x.split()[0]))
    tmp = temp.groupby(['trip_start_timestamp'], as_index=True).size().to_frame()
    tmp = tmp.rename({0: "count"}, axis=1)
    del tmp.index.name
    by_date = tmp.pivot_table('count', [tmp.index.month, tmp.index.day])
    by_date.index = [pd.datetime(year, month, day) for (month, day) in by_date.index]
    fig, ax = plt.subplots(figsize=(20, 7))
    by_date.plot(ax=ax)
    style = dict(size=10, color='gray')

    ax.annotate("New Year's Day", xy=(str(year)+'-1-1', 30), xytext=(str(year)+'-1-1', 10), arrowprops=dict(facecolor='black', shrink=0.05))
    ax.annotate("Independence Day", xy=(str(year)+'-7-4', 30), xytext=(str(year)+'-7-4', 10), arrowprops=dict(facecolor='black', shrink=0.05))
    ax.annotate("Halloween", xy=(str(year)+'-10-31', 30), xytext=(str(year)+'-10-31', 10), arrowprops=dict(facecolor='black', shrink=0.05))
    ax.annotate("Thanksgiving", xy=(str(year)+'-11-25', 30), xytext=(str(year)+'-11-25', 10), arrowprops=dict(facecolor='black', shrink=0.05))
    ax.annotate("Chrismas", xy=(str(year)+'-12-25', 10), xytext=(str(year)+'-12-25', 10), arrowprops=dict(facecolor='black', shrink=0.05))

    # Format the x axis with centered month labels
    ax.xaxis.set_major_locator(mpl.dates.MonthLocator())
    ax.xaxis.set_minor_locator(mpl.dates.MonthLocator(bymonthday=15))
    ax.xaxis.set_major_formatter(plt.NullFormatter())
    ax.xaxis.set_minor_formatter(mpl.dates.DateFormatter('%h'))
    plt.show()


def is_holiday(dataframe, timestamp):
    
    """
    create a boolean column to indicate if the timestamp day is a US holiday
    """
    
    from pandas.tseries.holiday import USFederalHolidayCalendar as calendar
    cal = calendar()
    holidays = cal.holidays(start=pd.to_datetime(dataframe[timestamp].astype(str).map(lambda x: x.split(' ')[0])).min(),                             end=pd.to_datetime(dataframe[timestamp].astype(str).map(lambda x: x.split(' ')[0])).max())

    return pd.to_datetime(dataframe[timestamp].astype(str).map(lambda x: x.split(' ')[0])).isin(holidays)


def is_weekend(dataframe, timestamp):
    return dataframe[timestamp].map(lambda x: True if x==6 or x==7 else False)


def scatter_plot(dataframe, colX, colY):
    plt.figure(figsize=(5, 5))
    sns.scatterplot(dataframe[colX], dataframe[colY])
    plt.show()


from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import IsolationForest
    
class iForest(object):

    def __init__(self, data):
        self.df = data.copy()
    
    def scale(self):
        scaler = MinMaxScaler()
        scaler.fit(self.df)
        scale_df = scaler.transform(self.df)
        return scale_df

    def model(self, df):
        clf = IsolationForest(n_estimators = 100, max_samples = 256, random_state = 42, contamination = 0.2, 
                              bootstrap = False, verbose = 1, n_jobs = -1, max_features = df.shape[1])
        clf.fit(df)
        scores = clf.decision_function(df)
        return scores    
