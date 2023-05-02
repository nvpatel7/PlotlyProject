#importing pandas and plotly
import pandas as pd
import plotly.express as px

#reading the csv file
df = pd.read_csv('./NYPD_Arrests_Data__Historic_.csv')

#changing the date format of the arrest date column to be able to group by year
df["ARREST_DATE"] = pd.to_datetime(df["ARREST_DATE"], format="%m/%d/%Y")

#create a new column for the year and month so we can make it easier to group by
df['year'] = df["ARREST_DATE"].dt.year
df['Month'] = df["ARREST_DATE"].dt.month_name()

#sorting the month columns since default sort is alphabetical order
df['Month'] = pd.Categorical(df['Month'], 
    categories=['January', 'February', 'March', 'April', 'May', 'June', 
                'July', 'August', 'September', 'October', 'November', 'December'])
df = df.sort_values("Month")

#creating the new dataframe with the count of arrests 
#per month for every year in the original dataframe and resetting the index
year_month = df.groupby(['year', 'Month']).size().reset_index(name='Arrests')


#creating the line graph
fig = px.line(year_month, x = 'Month', y = 'Arrests', color = 'year', markers = True,
              title = 'Arrests per Month in New York City Between 2006 and 2021')

#updating the layout of the graph
fig.update_layout(
    font = {
        'family': 'Open Sans, monospace',
        'color': '#000000',
        'size': 12
    },
    title = {
        'font': dict(size = 25, color = '#000000', 
                     family = 'Open Sans, monospace'),
        'x': 0.5,
        'y': 0.95,
        'xanchor': 'center',
        'yanchor': 'top',
    }
)

fig.show()

