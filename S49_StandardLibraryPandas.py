'E.Handling Missing Value'
'''
-In Pandas and databases ,NULL means a values is missing , empty or unknown,
it does not mean 0 (ZERO) or and empty string necessarily it means no data
available 
-np.nan means not a number it is a special value in numpy used to  represent 
missing or undefined numeric data
-In pandas, `np.nan` is often used to represent missing values, even in string
(`object`) columns. This is because pandas historically relied on NumPy for
handling missing data, making `np.nan` the common missing-value marker across 
many column types.

'''
'creating a dataframe to understand more pandas method'

import numpy as np
import pandas as pd 
df=pd.DataFrame({"name":["alice","bob","charlie","david",np.nan],
                 "age":[25,np.nan,30,20,28],
                 "salary":[5000,6000,np.nan,45000,5300],
                 "city":["NY","LA",np.nan,"chicago","huston"]})
print(df)
#       name   age   salary     city
# 0    alice  25.0   5000.0       NY
# 1      bob   NaN   6000.0       LA
# 2  charlie  30.0      NaN     NaN
# 3    david  20.0  45000.0  chicago
# 4      NaN  28.0   5300.0   huston

'1.df.isnull()'
'''
It is used in pandas to check for missing (null) values in dataframe 
it returns True if a value is missing (NaN ,None ,pd.NA) and returns if a 
value exists '''
#eg 
print(df.isnull())
#     name    age  salary   city
# 0  False  False   False  False
# 1  False   True   False  False
# 2  False  False    True   True
# 3  False  False   False  False

'2.df.dropna(axis=0/1)'
'''
-It is used to pandas to remove rows or columns that contain missing values 
like NaN ,None or pd.NA
-axis=0 
it is default behavour of df.dropna() meaning that missing values one
checked row -wise and any row containing at least one null value is 
removed unless specified otherwise

-axis=0
it meaning that missing values onechecked column -wise and any column 
containing at least one null value is removed unless specified otherwise'''
#eg 01  axis = 0 
print(df.dropna())
# 0  alice  25.0   5000.0       NY
# 3  david  20.0  45000.0  chicago

#eg axis = 1 
print(df.dropna(axis=1))
# Empty DataFrame
# Columns: []
# Index: [0, 1, 2, 3, 4]

'3.df.Fillna()'
'''
-It is used in pandas to replace missing value (NaN ,None , pd.NA) with a 
specified value
-df.Fillna() does not modify original dataframe, it returns a new dataframe 
-when we have change original dataframe then we have to assign df.fillna() back 
to original dataframe vairiable to get modify original dataframe'''



'''#eg 01 (filling Null values) its working with whole dataframe that 
create new dataframe '''

df2=df.fillna("unknown") # its create and modify new dataframe 
print(df2) 
#       name      age   salary     city
# 0    alice     25.0   5000.0       NY
# 1      bob  unknown   6000.0       LA
# 2  charlie     30.0  unknown  unknown
# 3    david     20.0  45000.0  chicago
# 4  unknown     28.0   5300.0   huston

'''#eg 02 assigning df.fillna() back to original dataframe variable so 
change can happen in original dataframe '''

'df=df.fillna("unknown")' # its modify original dataframe 
'print(df)'
#      name      age   salary     city
# 0    alice     25.0   5000.0       NY
# 1      bob  unknown   6000.0       LA
# 2  charlie     30.0  unknown  unknown
# 3    david     20.0  45000.0  chicago
# 4  unknown     28.0   5300.0   huston


'''
note:
here you can see that numeric column also get string unknown in this
case we have to change specific column value so value can match columns
datatype 
''' 

#eg 01 filling value in  specific column in  new dataframe 
'method 01 '
df2=df.fillna({"age":27}) # its fill value in new dataframe's integer column using dictionary
print(df2)
#       name   age   salary     city
# 0    alice  25.0   5000.0       NY
# 1      bob  27.0   6000.0       LA
# 2  charlie  30.0      NaN      NaN
# 3    david  20.0  45000.0  chicago
# 4      NaN  28.0   5300.0   huston

'method 02 '
#eg 02  # its fill value in new dataframe's string column
df2=df["name"].fillna("shubham") 
print(df2)
# 0      alice
# 1        bob
# 2    charlie
# 3      david
# 4    shubham
# Name: name, dtype: str

'method 03'
#eg 03 - this column null position get value using previous value and next 
# value's combined average value

df2=df["age"].fillna(df["age"].mean()) # 
# its fill value in new dataframe's integer column
print(df2)
# 0    25.00
# 1    25.75
# 2    30.00
# 3    20.00
# 4    28.00
# Name: age, dtype: float64

'method 04 '
#eg 04 fillig multiple specific columns using dictionary
df2=df.fillna({"name":"shubham","age":29,"salary":55323,"city":"texas"})
print(df2)
#       name   age   salary     city
# 0    alice  25.0   5000.0       NY
# 1      bob  29.0   6000.0       LA
# 2  charlie  30.0  55323.0    texas
# 3    david  20.0  45000.0  chicago
# 4  shubham  28.0   5300.0   huston



'3.1.df.ffill(forward fill)'
'''
forward fill(often written as ffill) in pandas is a method used to fill 
missing values using previous valid value in the column'''
#eg 
df2=df.ffill()
print(df2)
#       name   age   salary     city
# 0    alice  25.0   5000.0       NY
# 1      bob  25.0   6000.0       LA
# 2  charlie  30.0   6000.0       LA
# 3    david  20.0  45000.0  chicago
# 4    david  28.0   5300.0   huston

'3.2.df.bfill( backword fill)'
'''
backward fill(often written as bfill) in pandas is a method used to fill 
missing values using next valid value in the column'''
#eg
df2=df.bfill()
print(df2)
#       name   age   salary     city
# 0    alice  25.0   5000.0       NY
# 1      bob  30.0   6000.0       LA
# 2  charlie  30.0  45000.0  chicago
# 3    david  20.0  45000.0  chicago
# 4      NaN  28.0   5300.0   huston


'F.Sorting'
'''
-In pandas it used to sort a dataframe based on one or more columns
-it arranges rows in ascending or descending = True '''


df3=pd.DataFrame({"eid":[1,2,3,4,5],
                 "ename":["sam","alex","thomas","messi","ronaldo"],
                 "esalary":[12033,13032,14322,10232,12332],
                 "ecity":["ny","la","Tx","dc","oh"]})
print(df3)
#    eid    ename  esalary ecity
# 0    1      sam    12033    ny
# 1    2     alex    13032    la
# 2    3   thomas    14322    Tx
# 3    4    messi    10232    dc

#eg 01 ascending order 
print(df3.sort_values(by="esalary"))
#   eid    ename  esalary ecity
# 3    4    messi    10232    dc
# 0    1      sam    12033    ny
# 4    5  ronaldo    12332    oh
# 1    2     alex    13032    la
# 2    3   thomas    14322    Tx

#eg descending order 
print(df3.sort_values(by="ecity",ascending=False))
#    eid    ename  esalary ecity
# 4    5  ronaldo    12332    oh
# 0    1      sam    12033    ny
# 1    2     alex    13032    la
# 3    4    messi    10232    dc
# 2    3   thomas    14322    Tx


'G.Reading and Writing Files'
'''
| File Type                  | Read                  | Write               |
| -------------------------- | --------------------- | ------------------- |
| **CSV**                    | `pd.read_csv()`       | `df.to_csv()`       |
| **Excel**                  | `pd.read_excel()`     | `df.to_excel()`     |
| **JSON**                   | `pd.read_json()`      | `df.to_json()`      |
| **SQL Database**           | `pd.read_sql()`       | `df.to_sql()`       |
| **Parquet (Fast storage)** | `pd.read_parquet()`   | `df.to_parquet()`   |
| **Pickle (Python object)** | `pd.read_pickle()`    | `df.to_pickle()`    |
| **HTML Table**             | `pd.read_html()`      | `df.to_html()`      |
| **XML**                    | `pd.read_xml()`       | `df.to_xml()`       |
| **Clipboard (Copy/Paste)** | `pd.read_clipboard()` | `df.to_clipboard()` |'''

'1.1.pd.read_csv()'
'''
It is function in pandas used to read data from a  CSV(comma seperated values)
file and load it into a dataframes it converts a CSV file into a pandas 
dataframes so you can analyze it '''

#To see original data student.csv 
with open ("student.csv","r") as file1:
    data=file1.read()
    print(data)
# Name , Age,  Marks
# Alice ,  20   ,  85
# Bob  , 21   ,  90
# Charlie  , 19  ,   78
     
#eg 01 reading data from csv 
df4=pd.read_csv("student.csv")     
print(df4)
#        Name    Age    Marks
# 0     Alice     20       85
# 1      Bob      21       90
# 2  Charlie      19       78

'1.2.df.to_csv()'
'df.to_csv() is a DataFrame method that saves a DataFrame to a CSV file'


'A.Working with data or modifying dataframe '
df4["Grade"]=["A","A+","B"]

'B.To save this changes in CSV file or save CSV file we use df.to_csv()'
#eg 
df4.to_csv("students_updated.csv",index=False)

'''
where,
df                     → The DataFrame you want to save.
.to_csv()              → Method that writes the DataFrame to a CSV file.
"students_updated.csv" → The name (or path) of the output CSV file.
index=False            → Do not save the DataFrame's index (row numbers).'''

"C.to check csv file is updated or not "
df5=pd.read_csv("students_updated.csv")
print(df5)
#        Name    Age    Marks Grade
# 0     Alice     20       85     A
# 1      Bob      21       90    A+
# 2  Charlie      19       78     B

'This same method applies to other file types as well.'
