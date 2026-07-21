'PANDAS'
'''
-We use pandas in python mainly for working with structured data (tables) in an easy and 
powerful way
-pandas helps you store data in table (like Excel) clean and process idea analyse data 
quickly and prepare data for machine learning
-pandas uses series 1D data(like a column) and dataframe 2D table (row to column)'''


'A.Creating/load data'

'1.DataFrame()'
'''
-dataframe is the main data structure in padas used to store and work with tabular data 
(row and column )
-dataframe() in padas is used to create a dataframe(table)'''
#eg 
import pandas as pd
data = {"sid":[1,2,3,4,5,6],
        "sname":["abc","pqr","tuv","ijk",'def',"rrr"],
        "smark":[34,44,56,67,76,91],
        "scity":["sangli","pune","mumbai","delhi","kolhapur","bengaluru"]}

'creating a new dataset(dataframe) '
df=pd.DataFrame(data)
print(df)
#    sid sname  smark      scity
# 0    1   abc     34     sangli
# 1    2   pqr     44       pune
# 2    3   tuv     56     mumbai
# 3    4   ijk     67      delhi
# 4    5   def     76    kolhapur
# 5    6   rrr     91  bengaluru
'note: the first column in above table without name is repersenting a row_index_number that start from 0'


'B.Viewing data'
''' 
pandas has many methods (function) used to work with data in a dataframe or series 
'''
'1.df.head()'
'''
-df.head() is used to view the first few rows of dataframe 
-df.head() shows first 5 rows by default '''

#eg 01
df= pd.DataFrame(data)
print(df.head())
#    sid sname  smark     scity
# 0    1   abc     34    sangli
# 1    2   pqr     44      pune
# 2    3   tuv     56    mumbai
# 3    4   ijk     67     delhi
# 4    5   def     76  kolhapur

#eg 02
print(df.head(2))
#    sid sname  smark   scity
# 0    1   abc     34  sangli
# 1    2   pqr     44    pune

'2.df.tail()'
'''
-df.tail() is used to view the last few rows of a dataframe 
-df.tail() shows last 5 rows by default'''

#eg 01
df=pd.DataFrame(data)
print(df.tail())
#    sid sname  smark      scity
# 1    2   pqr     44       pune
# 2    3   tuv     56     mumbai
# 3    4   ijk     67      delhi
# 4    5   def     76   kolhapur
# 5    6   rrr     91  bengaluru

#eg 02 
print(df.tail(2))
#    sid sname  smark      scity
# 4    5   def     76   kolhapur
# 5    6   rrr     91  bengaluru


'3.df.sample()'
'''
-df.sample() is used to randomly select rows from a dataframe
-df.sample() is return one random row by default'''

#eg 01 
print(df.sample())
#    sid sname  smark  scity
# 3    4   ijk     67  delhi

#eg 02 

print(df.sample(3))
#    sid sname  smark      scity
# 5    6   rrr     91  bengaluru
# 0    1   abc     34     sangli
# 1    2   pqr     44       pune



'4.df.info()'
'''
-df.info() is used to display a quick summary of dataframe 
-it helps you understand the structure of your dataset'''

#eg 02 
print(df.info())
# <class 'pandas.DataFrame'>
# RangeIndex: 6 entries, 0 to 5
# Data columns (total 4 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   sid     6 non-null      int64
#  1   sname   6 non-null      str  
#  2   smark   6 non-null      int64
#  3   scity   6 non-null      str  
# dtypes: int64(2), str(2)
# memory usage: 324.0 bytes
# None
'''
note:
df.info() returns None because it is designed to print
information directly not return value'''



'5.df.describe()'
'''
-it is used to generate as statistical summary of dataframe 
-it mainly works with a n numeric columns and gives key 
statistics '''
#eg
print(df.describe())
#             sid      smark
# count  6.000000   6.000000
# mean   3.500000  61.333333
# std    1.870829  20.992062
# min    1.000000  34.000000
# 25%    2.250000  47.000000
# 50%    3.500000  61.500000
# 75%    4.750000  73.750000
# max    6.000000  91.000000
'''
note:
25% - Lower quater
50% - Median
75% - upper quater '''

'C.Selecting Data'

'1.df["column_name"]'
'It is used to select a single column from a dataframe or dataset '
#eg 01 - selecting single column from dataframe 
print(df["sname"])
# 0    abc
# 1    pqr
# 2    tuv
# 3    ijk
# 4    def
# 5    rrr
# Name: sname, dtype: str

'2.df[["column_name1","column_name2",...,"column_nameN"]]'
'''
It is used to select multiple columns from a dataframe'''
#eg 01 selecting multiple columns from a dataframe
print(df[["sname","smark"]])
#   sname  smark
# 0   abc     34
# 1   pqr     44
# 2   tuv     56
# 3   ijk     67
# 4   def     76
# 5   rrr     91

'3.df.loc[row_index_number]'
'''
It is used to select row by its index_number(label) from dataframe'''

#eg 01  selecting single row from a dataframe
print(df.loc[2])   # here 2 is row index_number 
# sid           3
# sname       tuv
# smark        56
# scity    mumbai
# Name: 2, dtype: object

'D.Modifying Data'

'1.df["New_Column/Existing_Column"]=["values"]'
'It is used to add a new column or update an existing one in a dataframe'

# eg 01 Updating existing column 
df["sname"] = ["Sam","Thomas","Alex","Harry","Peter","Robert"]
print(df)
#    sid   sname  smark      scity
# 0    1     Sam     34     sangli
# 1    2  Thomas     44       pune
# 2    3    Alex     56     mumbai
# 3    4   Harry     67      delhi
# 4    5   Peter     76   kolhapur
# 5    6  Robert     91  bengaluru


#eg 02 updating existing column with less length of values ?
'df["sname"]=["barak","micheal","nelson"]'
'print(df.head())'
# ValueError: Length of values (3) does not match length of index (6)
'''
note:
-if the lengths does not match of a new column values and a exist column values 
it raise ValueError
'''

#eg 03 adding new column in existing dataframe
df["sstatus"]=["on","off","on","on","on","off"]
print(df)
#     sid   sname  smark      scity sstatus
# 0    1     Sam     34     sangli      on
# 1    2  Thomas     44       pune     off
# 2    3    Alex     56     mumbai      on
# 3    4   Harry     67      delhi      on
# 4    5   Peter     76   kolhapur      on
# 5    6  Robert     91  bengaluru     off

'2.df.rename(columns={"old_column_nm:new_column_nm},Inplace=True)'

'''
-in pandas it is used to rename columns names in dataframe
-in pandas inplace=Ture means modify the original dataframe directly instead
of creating a new one '''

#eg 01 changing single column name 
df.rename(columns={"sname":"student_name"},inplace=True)
print(df.info())
# <class 'pandas.DataFrame'>
# RangeIndex: 6 entries, 0 to 5
# Data columns (total 5 columns):
#  #   Column        Non-Null Count  Dtype
# ---  ------        --------------  -----
#  0   sid           6 non-null      int64
#  1   student_name  6 non-null      str  
#  2   smark         6 non-null      int64
#  3   scity         6 non-null      str  
#  4   sstatus       6 non-null      str  
# dtypes: int64(2), str(3)
# memory usage: 372.0 bytes
# None


#eg 02 changing multiple column name 
df.rename(columns={"sid":"studet_id","smark":"student_mark","scity":"student_scity"},inplace=True)
print(df.info())
# <class 'pandas.DataFrame'>
# RangeIndex: 6 entries, 0 to 5
# Data columns (total 5 columns):
#  #   Column         Non-Null Count  Dtype
# ---  ------         --------------  -----
#  0   studet_id      6 non-null      int64
#  1   student_name   6 non-null      str  
#  2   student_mark   6 non-null      int64
#  3   student_scity  6 non-null      str  
#  4   sstatus        6 non-null      str  
# dtypes: int64(2), str(3)
# memory usage: 372.0 bytes
# None


'3.df.drop(columns=["col1"],Inplace=True)'
'''
-It is used to remove / delete a single column from a pandas dataframe '''
df.drop(columns=["sstatus"], inplace=True)
print(df)
#    studet_id student_name  student_mark student_scity
# 0          1          Sam            34        sangli
# 1          2       Thomas            44          pune
# 2          3         Alex            56        mumbai
# 3          4        Harry            67         delhi
# 4          5        Peter            76      kolhapur
# 5          6       Robert            91     bengaluru

'More Methods In Next Session S49'
