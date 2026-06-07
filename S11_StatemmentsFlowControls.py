'''statements in flow controls'''
'''1.break'''
'''ts is used to stop loop permantaly before normal ending '''
# eg.1
for i in range(11):
    if i == 7:
        break 
    print(i)
# output -
# 0
# 1
# 2
# 3
# 4
# 5
# 6

#eg.2
i = 1
while i <11:
    if i == 7:
        break 
    print(i)
    i += 1 
# output - 
# 1
# 2
# 3
# 4
# 5
# 6

'''2.continue'''
'''it is used to skip the iteration of loop body for 
current iteration  only move control to the next'''

# eg.1
for i in range(11):
    if i == 5:
        continue 
    print(i)
# output - 
# 0
# 1
# 2
# 3
# 4
# 6 # five is skipeed here and control moves to next 
# 7
# 8
# 9
# 10
       
       
# eg.2
i = 1 
while i < 11: 
    if i == 5:
        continue
    print(i)
    i += 1 
    
# output -
# 1
# 2
# 3
# 4


'''3.pass'''
''' the pass statement is null(empty) statement in python
it is used when a statement is required syntactically , but dont 
you do not want tp write any code there yet'''

def hello():
    pass