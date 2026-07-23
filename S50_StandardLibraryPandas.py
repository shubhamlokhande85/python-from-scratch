'H.Grouping & Aggregation'
'1.groupby()'
'''
In pandas it is used to group data based on one or more columns and preform
aggregation(like sum,mean,count..etc), it splits data into group, applies a 
function and combine the result'''

#dataframe 
import pandas as pd 
df =pd.DataFrame({"name":["rahul","bob","charlie","david",
                  "eva","frank","grace","henry"],
                  "department":["IT","HR","IT","Finance",
                                "HR","IT","Finance","HR"],
                  "salary":[60000,50000,75000,50000,
                            48000,65000,52000,47000],
                  "city":["pune","mumbai","pune","dehli",
                          "mumbai","pune","dehli","mumbai"]})
print(df)
#       name department  salary    city
# 0    rahul         IT   60000    pune
# 1      bob         HR   50000  mumbai
# 2  charlie         IT   75000    pune
# 3    david    Finance   50000   dehli
# 4      eva         HR   48000  mumbai
# 5    frank         IT   65000    pune
# 6    grace    Finance   52000   dehli
# 7    henry         HR   47000  mumbai

#eg 01 Object creation for aggregation operation 
print(df.groupby("department"))
#<pandas.api.typing.DataFrameGroupBy object at 0x000002316813A3C0>
'''A GroupBy object has been created, but no operation (like sum, mean, or count)
has been requested yet'''

#eg 02 Total(sum) salary by department 
print(df.groupby("department")["salary"].sum())
# department
# Finance    102000
# HR         145000
# IT         200000
# Name: salary, dtype: int64


#eg 03 count employees in each department 
print(df.groupby("department")["name"].count())
# department
# Finance    2
# HR         3
# IT         3
# Name: name, dtype: int64

#eg 04 maximum salary by city 
print(df.groupby("city")["salary"].max())
# city
# dehli     52000
# mumbai    50000
# pune      75000
# Name: salary, dtype: int64

#eg 05 multiple aggregation (.agg[...])
print(df.groupby("department")["salary"].agg(["mean","sum","max","min"]))

#                     mean     sum    max    min
# department                                    
# Finance     51000.000000  102000  52000  50000
# HR          48333.333333  145000  50000  47000
# IT          66666.666667  200000  75000  60000

'I.Useful Utillities'

'1.df.["column_name"].unique()'
'''It returns an unique (distinct) values from a column'''

#eg # show unique cities 
print(df["city"].unique())
# <StringArray>
# ['pune', 'mumbai', 'dehli']
# Length: 3, dtype: str

'2.df.nunique()'
'It returns the number of unique values in each column of a dataframe'
#eg 
print(df["department"].nunique())
#3

'3.df.value_counts()'
'''
In pandas it is used to count how many times each unique row appears in dataframe
or values in series'''
#eg show unique rows from datafrmae 
print(df.value_counts())
# name     department  salary  city     #count
# rahul    IT          60000   pune      1
# bob      HR          50000   mumbai    1
# charlie  IT          75000   pune      1
# david    Finance     50000   dehli     1
# eva      HR          48000   mumbai    1
# frank    IT          65000   pune      1
# grace    Finance     52000   dehli     1
# henry    HR          47000   mumbai    1
# Name: count, dtype: int64
'note: The 1 in last column count of unique rows that appears in dataframe '

      