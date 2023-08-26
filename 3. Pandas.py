import pandas as pd
# Access a file:
df = pd.read_csv("weather_data.csv")        # access all deta from this fiel

# Access row and column:
r , c = df.shape        # df.shape --> row and comolmn

# Head and tail:
df.head(2)      # 1st 2 row
df.tail(2)      # last 2 row

# Specific row access with index:
df[1:3]         # row index 1 -3
df[:3]          # row index start -3
df[2:]          # row index 2 - end

# Column:
df.columns      # all columns

# Specific column access:
df.day          # access day column
df["day"]       # access day column

# Type:
type(df["day"]) # pandas.core.series.series

# Access specific column:
df[['day','temperature']]       # access 2 column

# Operation on DataFrame:
df['temperature'].max()         # return max vlaue of temperature column
x = df[df["temperature"] > 32]  # conditon apply
df['day'][df['temperature'] == df['temperature'].max()] 
                                # pritns the day when your temperature is maximum
x = df[['day' , 'temperature']][df['temperature'] == df['temperature'].max()] 
print(x)                        # print day along with temperature when temp max

# index: (you can set any column as index)
df.index            # index 0 - 6 and step 1
df.set_index('day') # set index day column
df.set_index('day', inplace=True)   # set index not 0 - 6. it set date index
print(df)
df.reset_index(inplace=True)        # reset this indeing   


 


                # ***** Different ways of creationg dataFrame *****
# Using CSV:
csv = pd.read_csv("exel.csv")       # read csv file into csv variable

# Using Exel:
exel = pd.read_excel("exel.xlsx")   # read exel file into exel variable

# Using python dictionary:
weather_data = {
     'day': ['1/1/2017', '1/2/2017', '1/3/2017'],
     'temperature': [32, 35,28],
     'windspeed': [6,7,2],
     'event': ['Rain', 'Sunny', 'Snow']
}
dictionary = pd.DataFrame(weather_data)     # read dictionary as dataFrame into dictionary variable

# Using tuple list:
weather_data = [
     ('1/1/2017', 32, 6, 'Rain'),
     ('1/2/2017', 35, 7, 'Sunny'),
     ('1/3/2017', 28, 2, 'Snow')
]
tuple_data = pd.DataFrame(weather_data , columns=["day" , "temp" , "windspeed" , "event"])
                        # crating a dataFram with tuple list

# List dictionary:
weather_data = [
    {'day': '1/1/2017', 'temperature': 32, 'windspeed': 6, 'event': 'Rain'},
    {'day': '1/2/2017', 'temperature': 35, 'windspeed' : 7, 'event': 'Sunny'},
    {'day': '1/3/2017', 'temperature': 28, 'windspeed': 2, 'event': 'Snow'},
 ]
dictionary = pd.DataFrame(weather_data)     # creating dictionary list dataFrame


 


                # ***** Reading and witing cvs and exel file *****
                
# Read from csv file:

df = pd.read_csv("stock_data.csv" , skiprows=1)     # import all contant into df and skip 1st row for (skiprows = 1)
df = pd.read_csv("stock_data.csv" , header=1)       # import all contant into df and skip 1st row for (header = 1)
df = pd.read_csv("stock_data.csv" , header=None)    # header will indexd with start 0
df = pd.read_csv("stock_data.csv" , header=None ,  names=["tikers" , "eps" , "revenue" , "price" ])   
    # replace header index with this

# Read specific number of rows:
df = pd.read_csv("stock_data.csv" , nrows=3)        # first 3 rows excluding your headers

# NaN values:
df = pd.read_csv("stock_data.csv" , na_values=["not available" , "n.a."])      
        # in will replace "not available" and "n.a. " text to [NaN]

df = pd.read_csv("stock_data.csv" , na_values={     # set specific column NaN values
    "esp" : ["not available" , "n.a. " ],
    "revenue" : ["not available" , "n.a. " , -1] ,
    "people" : ["not availabele" , "n.a. "]
})

# Write into csv file:
df.to_csv("new.csv")                # create a new.csv file
df.to_csv("new.csv" , index=False)  # create a new.csv file without row index
df.to_csv("new.csv" , columns=["eps" , "price"])
                                    # create a new.csv file with 2 column
                                    # header = False --> skip header when create

# Read from exel file:
df = pd.read_excel("stock_data.xlsx" ,"Sheet1")     # onpen Sheet1 form this exel file

# Using converters:

def convert_people(cell):       # this is a demo function
    if cell == "n.a.":
        return "Unkonwn People"
    else:
        return cell
    
df = pd.read_excel("stock_data.xlsx" , "Sheet1" , converters={
    "people" : convert_people   # using a function for convert people row data 
})

# Write into exel file:
df.to_excel("new.xlsx" , sheet_name="stock")    # create a new.xlsx file 
df.to_excel("new.xlsx" , sheet_name="stock" , startrow=4 , startcol=5)
                                                # start with 4 rows and 5 column
# Dealing with 2 data freame
df_stocks = pd.DataFrame({
'tickers': ['GOOGL', 'WMT', 'MSFT'],
'price': [845, 65, 64 ],
'pe':[30.37, 14.26, 30.97],
'eps': [27.82, 4.61, 2.12]
})

df_weather = pd.DataFrame({
'day': ['1/1/2017','1/2/2017' ,'1/3/2017'],     
'temperature': [32, 35, 28],
'event': ['Rain', 'Sunny', 'Snow']
})
print(df)

with pd.ExcelWriter('stocks_weather.xlsx') as writer:
    df_stocks.to_excel(writer, sheet_name="stocks")
    df_weather.to_excel(writer, sheet_name="weather" )





                # ***** Missing data handaling *****

# fillna():
df = pd.read_csv("data.csv" , parse_dates=["day"])      # replace day column to date
new_df = df.fillna(0)       # all NaN value will replace with 0
new_df = df.fillna({
    "temperature" : 0,      # replace NaN vlaues in individual column with individual values
    "windspeed" : 0 ,
    "event" : "no event"
})
new_df = df.fillna(method="ffill")      # ffill --> forword fill it will replace NaN values with previous row values
new_df = df.fillna(method="bfill")      # bfill --> Back fill it will replace NaN values with Next row values
new_df = df.fillna(method="bfill" , axis="columns")      # bfill --> Back fill it will replace NaN values with Next column values
new_df = df.fillna(method="ffill" , limit=1)      # forword fill 1 times for every values

# interpolate():
df = pd.read_csv("data.csv")   
new_df = df.interpolate()               # Replace NULL values with the number of middle values of between the previous and next row
# method("time")        --> will consider the time while insert NaN values

# dropna():
new_df = df.dropna()                # it will drop all NaN value row
new_df = df.dropna(how="all")       # when all values are NaN only this row will drop
new_df = df.dropna(thresh=2)        # If i have at list 1 valid values keep the row

# Date_range():
n_df = pd.read_csv("data.csv" , parse_dates=["day"])
dt = pd.date_range("01-01-2017" , "01-11-2017")
index = pd.DatetimeIndex(dt)
n_df = n_df.reindex(index)
print(n_df)                               





                    # ***** Handaling Missing data *****
import numpy as np
df = pd.read_csv("weather.csv")

# Replace data:
new_df = df.replace([-99999] , np.nan)    # replace -99999 with NaN ---> [value list] , replce value

# Replace bashed on column:
new_df = df.replace({
    "temperature" : -99999,     # column wise replace 
    "windspeed" : -99999,
    "event" : "0"
} , np.nan)

# Replace beshed on value:
new_df = df.replace({           # value wise replace
    -99999 : np.nan,
    "0" : "Zero"
})

# Replace with regex:
new_df = df.replace({
    "temperature" : "[A-Za-z]",
    "windspeed" : "[A-Za-z]"
},"" , regex=True) 
print(new_df)

# Replace the list of values to another list of values:
df = pd.DataFrame({
'score': ['exceptional','average', 'good', 'poor', 'average', 'exceptional'],
'student': ['rob', 'maya', 'parthiv', 'tom', 'julian', 'erica']
})
new_df = df.replace(["poor" , "average" , "good" , "exceptional"] , [1, 2, 3,4]) # replace 1 list to another 





                    # ***** Pandas group by data *****
# Data Frame groupby:
df = pd.read_csv("weather_by_cities.csv")
g = df.groupby("city")          # dataframe groupby object
for i , j in g:
    print(i)        # i is city name
    print(j)        # j is data frame
mumbai = g.get_group("mumbai")  # mumbai data frame is hare
g.max()                         # new datafeame with max value
g.mean()                        # mean of 3 data set will come hare a new dataset
g.describe()                    # describe many things of 3 different dataframe



                    # ***** Pandas concat ******
# Concatinate: 

india_weather = pd.DataFrame({
    "city" : ["mombai" , "dehli" , "banglore"] ,
    "temp" : [32 , 45 , 30],
    "humidity" : [80 , 60 , 78]
})
usa_weather = pd.DataFrame({
    "city" : ["new york" , "chicago" , "orlando"] ,
    "temp" : [21 , 14 , 35],
    "humidity" : [68 , 65 , 75] 
})

df = pd.concat([india_weather , usa_weather])   # concat these two data frame 
df = pd.concat([india_weather , usa_weather] , ignore_index=True)   # will ignore index , default is False
df = pd.concat([india_weather , usa_weather] , keys=["India" , "USA"])   # will create adition index ["India" , "USA"]

india = df.loc["India"]     # access India indexed data frame

# Concar another axis:
temp_df = pd.DataFrame({
    "city" : ["mombai" , "dehli" , "banglore"] ,
    "temp" : [34 , 53 , 43]
})
wind_df = pd.DataFrame({
    "city" : ["new york" , "chicago" , "orlando"] ,
    "temp" : [31 , 24 , 25]
})
df = pd.concat([temp_df , wind_df] , axis=1)     # default axis is 0

# Indexing wiht concat:

temp_df = pd.DataFrame({
    "city" : ["mombai" , "dehli" , "banglore"] ,
    "temp" : [34 , 53 , 43]
},index=[0, 1, 2])              # defining index 
 
wind_df = pd.DataFrame({
    "city" : ["delhi" , "mombai"] ,
    "temp" : [31 , 24 ]
},index=[1 , 0])                # defining index

df = pd.concat([temp_df , wind_df] , axis=1)

# Join dataframe with series():
s = pd.Series(["Humid" , "Dry" , "Rani"] , name="Event")

temp_df = pd.DataFrame({
    "city" : ["mombai" , "dehli" , "banglore"] ,
    "temp" : [34 , 53 , 43]
},index=[0, 1, 2])

new = pd.concat([temp_df , s] , axis=1)     # append new datafreame into temp_df




                    # **** Marge Dataframe
df1 = pd.DataFrame({
    "city" : ["new york" , "chicago" , "orlando"] ,
    "temp" : [34 , 53 , 43]                   
})             
df2 = pd.DataFrame({
    "city" : ["new york" , "chicago" , "orlando"] ,
    "humidity" : [64 , 68 , 75]                   
})             

# Using marge():
df3 = pd.merge(df1 , df2 , on="city")

df1 = pd.DataFrame({
    "city" : ["new york" , "chicago" , "dhaka"] ,
    "temp" : [34 , 53 , 43]                   
})             
df2 = pd.DataFrame({
    "city" : ["new york" , "chicago" , "orlando"] ,
    "humidity" : [64 , 68 , 75]                   
})  
df3 = pd.merge(df1 , df2 , on="city")   # different city will ignore . it is semilar to set theory
df3 = pd.merge(df1 , df2 , on="city" , how="outer")     # like as union set and inner jion is default
df3 = pd.merge(df1 , df2 , on="city" , how="left")      #  take onley left varible city
df3 = pd.merge(df1 , df2 , on="city" , how="outer" , indicator=True)       #  show marge indicator like left_only , both , right_only

# suffixes:

df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando", "baltimore"],
    "temperature": [21,14,35,38],
    "humidity": [65,68,71, 75]
})

df2 = pd.DataFrame({
    "city": ["chicago","new york","san diego"],
    "temperature": [21,14,35],
    "humidity": [65,68,71]
})

df3 = pd.merge(df1 , df2 , on="city")       # it will append suffixes into header
df3 = pd.merge(df1 , df2 , on="city" , suffixes=("_left" , "_right"))       # create own suffixes






                # ***** pivot and pivot tabel *****
# pivot allaws you to reshape and tranform your data
df = pd.read_csv("pivot_weather.csv")
n_df = df.pivot(index="date" , columns="city")  # tranform as index date and city column
n_df = df.pivot(index="date" , columns="city" , values="humidity")  # print only humidity

# pivot tabel:
# pivot table is used to sammarize ang aggregate data inside dataframe
new_df = df.pivot_table(index="city" , columns="date")  # create a new table
new_df = df.pivot_table(index="city" , columns="date" ,aggfunc=sum)  
new_df = df.pivot_table(index="city" , columns="date" ,aggfunc=sum , margins=True)  

# Use grouper function to aggregate:

df["date"] = pd.to_datetime(df["date"])
x = df.pivot_table(index=pd.Grouper(freq="M" , key="date") , columns="city")    # default is average

print(x)
