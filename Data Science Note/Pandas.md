# Pandas for Data Science


```python
import pandas as pd
```

## Access a file :


```python
df = pd.read_csv("weather_data.csv")        # access all deta from this fiel
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2017</td>
      <td>32.0</td>
      <td>6.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/4/2017</td>
      <td>NaN</td>
      <td>9.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/5/2017</td>
      <td>28.0</td>
      <td>NaN</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/6/2017</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1/7/2017</td>
      <td>32.0</td>
      <td>NaN</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1/8/2017</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1/9/2017</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1/10/2017</td>
      <td>34.0</td>
      <td>8.0</td>
      <td>Cloudy</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1/11/2017</td>
      <td>40.0</td>
      <td>12.0</td>
      <td>Sunny</td>
    </tr>
  </tbody>
</table>
</div>



## Access row and column :


```python
r , c = df.shape        # df.shape --> row and comolmn
```

## Head and tail :


```python
df.head(2)      # 1st 2 row
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2017</td>
      <td>32.0</td>
      <td>6.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/4/2017</td>
      <td>NaN</td>
      <td>9.0</td>
      <td>Sunny</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.tail(2)      # last 2 row
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>1/10/2017</td>
      <td>34.0</td>
      <td>8.0</td>
      <td>Cloudy</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1/11/2017</td>
      <td>40.0</td>
      <td>12.0</td>
      <td>Sunny</td>
    </tr>
  </tbody>
</table>
</div>



## Specific row access with index:


```python
df[1:3]         # row index 1 -3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>1/4/2017</td>
      <td>NaN</td>
      <td>9.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/5/2017</td>
      <td>28.0</td>
      <td>NaN</td>
      <td>Snow</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[:3]          # row index start -3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2017</td>
      <td>32.0</td>
      <td>6.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/4/2017</td>
      <td>NaN</td>
      <td>9.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/5/2017</td>
      <td>28.0</td>
      <td>NaN</td>
      <td>Snow</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[2:]          # row index 2 - end
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>1/5/2017</td>
      <td>28.0</td>
      <td>NaN</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/6/2017</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1/7/2017</td>
      <td>32.0</td>
      <td>NaN</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1/8/2017</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1/9/2017</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1/10/2017</td>
      <td>34.0</td>
      <td>8.0</td>
      <td>Cloudy</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1/11/2017</td>
      <td>40.0</td>
      <td>12.0</td>
      <td>Sunny</td>
    </tr>
  </tbody>
</table>
</div>



## Column :


```python
df.columns      # all columns
```




    Index(['day', 'temperature', 'windspeed', 'event'], dtype='object')



## Specific column access:


```python
df.day          # access day column
```




    0     1/1/2017
    1     1/4/2017
    2     1/5/2017
    3     1/6/2017
    4     1/7/2017
    5     1/8/2017
    6     1/9/2017
    7    1/10/2017
    8    1/11/2017
    Name: day, dtype: object




```python
df["day"]       # access day column
```




    0     1/1/2017
    1     1/4/2017
    2     1/5/2017
    3     1/6/2017
    4     1/7/2017
    5     1/8/2017
    6     1/9/2017
    7    1/10/2017
    8    1/11/2017
    Name: day, dtype: object



## Type:


```python
type(df["day"]) # pandas.core.series.series
```




    pandas.core.series.Series



## Access specific column:


```python
df[['day','temperature']]       # access 2 column
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temperature</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2017</td>
      <td>32.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/4/2017</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/5/2017</td>
      <td>28.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/6/2017</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1/7/2017</td>
      <td>32.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1/8/2017</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1/9/2017</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1/10/2017</td>
      <td>34.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1/11/2017</td>
      <td>40.0</td>
    </tr>
  </tbody>
</table>
</div>



## Operation on DataFrame:


```python
df['temperature'].max()         # return max vlaue of temperature column
```




    40.0




```python
x = df[df["temperature"] > 32]  # conditon apply
df['day'][df['temperature'] == df['temperature'].max()] 
                                # pritns the day when your temperature is maximum
```




    8    1/11/2017
    Name: day, dtype: object




```python
x = df[['day' , 'temperature']][df['temperature'] == df['temperature'].max()] 
print(x)                        # print day along with temperature when temp max
```

             day  temperature
    8  1/11/2017         40.0


## index: (you can set any column as index)


```python
df.index            # index 0 - 6 and step 1
```




    RangeIndex(start=0, stop=9, step=1)




```python
df.set_index('day') # set index day column 
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
    <tr>
      <th>day</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1/1/2017</th>
      <td>32.0</td>
      <td>6.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1/4/2017</th>
      <td>NaN</td>
      <td>9.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>1/5/2017</th>
      <td>28.0</td>
      <td>NaN</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>1/6/2017</th>
      <td>NaN</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1/7/2017</th>
      <td>32.0</td>
      <td>NaN</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1/8/2017</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>1/9/2017</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1/10/2017</th>
      <td>34.0</td>
      <td>8.0</td>
      <td>Cloudy</td>
    </tr>
    <tr>
      <th>1/11/2017</th>
      <td>40.0</td>
      <td>12.0</td>
      <td>Sunny</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.set_index('day', inplace=True)   # set index not 0 - 6. it set date index
print(df)
```

               temperature  windspeed   event
    day                                      
    1/1/2017          32.0        6.0    Rain
    1/4/2017           NaN        9.0   Sunny
    1/5/2017          28.0        NaN    Snow
    1/6/2017           NaN        7.0     NaN
    1/7/2017          32.0        NaN    Rain
    1/8/2017           NaN        NaN   Sunny
    1/9/2017           NaN        NaN     NaN
    1/10/2017         34.0        8.0  Cloudy
    1/11/2017         40.0       12.0   Sunny



```python
df.reset_index(inplace=True)        # reset this indeing  
```

# Different ways of creationg dataFrame

## Using CSV:


```python
csv = pd.read_csv("exel.csv")       # read csv file into csv variable
```

## Using Exel:


```python
exel = pd.read_excel("exel.xlsx")   # read exel file into exel variable
```

## Using python dictionary:


```python
weather_data = {
     'day': ['1/1/2017', '1/2/2017', '1/3/2017'],
     'temperature': [32, 35,28],
     'windspeed': [6,7,2],
     'event': ['Rain', 'Sunny', 'Snow']
}
dictionary = pd.DataFrame(weather_data)     # read dictionary as dataFrame into dictionary variable
dictionary
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2017</td>
      <td>32</td>
      <td>6</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/2/2017</td>
      <td>35</td>
      <td>7</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/3/2017</td>
      <td>28</td>
      <td>2</td>
      <td>Snow</td>
    </tr>
  </tbody>
</table>
</div>



## Using tuple list:


```python
weather_data = [
     ('1/1/2017', 32, 6, 'Rain'),
     ('1/2/2017', 35, 7, 'Sunny'),
     ('1/3/2017', 28, 2, 'Snow')
]
tuple_data = pd.DataFrame(weather_data , columns=["day" , "temp" , "windspeed" , "event"])
tuple_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temp</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2017</td>
      <td>32</td>
      <td>6</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/2/2017</td>
      <td>35</td>
      <td>7</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/3/2017</td>
      <td>28</td>
      <td>2</td>
      <td>Snow</td>
    </tr>
  </tbody>
</table>
</div>



## List dictionary:


```python
weather_data = [
    {'day': '1/1/2017', 'temperature': 32, 'windspeed': 6, 'event': 'Rain'},
    {'day': '1/2/2017', 'temperature': 35, 'windspeed' : 7, 'event': 'Sunny'},
    {'day': '1/3/2017', 'temperature': 28, 'windspeed': 2, 'event': 'Snow'},
 ]
dictionary = pd.DataFrame(weather_data)     # creating dictionary list dataFrame
dictionary
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2017</td>
      <td>32</td>
      <td>6</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/2/2017</td>
      <td>35</td>
      <td>7</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/3/2017</td>
      <td>28</td>
      <td>2</td>
      <td>Snow</td>
    </tr>
  </tbody>
</table>
</div>



# Reading and witing cvs and exel file

## Read from csv file:


```python
df = pd.read_csv("stock_data.csv" , skiprows=1)     # import all contant into df and skip 1st row for (skiprows = 1)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>GOOGL</th>
      <th>27.82</th>
      <th>87</th>
      <th>845</th>
      <th>larry page</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>WMT</td>
      <td>4.61</td>
      <td>484</td>
      <td>65</td>
      <td>n.a.</td>
    </tr>
    <tr>
      <th>1</th>
      <td>MSFT</td>
      <td>-1</td>
      <td>85</td>
      <td>64</td>
      <td>bill gates</td>
    </tr>
    <tr>
      <th>2</th>
      <td>RIL</td>
      <td>not available</td>
      <td>50</td>
      <td>1023</td>
      <td>mukesh ambani</td>
    </tr>
    <tr>
      <th>3</th>
      <td>TATA</td>
      <td>5.6</td>
      <td>-1</td>
      <td>n.a.</td>
      <td>ratan tata</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.read_csv("stock_data.csv" , header=1)       # import all contant into df and skip 1st row for (header = 1)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>GOOGL</th>
      <th>27.82</th>
      <th>87</th>
      <th>845</th>
      <th>larry page</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>WMT</td>
      <td>4.61</td>
      <td>484</td>
      <td>65</td>
      <td>n.a.</td>
    </tr>
    <tr>
      <th>1</th>
      <td>MSFT</td>
      <td>-1</td>
      <td>85</td>
      <td>64</td>
      <td>bill gates</td>
    </tr>
    <tr>
      <th>2</th>
      <td>RIL</td>
      <td>not available</td>
      <td>50</td>
      <td>1023</td>
      <td>mukesh ambani</td>
    </tr>
    <tr>
      <th>3</th>
      <td>TATA</td>
      <td>5.6</td>
      <td>-1</td>
      <td>n.a.</td>
      <td>ratan tata</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.read_csv("stock_data.csv" , header=None)    # header will indexd with start 0
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>tickers</td>
      <td>eps</td>
      <td>revenue</td>
      <td>price</td>
      <td>people</td>
    </tr>
    <tr>
      <th>1</th>
      <td>GOOGL</td>
      <td>27.82</td>
      <td>87</td>
      <td>845</td>
      <td>larry page</td>
    </tr>
    <tr>
      <th>2</th>
      <td>WMT</td>
      <td>4.61</td>
      <td>484</td>
      <td>65</td>
      <td>n.a.</td>
    </tr>
    <tr>
      <th>3</th>
      <td>MSFT</td>
      <td>-1</td>
      <td>85</td>
      <td>64</td>
      <td>bill gates</td>
    </tr>
    <tr>
      <th>4</th>
      <td>RIL</td>
      <td>not available</td>
      <td>50</td>
      <td>1023</td>
      <td>mukesh ambani</td>
    </tr>
    <tr>
      <th>5</th>
      <td>TATA</td>
      <td>5.6</td>
      <td>-1</td>
      <td>n.a.</td>
      <td>ratan tata</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.read_csv("stock_data.csv" , header=None ,  names=["tikers" , "eps" , "revenue" , "price" ])   
# replace header index with this
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tikers</th>
      <th>eps</th>
      <th>revenue</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>tickers</th>
      <td>eps</td>
      <td>revenue</td>
      <td>price</td>
      <td>people</td>
    </tr>
    <tr>
      <th>GOOGL</th>
      <td>27.82</td>
      <td>87</td>
      <td>845</td>
      <td>larry page</td>
    </tr>
    <tr>
      <th>WMT</th>
      <td>4.61</td>
      <td>484</td>
      <td>65</td>
      <td>n.a.</td>
    </tr>
    <tr>
      <th>MSFT</th>
      <td>-1</td>
      <td>85</td>
      <td>64</td>
      <td>bill gates</td>
    </tr>
    <tr>
      <th>RIL</th>
      <td>not available</td>
      <td>50</td>
      <td>1023</td>
      <td>mukesh ambani</td>
    </tr>
    <tr>
      <th>TATA</th>
      <td>5.6</td>
      <td>-1</td>
      <td>n.a.</td>
      <td>ratan tata</td>
    </tr>
  </tbody>
</table>
</div>



## Read specific number of rows:


```python
df = pd.read_csv("stock_data.csv" , nrows=3)        # first 3 rows excluding your headers
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tickers</th>
      <th>eps</th>
      <th>revenue</th>
      <th>price</th>
      <th>people</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>GOOGL</td>
      <td>27.82</td>
      <td>87</td>
      <td>845</td>
      <td>larry page</td>
    </tr>
    <tr>
      <th>1</th>
      <td>WMT</td>
      <td>4.61</td>
      <td>484</td>
      <td>65</td>
      <td>n.a.</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MSFT</td>
      <td>-1.00</td>
      <td>85</td>
      <td>64</td>
      <td>bill gates</td>
    </tr>
  </tbody>
</table>
</div>



## NaN values:


```python
df = pd.read_csv("stock_data.csv" , na_values=["not available" , "n.a."])      
# in will replace "not available" and "n.a. " text to [NaN]
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tickers</th>
      <th>eps</th>
      <th>revenue</th>
      <th>price</th>
      <th>people</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>GOOGL</td>
      <td>27.82</td>
      <td>87</td>
      <td>845.0</td>
      <td>larry page</td>
    </tr>
    <tr>
      <th>1</th>
      <td>WMT</td>
      <td>4.61</td>
      <td>484</td>
      <td>65.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MSFT</td>
      <td>-1.00</td>
      <td>85</td>
      <td>64.0</td>
      <td>bill gates</td>
    </tr>
    <tr>
      <th>3</th>
      <td>RIL</td>
      <td>NaN</td>
      <td>50</td>
      <td>1023.0</td>
      <td>mukesh ambani</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TATA</td>
      <td>5.60</td>
      <td>-1</td>
      <td>NaN</td>
      <td>ratan tata</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.read_csv("stock_data.csv" , na_values={     # set specific column NaN values
    "esp" : ["not available" , "n.a. " ],
    "revenue" : ["not available" , "n.a. " , -1] ,
    "people" : ["not availabele" , "n.a. "]
})
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tickers</th>
      <th>eps</th>
      <th>revenue</th>
      <th>price</th>
      <th>people</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>GOOGL</td>
      <td>27.82</td>
      <td>87.0</td>
      <td>845</td>
      <td>larry page</td>
    </tr>
    <tr>
      <th>1</th>
      <td>WMT</td>
      <td>4.61</td>
      <td>484.0</td>
      <td>65</td>
      <td>n.a.</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MSFT</td>
      <td>-1</td>
      <td>85.0</td>
      <td>64</td>
      <td>bill gates</td>
    </tr>
    <tr>
      <th>3</th>
      <td>RIL</td>
      <td>not available</td>
      <td>50.0</td>
      <td>1023</td>
      <td>mukesh ambani</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TATA</td>
      <td>5.6</td>
      <td>NaN</td>
      <td>n.a.</td>
      <td>ratan tata</td>
    </tr>
  </tbody>
</table>
</div>



## Write into csv file:


```python
df.to_csv("new.csv")                # create a new.csv file
df.to_csv("new.csv" , index=False)  # create a new.csv file without row index
df.to_csv("new.csv" , columns=["eps" , "price"])
                                    # create a new.csv file with 2 column
                                    # header = False --> skip header when create
```

## Read from exel file:


```python
df = pd.read_excel("stock_data.xlsx" ,"Sheet1")     # onpen Sheet1 form this exel file
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tickers</th>
      <th>eps</th>
      <th>revenue</th>
      <th>price</th>
      <th>people</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>GOOGL</td>
      <td>27.82</td>
      <td>87</td>
      <td>845</td>
      <td>larry page</td>
    </tr>
    <tr>
      <th>1</th>
      <td>WMT</td>
      <td>4.61</td>
      <td>484</td>
      <td>65</td>
      <td>n.a.</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MSFT</td>
      <td>-1</td>
      <td>85</td>
      <td>64</td>
      <td>bill gates</td>
    </tr>
    <tr>
      <th>3</th>
      <td>RIL</td>
      <td>not available</td>
      <td>50</td>
      <td>1023</td>
      <td>mukesh ambani</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TATA</td>
      <td>5.6</td>
      <td>-1</td>
      <td>n.a.</td>
      <td>ratan tata</td>
    </tr>
  </tbody>
</table>
</div>



## Using converters:


```python
def convert_people(cell):       # this is a demo function
    if cell == "n.a.":
        return "Unkonwn People"
    else:
        return cell
    
df = pd.read_excel("stock_data.xlsx" , "Sheet1" , converters={
    "people" : convert_people   # using a function for convert people row data 
})
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tickers</th>
      <th>eps</th>
      <th>revenue</th>
      <th>price</th>
      <th>people</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>GOOGL</td>
      <td>27.82</td>
      <td>87</td>
      <td>845</td>
      <td>larry page</td>
    </tr>
    <tr>
      <th>1</th>
      <td>WMT</td>
      <td>4.61</td>
      <td>484</td>
      <td>65</td>
      <td>Unkonwn People</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MSFT</td>
      <td>-1</td>
      <td>85</td>
      <td>64</td>
      <td>bill gates</td>
    </tr>
    <tr>
      <th>3</th>
      <td>RIL</td>
      <td>not available</td>
      <td>50</td>
      <td>1023</td>
      <td>mukesh ambani</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TATA</td>
      <td>5.6</td>
      <td>-1</td>
      <td>n.a.</td>
      <td>ratan tata</td>
    </tr>
  </tbody>
</table>
</div>



## Write into exel file:


```python
df.to_excel("new.xlsx" , sheet_name="stock")    # create a new.xlsx file 
df.to_excel("new.xlsx" , sheet_name="stock" , startrow=4 , startcol=5)
                                                # start with 4 rows and 5 column
```

## Dealing with 2 data freame


```python
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
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tickers</th>
      <th>eps</th>
      <th>revenue</th>
      <th>price</th>
      <th>people</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>GOOGL</td>
      <td>27.82</td>
      <td>87</td>
      <td>845</td>
      <td>larry page</td>
    </tr>
    <tr>
      <th>1</th>
      <td>WMT</td>
      <td>4.61</td>
      <td>484</td>
      <td>65</td>
      <td>Unkonwn People</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MSFT</td>
      <td>-1</td>
      <td>85</td>
      <td>64</td>
      <td>bill gates</td>
    </tr>
    <tr>
      <th>3</th>
      <td>RIL</td>
      <td>not available</td>
      <td>50</td>
      <td>1023</td>
      <td>mukesh ambani</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TATA</td>
      <td>5.6</td>
      <td>-1</td>
      <td>n.a.</td>
      <td>ratan tata</td>
    </tr>
  </tbody>
</table>
</div>




```python
with pd.ExcelWriter('stocks_weather.xlsx') as writer:
    df_stocks.to_excel(writer, sheet_name="stocks")
    df_weather.to_excel(writer, sheet_name="weather" )
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tickers</th>
      <th>eps</th>
      <th>revenue</th>
      <th>price</th>
      <th>people</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>GOOGL</td>
      <td>27.82</td>
      <td>87</td>
      <td>845</td>
      <td>larry page</td>
    </tr>
    <tr>
      <th>1</th>
      <td>WMT</td>
      <td>4.61</td>
      <td>484</td>
      <td>65</td>
      <td>Unkonwn People</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MSFT</td>
      <td>-1</td>
      <td>85</td>
      <td>64</td>
      <td>bill gates</td>
    </tr>
    <tr>
      <th>3</th>
      <td>RIL</td>
      <td>not available</td>
      <td>50</td>
      <td>1023</td>
      <td>mukesh ambani</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TATA</td>
      <td>5.6</td>
      <td>-1</td>
      <td>n.a.</td>
      <td>ratan tata</td>
    </tr>
  </tbody>
</table>
</div>



# Missing data handaling 

## fillna():


```python
df = pd.read_csv("data.csv" , parse_dates=["day"])      # replace day column to date
new_df = df.fillna(0)       # all NaN value will replace with 0
new_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2017-01-01</td>
      <td>32.0</td>
      <td>6.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2017-01-04</td>
      <td>0.0</td>
      <td>9.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2017-01-05</td>
      <td>28.0</td>
      <td>0.0</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2017-01-06</td>
      <td>0.0</td>
      <td>7.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2017-01-07</td>
      <td>32.0</td>
      <td>0.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2017-01-08</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2017-01-09</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2017-01-10</td>
      <td>34.0</td>
      <td>8.0</td>
      <td>Cloudy</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2017-01-11</td>
      <td>40.0</td>
      <td>12.0</td>
      <td>Sunny</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_df = df.fillna({
    "temperature" : 0,      # replace NaN vlaues in individual column with individual values
    "windspeed" : 0 ,
    "event" : "no event"
})
new_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2017-01-01</td>
      <td>32.0</td>
      <td>6.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2017-01-04</td>
      <td>0.0</td>
      <td>9.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2017-01-05</td>
      <td>28.0</td>
      <td>0.0</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2017-01-06</td>
      <td>0.0</td>
      <td>7.0</td>
      <td>no event</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2017-01-07</td>
      <td>32.0</td>
      <td>0.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2017-01-08</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2017-01-09</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>no event</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2017-01-10</td>
      <td>34.0</td>
      <td>8.0</td>
      <td>Cloudy</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2017-01-11</td>
      <td>40.0</td>
      <td>12.0</td>
      <td>Sunny</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_df = df.fillna(method="ffill")      # ffill --> forword fill it will replace NaN values with previous row values
new_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2017-01-01</td>
      <td>32.0</td>
      <td>6.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2017-01-04</td>
      <td>32.0</td>
      <td>9.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2017-01-05</td>
      <td>28.0</td>
      <td>9.0</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2017-01-06</td>
      <td>28.0</td>
      <td>7.0</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2017-01-07</td>
      <td>32.0</td>
      <td>7.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2017-01-08</td>
      <td>32.0</td>
      <td>7.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2017-01-09</td>
      <td>32.0</td>
      <td>7.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2017-01-10</td>
      <td>34.0</td>
      <td>8.0</td>
      <td>Cloudy</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2017-01-11</td>
      <td>40.0</td>
      <td>12.0</td>
      <td>Sunny</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_df = df.fillna(method="bfill")      # bfill --> Back fill it will replace NaN values with Next row values
new_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2017-01-01</td>
      <td>32.0</td>
      <td>6.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2017-01-04</td>
      <td>28.0</td>
      <td>9.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2017-01-05</td>
      <td>28.0</td>
      <td>7.0</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2017-01-06</td>
      <td>32.0</td>
      <td>7.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2017-01-07</td>
      <td>32.0</td>
      <td>8.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2017-01-08</td>
      <td>34.0</td>
      <td>8.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2017-01-09</td>
      <td>34.0</td>
      <td>8.0</td>
      <td>Cloudy</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2017-01-10</td>
      <td>34.0</td>
      <td>8.0</td>
      <td>Cloudy</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2017-01-11</td>
      <td>40.0</td>
      <td>12.0</td>
      <td>Sunny</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_df = df.fillna(method="bfill" , axis="columns")      # bfill --> Back fill it will replace NaN values with Next column values
new_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2017-01-01</td>
      <td>32.0</td>
      <td>6.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2017-01-04</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2017-01-05</td>
      <td>28.0</td>
      <td>Snow</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2017-01-06</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2017-01-07</td>
      <td>32.0</td>
      <td>Rain</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2017-01-08</td>
      <td>Sunny</td>
      <td>Sunny</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2017-01-09</td>
      <td>NaT</td>
      <td>NaT</td>
      <td>NaT</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2017-01-10</td>
      <td>34.0</td>
      <td>8.0</td>
      <td>Cloudy</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2017-01-11</td>
      <td>40.0</td>
      <td>12.0</td>
      <td>Sunny</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_df = df.fillna(method="ffill" , limit=1)      # forword fill 1 times for every values
new_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2017-01-01</td>
      <td>32.0</td>
      <td>6.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2017-01-04</td>
      <td>32.0</td>
      <td>9.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2017-01-05</td>
      <td>28.0</td>
      <td>9.0</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2017-01-06</td>
      <td>28.0</td>
      <td>7.0</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2017-01-07</td>
      <td>32.0</td>
      <td>7.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2017-01-08</td>
      <td>32.0</td>
      <td>NaN</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2017-01-09</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2017-01-10</td>
      <td>34.0</td>
      <td>8.0</td>
      <td>Cloudy</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2017-01-11</td>
      <td>40.0</td>
      <td>12.0</td>
      <td>Sunny</td>
    </tr>
  </tbody>
</table>
</div>



## interpolate():


```python
df = pd.read_csv("data.csv")   
new_df = df.interpolate() # Replace NULL values with the number of middle values of between the previous and next row
new_df
# method("time")        --> will consider the time while insert NaN values
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2017</td>
      <td>32.000000</td>
      <td>6.00</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/4/2017</td>
      <td>30.000000</td>
      <td>9.00</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/5/2017</td>
      <td>28.000000</td>
      <td>8.00</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/6/2017</td>
      <td>30.000000</td>
      <td>7.00</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1/7/2017</td>
      <td>32.000000</td>
      <td>7.25</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1/8/2017</td>
      <td>32.666667</td>
      <td>7.50</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1/9/2017</td>
      <td>33.333333</td>
      <td>7.75</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1/10/2017</td>
      <td>34.000000</td>
      <td>8.00</td>
      <td>Cloudy</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1/11/2017</td>
      <td>40.000000</td>
      <td>12.00</td>
      <td>Sunny</td>
    </tr>
  </tbody>
</table>
</div>



## dropna():


```python
new_df = df.dropna()                # it will drop all NaN value row
new_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2017</td>
      <td>32.0</td>
      <td>6.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1/10/2017</td>
      <td>34.0</td>
      <td>8.0</td>
      <td>Cloudy</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1/11/2017</td>
      <td>40.0</td>
      <td>12.0</td>
      <td>Sunny</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_df = df.dropna(how="all")       # when all values are NaN only this row will drop
new_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2017</td>
      <td>32.0</td>
      <td>6.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/4/2017</td>
      <td>NaN</td>
      <td>9.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/5/2017</td>
      <td>28.0</td>
      <td>NaN</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/6/2017</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1/7/2017</td>
      <td>32.0</td>
      <td>NaN</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1/8/2017</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1/9/2017</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1/10/2017</td>
      <td>34.0</td>
      <td>8.0</td>
      <td>Cloudy</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1/11/2017</td>
      <td>40.0</td>
      <td>12.0</td>
      <td>Sunny</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_df = df.dropna(thresh=2)        # If i have at list 1 valid values keep the row
new_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2017</td>
      <td>32.0</td>
      <td>6.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/4/2017</td>
      <td>NaN</td>
      <td>9.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/5/2017</td>
      <td>28.0</td>
      <td>NaN</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/6/2017</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1/7/2017</td>
      <td>32.0</td>
      <td>NaN</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1/8/2017</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1/10/2017</td>
      <td>34.0</td>
      <td>8.0</td>
      <td>Cloudy</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1/11/2017</td>
      <td>40.0</td>
      <td>12.0</td>
      <td>Sunny</td>
    </tr>
  </tbody>
</table>
</div>



## Date_range():


```python
n_df = pd.read_csv("data.csv" , parse_dates=["day"])
n_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2017-01-01</td>
      <td>32.0</td>
      <td>6.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2017-01-04</td>
      <td>NaN</td>
      <td>9.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2017-01-05</td>
      <td>28.0</td>
      <td>NaN</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2017-01-06</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2017-01-07</td>
      <td>32.0</td>
      <td>NaN</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2017-01-08</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2017-01-09</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2017-01-10</td>
      <td>34.0</td>
      <td>8.0</td>
      <td>Cloudy</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2017-01-11</td>
      <td>40.0</td>
      <td>12.0</td>
      <td>Sunny</td>
    </tr>
  </tbody>
</table>
</div>




```python
dt = pd.date_range("01-01-2017" , "01-11-2017")
dt
```




    DatetimeIndex(['2017-01-01', '2017-01-02', '2017-01-03', '2017-01-04',
                   '2017-01-05', '2017-01-06', '2017-01-07', '2017-01-08',
                   '2017-01-09', '2017-01-10', '2017-01-11'],
                  dtype='datetime64[ns]', freq='D')




```python
index = pd.DatetimeIndex(dt)
n_df = n_df.reindex(index)
n_df      
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-01-01</th>
      <td>NaT</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-01-02</th>
      <td>NaT</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-01-03</th>
      <td>NaT</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-01-04</th>
      <td>NaT</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-01-05</th>
      <td>NaT</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-01-06</th>
      <td>NaT</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-01-07</th>
      <td>NaT</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-01-08</th>
      <td>NaT</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-01-09</th>
      <td>NaT</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-01-10</th>
      <td>NaT</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-01-11</th>
      <td>NaT</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



# Handaling Missing data


```python
import numpy as np
df = pd.read_csv("weather.csv")
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2017</td>
      <td>32 C</td>
      <td>6 mah</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/2/2017</td>
      <td>-99999</td>
      <td>7</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/3/2017</td>
      <td>28</td>
      <td>-99999</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/4/2017</td>
      <td>-99999</td>
      <td>7</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1/5/2017</td>
      <td>32</td>
      <td>-99999</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1/6/2017</td>
      <td>31</td>
      <td>2</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1/6/2017</td>
      <td>34</td>
      <td>5</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



## Replace data:


```python
df = pd.read_csv("weather.csv")
new_df = df.replace(["-99999"], np.nan ,regex=True)    # replace -99999 with NaN 
new_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2017</td>
      <td>32 C</td>
      <td>6 mah</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/2/2017</td>
      <td>NaN</td>
      <td>7</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/3/2017</td>
      <td>28</td>
      <td>NaN</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/4/2017</td>
      <td>NaN</td>
      <td>7</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1/5/2017</td>
      <td>32</td>
      <td>NaN</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1/6/2017</td>
      <td>31</td>
      <td>2</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1/6/2017</td>
      <td>34</td>
      <td>5</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



## Replace bashed on column:


```python
new_df = df.replace({
    "temperature" : "-99999",     # column wise replace 
    "windspeed" : "-99999",       # -99999 string format in file
    "event" : "0"
} , np.nan)
new_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2017</td>
      <td>32 C</td>
      <td>6 mah</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/2/2017</td>
      <td>NaN</td>
      <td>7</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/3/2017</td>
      <td>28</td>
      <td>NaN</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/4/2017</td>
      <td>NaN</td>
      <td>7</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1/5/2017</td>
      <td>32</td>
      <td>NaN</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1/6/2017</td>
      <td>31</td>
      <td>2</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1/6/2017</td>
      <td>34</td>
      <td>5</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



## Replace beshed on value:


```python
new_df = df.replace({           # value wise replace
    "-99999" : np.nan,
    "0" : "Zero"
})
new_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2017</td>
      <td>32 C</td>
      <td>6 mah</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/2/2017</td>
      <td>NaN</td>
      <td>7</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/3/2017</td>
      <td>28</td>
      <td>NaN</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/4/2017</td>
      <td>NaN</td>
      <td>7</td>
      <td>Zero</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1/5/2017</td>
      <td>32</td>
      <td>NaN</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1/6/2017</td>
      <td>31</td>
      <td>2</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1/6/2017</td>
      <td>34</td>
      <td>5</td>
      <td>Zero</td>
    </tr>
  </tbody>
</table>
</div>



## Replace with regex:


```python
new_df = df.replace({
    "temperature" : "[A-Za-z]",
    "windspeed" : "[A-Za-z]"
},"" , regex=True)    # remoce c , mah etc
new_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2017</td>
      <td>32</td>
      <td>6</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/2/2017</td>
      <td>-99999</td>
      <td>7</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/3/2017</td>
      <td>28</td>
      <td>-99999</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/4/2017</td>
      <td>-99999</td>
      <td>7</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1/5/2017</td>
      <td>32</td>
      <td>-99999</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1/6/2017</td>
      <td>31</td>
      <td>2</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1/6/2017</td>
      <td>34</td>
      <td>5</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



## Replace the list of values to another list of values:


```python
df = pd.DataFrame({
'score': ['exceptional','average', 'good', 'poor', 'average', 'exceptional'],
'student': ['rob', 'maya', 'parthiv', 'tom', 'julian', 'erica']
})
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>score</th>
      <th>student</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>exceptional</td>
      <td>rob</td>
    </tr>
    <tr>
      <th>1</th>
      <td>average</td>
      <td>maya</td>
    </tr>
    <tr>
      <th>2</th>
      <td>good</td>
      <td>parthiv</td>
    </tr>
    <tr>
      <th>3</th>
      <td>poor</td>
      <td>tom</td>
    </tr>
    <tr>
      <th>4</th>
      <td>average</td>
      <td>julian</td>
    </tr>
    <tr>
      <th>5</th>
      <td>exceptional</td>
      <td>erica</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_df = df.replace(["poor" , "average" , "good" , "exceptional"] , [1, 2, 3,4]) # replace 1 list to another 
new_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>score</th>
      <th>student</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>rob</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>maya</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>parthiv</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>tom</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>julian</td>
    </tr>
    <tr>
      <th>5</th>
      <td>4</td>
      <td>erica</td>
    </tr>
  </tbody>
</table>
</div>



# Pandas group by data

## Data Frame groupby:


```python
df = pd.read_csv("weather_by_cities.csv")
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>city</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2017</td>
      <td>new york</td>
      <td>32</td>
      <td>6</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/2/2017</td>
      <td>new york</td>
      <td>36</td>
      <td>7</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/3/2017</td>
      <td>new york</td>
      <td>28</td>
      <td>12</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/4/2017</td>
      <td>new york</td>
      <td>33</td>
      <td>7</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1/1/2017</td>
      <td>mumbai</td>
      <td>90</td>
      <td>5</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1/2/2017</td>
      <td>mumbai</td>
      <td>85</td>
      <td>12</td>
      <td>Fog</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1/3/2017</td>
      <td>mumbai</td>
      <td>87</td>
      <td>15</td>
      <td>Fog</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1/4/2017</td>
      <td>mumbai</td>
      <td>92</td>
      <td>5</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1/1/2017</td>
      <td>paris</td>
      <td>45</td>
      <td>20</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1/2/2017</td>
      <td>paris</td>
      <td>50</td>
      <td>13</td>
      <td>Cloudy</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1/3/2017</td>
      <td>paris</td>
      <td>54</td>
      <td>8</td>
      <td>Cloudy</td>
    </tr>
    <tr>
      <th>11</th>
      <td>1/4/2017</td>
      <td>paris</td>
      <td>42</td>
      <td>10</td>
      <td>Cloudy</td>
    </tr>
  </tbody>
</table>
</div>




```python
g = df.groupby("city")          # dataframe groupby object
g
```




    <pandas.core.groupby.generic.DataFrameGroupBy object at 0x7fe1d7858700>




```python
for i , j in g:
    print(i)        # i is city name
    print(j)        # j is data frame
```

    mumbai
            day    city  temperature  windspeed  event
    4  1/1/2017  mumbai           90          5  Sunny
    5  1/2/2017  mumbai           85         12    Fog
    6  1/3/2017  mumbai           87         15    Fog
    7  1/4/2017  mumbai           92          5   Rain
    new york
            day      city  temperature  windspeed  event
    0  1/1/2017  new york           32          6   Rain
    1  1/2/2017  new york           36          7  Sunny
    2  1/3/2017  new york           28         12   Snow
    3  1/4/2017  new york           33          7  Sunny
    paris
             day   city  temperature  windspeed   event
    8   1/1/2017  paris           45         20   Sunny
    9   1/2/2017  paris           50         13  Cloudy
    10  1/3/2017  paris           54          8  Cloudy
    11  1/4/2017  paris           42         10  Cloudy



```python
mumbai = g.get_group("mumbai")  # mumbai data frame is hare
mumbai
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>city</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>1/1/2017</td>
      <td>mumbai</td>
      <td>90</td>
      <td>5</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1/2/2017</td>
      <td>mumbai</td>
      <td>85</td>
      <td>12</td>
      <td>Fog</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1/3/2017</td>
      <td>mumbai</td>
      <td>87</td>
      <td>15</td>
      <td>Fog</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1/4/2017</td>
      <td>mumbai</td>
      <td>92</td>
      <td>5</td>
      <td>Rain</td>
    </tr>
  </tbody>
</table>
</div>




```python
g.max()                         # new datafeame with max value
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>mumbai</th>
      <td>1/4/2017</td>
      <td>92</td>
      <td>15</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>new york</th>
      <td>1/4/2017</td>
      <td>36</td>
      <td>12</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>paris</th>
      <td>1/4/2017</td>
      <td>54</td>
      <td>20</td>
      <td>Sunny</td>
    </tr>
  </tbody>
</table>
</div>




```python
g.mean()                        # mean of 3 data set will come hare a new dataset
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>temperature</th>
      <th>windspeed</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>mumbai</th>
      <td>88.50</td>
      <td>9.25</td>
    </tr>
    <tr>
      <th>new york</th>
      <td>32.25</td>
      <td>8.00</td>
    </tr>
    <tr>
      <th>paris</th>
      <td>47.75</td>
      <td>12.75</td>
    </tr>
  </tbody>
</table>
</div>




```python
g.describe()                    # describe many things of 3 different dataframe
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="8" halign="left">temperature</th>
      <th colspan="8" halign="left">windspeed</th>
    </tr>
    <tr>
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>mumbai</th>
      <td>4.0</td>
      <td>88.50</td>
      <td>3.109126</td>
      <td>85.0</td>
      <td>86.50</td>
      <td>88.5</td>
      <td>90.50</td>
      <td>92.0</td>
      <td>4.0</td>
      <td>9.25</td>
      <td>5.057997</td>
      <td>5.0</td>
      <td>5.00</td>
      <td>8.5</td>
      <td>12.75</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>new york</th>
      <td>4.0</td>
      <td>32.25</td>
      <td>3.304038</td>
      <td>28.0</td>
      <td>31.00</td>
      <td>32.5</td>
      <td>33.75</td>
      <td>36.0</td>
      <td>4.0</td>
      <td>8.00</td>
      <td>2.708013</td>
      <td>6.0</td>
      <td>6.75</td>
      <td>7.0</td>
      <td>8.25</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>paris</th>
      <td>4.0</td>
      <td>47.75</td>
      <td>5.315073</td>
      <td>42.0</td>
      <td>44.25</td>
      <td>47.5</td>
      <td>51.00</td>
      <td>54.0</td>
      <td>4.0</td>
      <td>12.75</td>
      <td>5.251984</td>
      <td>8.0</td>
      <td>9.50</td>
      <td>11.5</td>
      <td>14.75</td>
      <td>20.0</td>
    </tr>
  </tbody>
</table>
</div>



# Pandas concat

## Concatinate: 


```python
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
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>temp</th>
      <th>humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>mombai</td>
      <td>32</td>
      <td>80</td>
    </tr>
    <tr>
      <th>1</th>
      <td>dehli</td>
      <td>45</td>
      <td>60</td>
    </tr>
    <tr>
      <th>2</th>
      <td>banglore</td>
      <td>30</td>
      <td>78</td>
    </tr>
    <tr>
      <th>0</th>
      <td>new york</td>
      <td>21</td>
      <td>68</td>
    </tr>
    <tr>
      <th>1</th>
      <td>chicago</td>
      <td>14</td>
      <td>65</td>
    </tr>
    <tr>
      <th>2</th>
      <td>orlando</td>
      <td>35</td>
      <td>75</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.concat([india_weather , usa_weather] , ignore_index=True)   # will ignore index , default is False
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>temp</th>
      <th>humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>mombai</td>
      <td>32</td>
      <td>80</td>
    </tr>
    <tr>
      <th>1</th>
      <td>dehli</td>
      <td>45</td>
      <td>60</td>
    </tr>
    <tr>
      <th>2</th>
      <td>banglore</td>
      <td>30</td>
      <td>78</td>
    </tr>
    <tr>
      <th>3</th>
      <td>new york</td>
      <td>21</td>
      <td>68</td>
    </tr>
    <tr>
      <th>4</th>
      <td>chicago</td>
      <td>14</td>
      <td>65</td>
    </tr>
    <tr>
      <th>5</th>
      <td>orlando</td>
      <td>35</td>
      <td>75</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.concat([india_weather , usa_weather] , keys=["India" , "USA"])   # will create adition index ["India" , "USA"]
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>city</th>
      <th>temp</th>
      <th>humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">India</th>
      <th>0</th>
      <td>mombai</td>
      <td>32</td>
      <td>80</td>
    </tr>
    <tr>
      <th>1</th>
      <td>dehli</td>
      <td>45</td>
      <td>60</td>
    </tr>
    <tr>
      <th>2</th>
      <td>banglore</td>
      <td>30</td>
      <td>78</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">USA</th>
      <th>0</th>
      <td>new york</td>
      <td>21</td>
      <td>68</td>
    </tr>
    <tr>
      <th>1</th>
      <td>chicago</td>
      <td>14</td>
      <td>65</td>
    </tr>
    <tr>
      <th>2</th>
      <td>orlando</td>
      <td>35</td>
      <td>75</td>
    </tr>
  </tbody>
</table>
</div>




```python
india = df.loc["India"]     # access India indexed data frame
india
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>temp</th>
      <th>humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>mombai</td>
      <td>32</td>
      <td>80</td>
    </tr>
    <tr>
      <th>1</th>
      <td>dehli</td>
      <td>45</td>
      <td>60</td>
    </tr>
    <tr>
      <th>2</th>
      <td>banglore</td>
      <td>30</td>
      <td>78</td>
    </tr>
  </tbody>
</table>
</div>



## Concar another axis:


```python
temp_df = pd.DataFrame({
    "city" : ["mombai" , "dehli" , "banglore"] ,
    "temp" : [34 , 53 , 43]
})
wind_df = pd.DataFrame({
    "city" : ["new york" , "chicago" , "orlando"] ,
    "temp" : [31 , 24 , 25]
})
df = pd.concat([temp_df , wind_df] , axis=1)     # default axis is 0
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>temp</th>
      <th>city</th>
      <th>temp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>mombai</td>
      <td>34</td>
      <td>new york</td>
      <td>31</td>
    </tr>
    <tr>
      <th>1</th>
      <td>dehli</td>
      <td>53</td>
      <td>chicago</td>
      <td>24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>banglore</td>
      <td>43</td>
      <td>orlando</td>
      <td>25</td>
    </tr>
  </tbody>
</table>
</div>



## Indexing wiht concat:


```python
temp_df = pd.DataFrame({
    "city" : ["mombai" , "dehli" , "banglore"] ,
    "temp" : [34 , 53 , 43]
},index=[0, 1, 2])              # defining index 
 
wind_df = pd.DataFrame({
    "city" : ["delhi" , "mombai"] ,
    "temp" : [31 , 24 ]
},index=[1 , 0])                # defining index

df = pd.concat([temp_df , wind_df] , axis=1)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>temp</th>
      <th>city</th>
      <th>temp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>mombai</td>
      <td>34</td>
      <td>mombai</td>
      <td>24.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>dehli</td>
      <td>53</td>
      <td>delhi</td>
      <td>31.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>banglore</td>
      <td>43</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



## Join dataframe with series():


```python
s = pd.Series(["Humid" , "Dry" , "Rani"] , name="Event")
s
```




    0    Humid
    1      Dry
    2     Rani
    Name: Event, dtype: object




```python
temp_df = pd.DataFrame({
    "city" : ["mombai" , "dehli" , "banglore"] ,
    "temp" : [34 , 53 , 43]
},index=[0, 1, 2])

new = pd.concat([temp_df , s] , axis=1)     # append new datafreame into temp_df
new
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>temp</th>
      <th>Event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>mombai</td>
      <td>34</td>
      <td>Humid</td>
    </tr>
    <tr>
      <th>1</th>
      <td>dehli</td>
      <td>53</td>
      <td>Dry</td>
    </tr>
    <tr>
      <th>2</th>
      <td>banglore</td>
      <td>43</td>
      <td>Rani</td>
    </tr>
  </tbody>
</table>
</div>



# Marge Dataframe

## Using marge():


```python
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
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>temp</th>
      <th>humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>new york</td>
      <td>34</td>
      <td>64</td>
    </tr>
    <tr>
      <th>1</th>
      <td>chicago</td>
      <td>53</td>
      <td>68</td>
    </tr>
    <tr>
      <th>2</th>
      <td>orlando</td>
      <td>43</td>
      <td>75</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1 = pd.DataFrame({
    "city" : ["new york" , "chicago" , "dhaka"] ,
    "temp" : [34 , 53 , 43]                   
})             
df2 = pd.DataFrame({
    "city" : ["new york" , "chicago" , "orlando"] ,
    "humidity" : [64 , 68 , 75]                   
})  
df3 = pd.merge(df1 , df2 , on="city")   # different city will ignore . it is semilar to set theory
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>temp</th>
      <th>humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>new york</td>
      <td>34</td>
      <td>64</td>
    </tr>
    <tr>
      <th>1</th>
      <td>chicago</td>
      <td>53</td>
      <td>68</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3 = pd.merge(df1 , df2 , on="city" , how="outer")     # like as union set and inner jion is default
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>temp</th>
      <th>humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>new york</td>
      <td>34.0</td>
      <td>64.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>chicago</td>
      <td>53.0</td>
      <td>68.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>dhaka</td>
      <td>43.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>orlando</td>
      <td>NaN</td>
      <td>75.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3 = pd.merge(df1 , df2 , on="city" , how="left")      #  take onley left varible city
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>temp</th>
      <th>humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>new york</td>
      <td>34</td>
      <td>64.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>chicago</td>
      <td>53</td>
      <td>68.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>dhaka</td>
      <td>43</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3 = pd.merge(df1 , df2 , on="city" , how="outer" , indicator=True)       #  show marge indicator like left_only , both , right_only
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>temp</th>
      <th>humidity</th>
      <th>_merge</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>new york</td>
      <td>34.0</td>
      <td>64.0</td>
      <td>both</td>
    </tr>
    <tr>
      <th>1</th>
      <td>chicago</td>
      <td>53.0</td>
      <td>68.0</td>
      <td>both</td>
    </tr>
    <tr>
      <th>2</th>
      <td>dhaka</td>
      <td>43.0</td>
      <td>NaN</td>
      <td>left_only</td>
    </tr>
    <tr>
      <th>3</th>
      <td>orlando</td>
      <td>NaN</td>
      <td>75.0</td>
      <td>right_only</td>
    </tr>
  </tbody>
</table>
</div>



## suffixes:


```python
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
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>temperature_x</th>
      <th>humidity_x</th>
      <th>temperature_y</th>
      <th>humidity_y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>new york</td>
      <td>21</td>
      <td>65</td>
      <td>14</td>
      <td>68</td>
    </tr>
    <tr>
      <th>1</th>
      <td>chicago</td>
      <td>14</td>
      <td>68</td>
      <td>21</td>
      <td>65</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3 = pd.merge(df1 , df2 , on="city" , suffixes=("_left" , "_right"))       # create own suffixes
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>temperature_left</th>
      <th>humidity_left</th>
      <th>temperature_right</th>
      <th>humidity_right</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>new york</td>
      <td>21</td>
      <td>65</td>
      <td>14</td>
      <td>68</td>
    </tr>
    <tr>
      <th>1</th>
      <td>chicago</td>
      <td>14</td>
      <td>68</td>
      <td>21</td>
      <td>65</td>
    </tr>
  </tbody>
</table>
</div>



# pivot and pivot tabel


```python
# pivot allaws you to reshape and tranform your data
df = pd.read_csv("pivot_weather.csv")
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>city</th>
      <th>temperature</th>
      <th>humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5/1/2017</td>
      <td>new york</td>
      <td>65</td>
      <td>56</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5/2/2017</td>
      <td>new york</td>
      <td>66</td>
      <td>58</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5/3/2017</td>
      <td>new york</td>
      <td>68</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5/1/2017</td>
      <td>mumbai</td>
      <td>75</td>
      <td>80</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5/2/2017</td>
      <td>mumbai</td>
      <td>78</td>
      <td>83</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5/3/2017</td>
      <td>mumbai</td>
      <td>82</td>
      <td>85</td>
    </tr>
    <tr>
      <th>6</th>
      <td>5/1/2017</td>
      <td>beijing</td>
      <td>80</td>
      <td>26</td>
    </tr>
    <tr>
      <th>7</th>
      <td>5/2/2017</td>
      <td>beijing</td>
      <td>77</td>
      <td>30</td>
    </tr>
    <tr>
      <th>8</th>
      <td>5/3/2017</td>
      <td>beijing</td>
      <td>79</td>
      <td>35</td>
    </tr>
  </tbody>
</table>
</div>




```python
n_df = df.pivot(index="date" , columns="city")  # tranform as index date and city column
n_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="3" halign="left">temperature</th>
      <th colspan="3" halign="left">humidity</th>
    </tr>
    <tr>
      <th>city</th>
      <th>beijing</th>
      <th>mumbai</th>
      <th>new york</th>
      <th>beijing</th>
      <th>mumbai</th>
      <th>new york</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5/1/2017</th>
      <td>80</td>
      <td>75</td>
      <td>65</td>
      <td>26</td>
      <td>80</td>
      <td>56</td>
    </tr>
    <tr>
      <th>5/2/2017</th>
      <td>77</td>
      <td>78</td>
      <td>66</td>
      <td>30</td>
      <td>83</td>
      <td>58</td>
    </tr>
    <tr>
      <th>5/3/2017</th>
      <td>79</td>
      <td>82</td>
      <td>68</td>
      <td>35</td>
      <td>85</td>
      <td>60</td>
    </tr>
  </tbody>
</table>
</div>




```python
n_df = df.pivot(index="date" , columns="city" , values="humidity")  # print only humidity
n_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>city</th>
      <th>beijing</th>
      <th>mumbai</th>
      <th>new york</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5/1/2017</th>
      <td>26</td>
      <td>80</td>
      <td>56</td>
    </tr>
    <tr>
      <th>5/2/2017</th>
      <td>30</td>
      <td>83</td>
      <td>58</td>
    </tr>
    <tr>
      <th>5/3/2017</th>
      <td>35</td>
      <td>85</td>
      <td>60</td>
    </tr>
  </tbody>
</table>
</div>



## pivot tabel:


```python
# pivot table is used to sammarize ang aggregate data inside dataframe
new_df = df.pivot_table(index="city" , columns="date")  # create a new table
new_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="3" halign="left">humidity</th>
      <th colspan="3" halign="left">temperature</th>
    </tr>
    <tr>
      <th>date</th>
      <th>5/1/2017</th>
      <th>5/2/2017</th>
      <th>5/3/2017</th>
      <th>5/1/2017</th>
      <th>5/2/2017</th>
      <th>5/3/2017</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>beijing</th>
      <td>26</td>
      <td>30</td>
      <td>35</td>
      <td>80</td>
      <td>77</td>
      <td>79</td>
    </tr>
    <tr>
      <th>mumbai</th>
      <td>80</td>
      <td>83</td>
      <td>85</td>
      <td>75</td>
      <td>78</td>
      <td>82</td>
    </tr>
    <tr>
      <th>new york</th>
      <td>56</td>
      <td>58</td>
      <td>60</td>
      <td>65</td>
      <td>66</td>
      <td>68</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_df = df.pivot_table(index="city" , columns="date" ,aggfunc=sum)  # is not work until call (margins = True)
new_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="3" halign="left">humidity</th>
      <th colspan="3" halign="left">temperature</th>
    </tr>
    <tr>
      <th>date</th>
      <th>5/1/2017</th>
      <th>5/2/2017</th>
      <th>5/3/2017</th>
      <th>5/1/2017</th>
      <th>5/2/2017</th>
      <th>5/3/2017</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>beijing</th>
      <td>26</td>
      <td>30</td>
      <td>35</td>
      <td>80</td>
      <td>77</td>
      <td>79</td>
    </tr>
    <tr>
      <th>mumbai</th>
      <td>80</td>
      <td>83</td>
      <td>85</td>
      <td>75</td>
      <td>78</td>
      <td>82</td>
    </tr>
    <tr>
      <th>new york</th>
      <td>56</td>
      <td>58</td>
      <td>60</td>
      <td>65</td>
      <td>66</td>
      <td>68</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_df = df.pivot_table(index="city" , columns="date" ,aggfunc=sum , margins=True)  
new_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="4" halign="left">humidity</th>
      <th colspan="4" halign="left">temperature</th>
    </tr>
    <tr>
      <th>date</th>
      <th>5/1/2017</th>
      <th>5/2/2017</th>
      <th>5/3/2017</th>
      <th>All</th>
      <th>5/1/2017</th>
      <th>5/2/2017</th>
      <th>5/3/2017</th>
      <th>All</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>beijing</th>
      <td>26</td>
      <td>30</td>
      <td>35</td>
      <td>91</td>
      <td>80</td>
      <td>77</td>
      <td>79</td>
      <td>236</td>
    </tr>
    <tr>
      <th>mumbai</th>
      <td>80</td>
      <td>83</td>
      <td>85</td>
      <td>248</td>
      <td>75</td>
      <td>78</td>
      <td>82</td>
      <td>235</td>
    </tr>
    <tr>
      <th>new york</th>
      <td>56</td>
      <td>58</td>
      <td>60</td>
      <td>174</td>
      <td>65</td>
      <td>66</td>
      <td>68</td>
      <td>199</td>
    </tr>
    <tr>
      <th>All</th>
      <td>162</td>
      <td>171</td>
      <td>180</td>
      <td>513</td>
      <td>220</td>
      <td>221</td>
      <td>229</td>
      <td>670</td>
    </tr>
  </tbody>
</table>
</div>



## Use grouper function to aggregate:


```python
df["date"] = pd.to_datetime(df["date"])
x = df.pivot_table(index=pd.Grouper(freq="M" , key="date") , columns="city")    # default is average
x
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="3" halign="left">humidity</th>
      <th colspan="3" halign="left">temperature</th>
    </tr>
    <tr>
      <th>city</th>
      <th>beijing</th>
      <th>mumbai</th>
      <th>new york</th>
      <th>beijing</th>
      <th>mumbai</th>
      <th>new york</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-05-31</th>
      <td>30.333333</td>
      <td>82.666667</td>
      <td>58.0</td>
      <td>78.666667</td>
      <td>78.333333</td>
      <td>66.333333</td>
    </tr>
  </tbody>
</table>
</div>


