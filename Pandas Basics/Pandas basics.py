import pandas as pd
import sys
print(sys.version)
print('pandas version', pd.__version__)

#Used to work with a pandas DataFrame 
pd.DataFrame()

#We can read using this from a .csv or Excel or DB
pd.read_csv()

#Used to write to a DataSet
df = pd.read_parquet('flights.parquet')
#Parquet is an open-source, column-oriented data file format designed for efficient data storage and retrieval, especially for large datasets, and is widely used in big data processing frameworks like Apache Hadoop and Apache Spark.
type(df)

#We can write to files or DB
df.to_csv('flights.csv', index=False)

DataFrame Basics:
#Shows the first 5 rows of the DF
#if n is provided it'll show n rows
df.head(n)
#When head is used if the number of columns are huge then the data can be hidden.
pd.set_option('display.max_columns',500)
#shows Last 5 rows in the DataFrame
df.tail()

#provides a random subset of rows from the entire dataset
df.sample(frac=0.1"""provides the fraction of the data set
                    i.e 10 Percent of the DataSet.""" or 5"""
                    provides the number of dataset mentioned""",random_state=529)


#Access all the columns directly in the form of a list
df.columns

#will give the Index Value in the dataFrame
df.index

#Gives info of the Data Frame
df.info

#To provide the descriptive statistics of the Data'
df.describe()

#Shape of the DF
df.shape 
#Length of the DF
len(df)

df[['FlightDate', 'Arline', 'Origin']]

