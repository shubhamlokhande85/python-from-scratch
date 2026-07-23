'J.Merging and Joining'
'''
In pandas , merging and joining are used to combine dataframes. similar to SQL
Joins'''

'1.pd.merge()'
'''
-it is used to combine two dataframes based on one or more matching columns
similar to sql joins
-pd.mmerge() performas an inner join by default because the default value of 
the parameter is inner'''

import pandas as pd 

#studnet data 
df1=pd.DataFrame({"id":[1,2,3,4],
                 "sname":["abhy","vijay","karan","krishna"],
                 "smarks":[90,94,79,60]})

#Employee data 
df2=pd.DataFrame({"id":[9,2,5,4],
                  "ename":["sam","tom","alex", "eva"],
                  "esal":[45534,3234,5343,5456]})


'#eg 01 inner join'
inner_join_table=pd.merge(df1,df2,on="id")
print(inner_join_table)
#    id    sname  smarks ename  esal
# 0   2    vijay      94   tom  3234
# 1   4  krishna      60   eva  5456

''''
Note:
1. ON= 
-the ON parameter tells pandas which columns should be used as matching keys 
when merging two dataframes

2.HOW=
-The HOW parameter specifies which rows should be kept when meriging two 
dataframes , Even after choosing the matching column with ON= , There maybe
rows that exist in one dataframe but not the other HOW parameter controls
what happaens to those unmatched rows'''

'#eg 02 left join '
left_join=pd.merge(df1,df2,on="id",how="left")
print(left_join)
#  id    sname  smarks ename    esal
# 0   1     abhy      90   NaN     NaN
# 1   2    vijay      94   tom  3234.0
# 2   3    karan      79   NaN     NaN
# 3   4  krishna      60   eva  5456.0

'#eg 03 right join '
right_join=pd.merge(df1,df2,on="id",how="right")
print(right_join)
#    id    sname  smarks ename   esal
# 0   9      NaN     NaN   sam  45534
# 1   2    vijay    94.0   tom   3234
# 2   5      NaN     NaN  alex   5343
# 3   4  krishna    60.0   eva   5456

'Outer join or full join'
'''
-An outer join in pd.merge() combine two dataframes and keeps all row both
sides whether they match or not , it is also called full outer join 
-It returns matching row , non matching rows from left, non matching 
rows from right missing values filled with NaN'''


'#eg 034 Outer join or Full join'

outer_join=pd.merge(df1,df2,on="id" ,how="outer")
print(outer_join)
#    id    sname  smarks ename     esal
# 0   1     abhy    90.0   NaN      NaN
# 1   2    vijay    94.0   tom   3234.0
# 2   3    karan    79.0   NaN      NaN
# 3   4  krishna    60.0   eva   5456.0
# 4   5      NaN     NaN  alex   5343.0
# 5   9      NaN     NaN   sam  45534.0