#!/usr/bin/env python
# coding: utf-8

# # Pandas tutorial (Basic)

# This `pandas` tutorial mainly includes two parts, **Basic** and **Advanced**. The former is mandatory for this course and the latter is optional. The following content is the **Basic**  part.

# ## Install Pandas
# If you run code on your own computer, you need to install `pandas`. Open the console and enter ```pip install pandas```

# In[1]:


# Import pandas and view pandas version. The 'as' keyword is to replace pandas with an abbreviation 'pd'.
import pandas as pd

print(pd.__version__)


# ## Introduction to pandas Data Structures
# The two core data structures of `pandas` are
# - `Series`
# - `DataFrame`
# 
# The `Series` is designed to accommodate a sequence of one-dimensional data, and the `Dataframe` is designed to contain cases with several dimensions.

# ## Series
# As shown below, the structure of the `Series` object is simple, which consists of two columns of data that have the same length. The **Value** column holds the data (data of any `NumPy` type) where each element is associated with a label, contained within the **index** column, called the `index`.
# 
# |index|Value|
# |:---|--:|
# |0|-1|
# |1|3|
# |2|8|

# ### Defining a Series

# Call the `pd.Series()` function to create a `Series` object and specify the argument `data` as a `list` or another `Series` object.

# In[2]:


s = pd.Series(data=[-1, 3, 8])  # list
print(s)
# 'data' is the first location parameter, usually ignore parameter name
s1 = pd.Series(s)  # from another Series
print(s1)


# As you can see from the output of the `Series` object, on the left column there is the `index` column, which is a series of labels, and on the right are the corresponding values.

# :::{note}
# If you do not specify any index during the definition of the series, by default, pandas will assign numerical values increasing from 0 as labels. In this case, the labels correspond to the indexes (positions in the array) of the elements in the series object.
# :::

# In general, it is best to create a `Series` object with meaningful labels to distinguish and identify each value. During the constructor call, the labels are added by specifying the value of the `index` option or directly specifying the argument `data` as a `dict` object.

# In[3]:


s2 = pd.Series([-1, 3, 8], index=['x', 'y', 'z'])  # specify the index by 'index' option
print(s2)

s3 = pd.Series({"a": -1, "b": 3, "c": 8})  # dictionary
print(s3)


# Specify the argument `data` as a `array` object of `Numpy`.

# In[4]:


import numpy as np
arr = np.array([100, 20, -3]) # from NumPy Arrays
s4 = pd.Series(arr, index=['x', 'y', 'z'] )

print(s4)


# :::{note}
# Always keep in mind that the values contained in the `NumPy` array or in the
# original series are not copied, but are passed by reference. That is, the object is inserted
# dynamically within the new series object. If it changes, for example its internal element
# varies in value, then those changes will also be present in the new series object.
# :::

# In[5]:


arr[2] = -40
print(arr)
print(s4)


# As you can see in this example, by changing the third element of the `arr` array, we
# also modified the corresponding element in the `s4` series.

#  If you want to individually see the two arrays that make up this data structure, you can call the two attributes of the series as follows: index and values.

# In[6]:


print(s4.values)
print(s4.index)


# ### Selecting the Internal Elements

# You can select individual elements as ordinary `Numpy` arrays, specifying the key.

# In[7]:


s = pd.Series({"a": -1, "b": 3, "c": 8})
s[1]


# Or you can specify the label corresponding to the position of the index.

# In[8]:


s['a']


# In the same way that you select multiple items in a `Numpy` array, you can specify slices as following:

# In[9]:


s[0:2]


# In[10]:


s['a':'c']


# In[11]:


s[['a','c']]


# ### Assigning Values to the Elements

# In[12]:


s['a'] = 100
s


# ### Filtering Values

# If you need to get the indexes and values of the elements in the series that are greater than 4, you
# write the following

# In[13]:


s = pd.Series([1, 3, 5, 2, 10])
s[s > 4]  # greater than 4


# Or you can get the elements that satisfy specific conditions by writing the following

# In[14]:


# According to Boolean value to filter
print(s.isin([2, 5]))
print(s[s.isin([2, 5])])


# ### Operations and Mathematical Functions

# The `Series` object can participate in the common mathematical operations which is the same as the `Numpy` array.

# In[15]:


s * 2.5


# In[16]:


np.exp(s)


# ### Nan Value

# The `NaN` refers to `Not a Number`, which generally is caused by the missing value. Before data analysis, the `NaN` values need to be addressed.

# In[17]:


import numpy as np 
# Declaring a 'Series' including the NaN value
s = pd.Series([1, np.NaN, 10, 9, -2, np.NaN])
s


# Call `isnull()` or `notnull()` functions to generate boolean value and further get the indexes corresponding to the `NaN` value. 

# In[18]:


print(s.isnull())
print(s.notnull())


# Based on the generated boolean value, the `Series` object with full `NaN` value and without `NaN` can be generated by filtering mentioned above.

# In[19]:


print(s[s.isnull()])
print(s[s.notnull()])


# ### Operation of multiple Series

# In[20]:


s = pd.Series({"Singapore": 30, "Malaysia": 23, "Vietnam": 36, "Cambodia": 41})
s1 = pd.Series({"China": 51, "Japan": 73, "Vietnam": 36, "Laos": 31})
s * s1


# As you can see, only indexes that all series have can operate. 

# ## DataFrame

# Compared with the `Series`, the `DataFrame` can contain multidimensional data. Its first column and first row are `index` and `columns`, respectively. (Only for DataFrame without multiple indexes, `DataFrame` with multiple indexes will be introduced in the `Advanced` part). Each column must contain the same data type (numeric, string, boolean, etc.) but different columns can have different data types.
# 
# |index|numeric|string|boolean|
# |:--|:--:|:--:|--:|
# |0|-1|Singapore|True|
# |1|3|China|True|
# |2|8|Japan|False|
# 

# ### Defining a DataFrame

# Call `DataFrame()` function to create a `DataFrame`. The `Array`, `List` and `dict` all can be taken as the input of `data` argument.

# In[21]:


# Array
df = pd.DataFrame(
    np.array([[14, 35, 35, 35], [19, 34, 57, 34], [42, 74, 49, 59]]))
print(df)

# List,  use 'columns' and 'index' parameters to specify the column and index of generated dataframe.
df = pd.DataFrame([["Malaysia", "Kuala Lumpur", 32365999, False],
                   ["Singapore", "Singapore", 5850342, True],
                   ["Vietnam", "Hanoi", 97338579, True]],
                  columns=["Country", "Capital", "Population", "Isdeveloped"],
                  index=["a", "b", "c"])
print(df)

# dict
df = pd.DataFrame({"Country": ["Malaysia", "Singapore", "Vietnam"],
                   "Capital": ["Kuala Lumpur", "Singapore", "Hanoi"],
                   "Population": [32365999, 5850342, 97338579],
                   "Isdeveloped": [False, True, True]},
                  index=["a", "b", "c"])
print(df)


# ### Selecting the Internal Elements

# Similar to `Series`, two ways can be used to select the elements from `DataFrame`. Call `iloc[]` and `loc[]` to select the elements by position and label, respectively .

# In[22]:


# use ':' to represent select all
df.iloc[:, 0:2]


# In[23]:


df.loc[:, "Country":"Population"]


# In[24]:


df.loc["a", ["Country", "Population"]]


# In[25]:


df.iloc[[0, 1]] # If you omit number of columns, all columns will be selected 


# Use ```columns```,```index``` and ```values``` attributes to obtain corresponding object value.

# In[26]:


df.index


# In[27]:


df.columns


# In[28]:


df.values


# Select the corresponding column(s) according to the labels or indexes of columns.

# In[29]:


df["Country"]


# In[30]:


df[["Country", "Population"]] # Use list to select multiple columns  


# In[31]:


df.Country # Also support as atrribute to select


# In[32]:


df["a":"b"] # When select multiple rows, do not use list   


# In[33]:


df[0:2] # When select multiple rows, do not use list


# ### Assigning value

# In[34]:


df1 = df.copy(True)
df1.loc["c", "Country"] = "Japan"
df1.loc["c", "Capital"] = "Tokyo"
df1.loc["c", "Population"] = 126476461
df1.loc["c", "Isdeveloped"] = True
df1


# In[35]:


df1.loc["c"] = ["Japan", "Tokyo", 126476461, True]
df


# ### Assigning index, columns, and name of index and columns

# In[36]:


df1.index = ["e", "f", "g"]
df1.index.name = "label"
df1.columns.name = "attributes"
df1.columns = ["Coun", "Cap", "Pop", "ID"]
df1


# ### Delete columns from dataframe

# In[37]:


del df1["ID"]
df1


# ### Filtering
# Same as ```Series()``` mentioned above.

# In[38]:


df2 = pd.DataFrame(np.array([[14, 35, 35, 35],
                             [19, 34, 57, 34],
                             [42, 74, 49, 59]]))
# filtering lesser than 30
df2[df2 < 30]


# In[39]:


# Filtering accroding to conditions of one column
df[df["Population"] < 50000000]


# You can filter the `DataFrame` according to conditions of multiple columns like the following:

# In[40]:


df[(df["Population"] < 50000000) & (df["Isdeveloped"] == True)]


# ### Transposition  of a Dataframe
# Same as `Numpy` array, `Dataframe` can be transposed. `Columns` changes to `Index` and `Index` changes to `Columns`.

# In[41]:


df1 = df.T
df1


# In[42]:


df1.index


# In[43]:


df1.columns


# ### Merge of Dataframe
# Call `concat()`, `append()` functions to merge the multiple dataframes.

# In[44]:


df1 = pd.DataFrame(np.random.rand(3,4))
df2 = pd.DataFrame(np.random.rand(3,4))
df3 = pd.DataFrame(np.random.rand(6,4))
df4 = pd.DataFrame(np.random.rand(3,6))


# In[45]:


# Vertical merging by default.
pd.concat([df1, df2, df3, df4])


# :::{note}
# As you see, when the shape of multiple dataframe don't match. blank position will be filled using `NaN` value.
# :::

# In[46]:


result = df1.append(df2)
result


# Horizontal merging by specifying `axis` argument as 'columns' or 1. 

# In[47]:


pd.concat([df1, df2, df3, df4], axis='columns')


# // todo ### `join`, `inner` and `merge`

# ### View data

# In[48]:


df1 = pd.DataFrame(np.random.rand(100,4))
df1.head(2)


# In[49]:


df1.tail(3)


# ### Computational tools

# Compute quickly covariance and *Pearson correlation coefficients* of different columns.

# In[50]:


df1 = pd.DataFrame(np.random.rand(5, 5), index=['i1', 'i2', 'i3', 'i4', 'i5'],
                   columns=['c1', 'c2', 'c3', 'c4', 'c5'])
df1.cov()


# In[51]:


df1.corr() # method = pearson (default), optional: kendall, spearman


# In[52]:


df1.corr(method='kendall')


# Compute quickly average value, maximum, mimmum and sum of different columns or rows.

# In[53]:


# compute average value of each column by default.
df1.mean()


# Compute the sum of each row by specifying the `axis` argument as 'columns' or 1.

# In[54]:


df1.sum(axis=1)


# Display a summary of the characteristics of the dataframe

# In[55]:


df1.describe()


# ### Data ranking

# In[56]:


df1 = df.copy(deep=True)
df1.sort_values(by=['Population', 'Country'], ascending=False, na_position='first')


# ## NaN value

# In[57]:


df1 = pd.DataFrame(np.random.rand(5, 5), index=['i1', 'i2', 'i3', 'i4', 'i5'],
                   columns=['c1', 'c2', 'c3', 'c4', 'c5'])
df1.iloc[0, 1] = np.nan
df1.iloc[2, 2] = np.nan
df1.iloc[3, 1] = np.nan
df1.iloc[3, 3] = np.nan
df1


# In[58]:


# detecting nan value
print(df1.isnull())
print(df1.notnull())
print(df1.isna())


# After obtaining the dataframe with Boolean values, you can easily get the number of `NaN` values

# In[59]:


# False:0, True:1
df1.isnull().sum(axis=1)


# Fill `NaN` with a specific value or a value generated by some rules

# In[60]:


# fill NaN value using a specific value
df1.fillna(value=0)


# In[61]:


# fill NaN value using a method
# set inplace to True, the changes will act on dataframe
df1.fillna(method="ffill") # other method: ‘backfill’, ‘bfill’, ‘pad’


# In[62]:


df1.fillna(method="pad")


# In[63]:


# delete NaN value
# ‘any’ : If any NA values are present, drop that row or column.
# ‘all’ : If all values are NA, drop that row or column.

# 0, or ‘index’ : Drop rows which contain missing values.
# 1, or ‘columns’ : Drop columns which contain missing value.
df1.dropna(axis="index", how="any")


# ## Date index

# Data index is very useful for you to deal with time series. You can create a data index by the `date_range` function. The date index mentioned here usually is discrete with equal intervals and it usually has three features: begin date,  end date, and frequency (or intervals).

# In[64]:


dti = pd.date_range("2018-01-01", periods=3, freq="H")
print(dti)
dti = pd.date_range(start="2021-09-28", end="2021-09-30", freq="10H")
print(dti)


# Manipulating and converting date times with timezone information

# In[65]:


dti = pd.date_range(start="2021-09-28", end="2021-09-30", freq="10H")
dti = dti.tz_localize("UTC")
dti


# In[66]:


dti = pd.date_range(start="2021-09-28", end="2021-09-30", freq="10H")
dti = dti.tz_localize("Asia/Singapore")
dti


# Using the `origin` option, one can specify an alternative starting point for the creation of a `DatetimeIndex`. For example, to use 1900-01-01 00:00:00 as the starting time and hour as the unit period length:

# In[67]:


pd.to_datetime([100, 101, 102], unit="h", origin=pd.Timestamp("1900-01-01 00:00:00"))


# Supported units are `D`: day, `h`: hour, `m`: minute, and `s`: second.

# :::{tip}
# The time labels of climate products is usually given a start time point and discrete time interval, and then represented by a column of integers. In this case, we can use above way to construct time labels.
# :::

# ## Upsampling and Downsampling

# * Upsampling: Increase the frequency of the samples by interpolation, such as from minutes to seconds. 
# * Downsampling: Decrease the frequency of the samples by aggregation, such as from months to years.
# 

# In[68]:


# prepare data, this section will be introduced in the next tutorial
# Data Source: http://www.weather.gov.sg/climate-historical-daily/
data = pd.read_csv('../../assets/data/Changi_daily_rainfall.csv', index_col=0, header=0, parse_dates=True)
data.head()


# In[69]:


# Downsampling: Convert monthly data to yearly data by sum or max
df = data.copy(deep=True)
dfsum = df.resample("Y").sum()
dfsum.columns = ["Yearly Rainfall Total (mm)"]
dfsum.head()


# In[70]:


dfmax = df.resample("Y").max()
dfmax.columns = ["Yearly Rainfall Maximum (mm)"]
dfmax.head()


# In[71]:


# Upsampling: Convert monthly data to 10 days' data 
# by directly return (asfreq) or forward filling (pad/ffill)
dfmax.resample('10D').asfreq()[0:5]


# In[72]:


dfmax.resample('10D').pad()[0:5]


# In[73]:


dfmax.resample('D').ffill(limit=2)[0:5]


# ## Input/Output of data

# Typically, you can read data from files ending with ". Xlsx" and ". CSV" using `read_excel()` and `read_csv()` functions, respectively. The `index_col` and `header` arguments are used to specify which column and row are used as `index` and `columns` of dataframe. You can also set `parse_dates` as `True` to parse `index` as the date format. If your date format is uncommon, you can specify the `date_parser` argument which is a function to use for converting a sequence of string columns to an array of datetime instances.

# In[74]:


df = pd.read_csv('../../assets/data/Changi_daily_rainfall.csv', index_col=0, header=0, 
                 parse_dates=True)
df.head()


# In[75]:


custom_dateparse = lambda x: pd.to_datetime(x, format='%Y-%m-%d')
df = pd.read_csv('../../assets/data/Changi_daily_rainfall.csv', index_col=0, header=0, 
                 parse_dates=True, date_parser=custom_dateparse)
df.head()


# You can also specify the `parse_dates` argument as a `list` to parse a column as a date format.

# In[76]:


df = pd.read_csv('../../assets/data/Changi_daily_rainfall.csv', index_col=0, header=0, 
                 parse_dates=[0])
df.head()


# The usage of `read_excel()` function is the same as the `read_csv()`

# :::{tip}
# 1. The `Series` objects can be regarded as the special `DataFrames` object. Actually, when you extract one column from the `DataFrames`, it will be converted to the `Series`.
# 2. The `DataFrame` object has many of the same usages as the `Numpy` array and you can learn by analogy.
# :::

# ## References
# + [Pandas documentation](https://pandas.pydata.org/docs/).
# + [10 minutes to pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html)
# + [Python Data Analytics](https://www.apress.com/gp/book/9781484209585)
