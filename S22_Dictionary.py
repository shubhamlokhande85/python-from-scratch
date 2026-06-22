'DISCTIONARY'
'it is collection of object or values that stored in sequence'
'it stores data in key - value pairs'
'its key are immutable but its values are mutables '
'its does not allow duplicates key values pairs'
'its store same as well as different datatypes of data'
'its denotes by curly braces {}'

'a.common operation on dictionary '

dict={1:"shubham", 2:"shanggai",3:"bombay","d":False }

'1. displaying entire list'
print(dict)
# output -{1: 'shubham', 2: 'shanggai', 3: 'bombay', 4: False} 

'2.accesing specific value from dictionary using key '
print(dict["d"]) # "d" is key not index 
# False

print(dict[3]) # 3 is key
#bombay

'3.displaying only keys from disctionary'
print(dict.keys())
# dict_keys([1, 2, 3, 'd'])

'4.displaying only values from dictionary'
print(dict.values())
#dict_values(['shubham', 'shanggai', 'bombay', False])

'5.updating a specific value from a dictionary using key associated with it'
dict[1]="Delhi"
print(dict)
#{1: 'Delhi', 2: 'shanggai', 3: 'bombay', 'd': False}

'6.displaying length of disctionary '
print(len(dict))
#4

'7. deleting specific value from dictionary using key associated with it'
del dict["d"]
print(dict)
# {1: 'Delhi', 2: 'shanggai', 3: 'bombay'}

'8.Deleting Entire dictionary'
del dict
print(dict)
# <class 'dict'>

'b. Dictionary methods'

'1.get()'
'it is a dictionary method used to safetly access the value of key'
'syntax'
'dict_name.get(key,default_value)'

dict2={1:"prannad",2:"shubham",3:"piyush"}
print(dict2.get(2))
#shubham

'if key is not available its return None'
print(dict2.get(7))
# None

'using default value - if key does not exits then default value will print '
print(dict2.get(5,"key is not avalible in dictionary"))
#key is not avalible in dictionary

'2.items()'
'it is a dictionary method that return all key values pairs as tuple'
'syntax'
'dict_name.items()'
print(dict2.items())
#dict_items([(1, 'prannad'), (2, 'shubham'), (3, 'piyush')])

'3.keys()'
'it is a dictionary method that returns all the keys from a dictionary'
'syntax'
'dict_name.keys()'
print(dict2.keys())
#dict_keys([1, 2, 3])

'4.values()'
'it is dictionary method that returns only values from dictionary'
'syntax'
'dict_name.values()'
print(dict2.values())
# dict_values(['prannad', 'shubham', 'piyush']

'5.pop()'

'it is dictionary method used to remove a key and return its value'
'syntax'
'dict_name.pop(key , default_Message)'
dict3={1:"hello",2:"world"}
print(dict3.pop(1))  # remove value of key 1
#hello

print(dict3)
#{2: 'world'}

'when key not found in dictionary its raise a KeyError'
'print(dict3.pop(3))'
# KeyError: 3

'if pop() applied on empty dictionary its raise TypeError'
dict4={} # Empty dictionary
'print(dict4.pop())'
#TypeError: pop expected at least 1 argument, got 0

'6.popitem()'
'it is a dictionary method that removes and return last inserted key-value pair '
'it return output in tuple'

'syntax '
'dict_name.popitem()'
dict5={1:"ramesh",2:"samanth",3:"suraj",4:"omkar"}
print(dict5.popitem())
#(4, 'omkar')
print(dict5)
#{1: 'ramesh', 2: 'samanth', 3: 'suraj'}

'7.update()'
'''it is dictionary method that used to add new  items
or modify existing item from another dictionary or iterable'''

'syntax'
'dict_name1.update(dict_name2)' # in case of merge
'dict_name1.update(dicttionary iterabel)' # in case of add or modify


'eg.1 update() add new key-value pair if the key values pair not present in dictionary' 
dict6={1:"hello",2:"world",3:"welcome"}
dict6.update({4:"to",5:"planet",6:"earth"}) # iterable used 
print(dict6)
# {1: 'hello', 2: 'world', 3: 'welcome', 4: 'to', 5: 'planet', 6: 'earth'}

'eg.2 if key already existing then update () replace(updates) its value with new one '
dict6.update({1:"Namskar"})
print(dict6)
#{1: 'Namskar', 2: 'world', 3: 'welcome', 4: 'to', 5: 'planet', 6: 'earth'}

'eg3 update method can merge two dictionary into one '
dict7={1:"football",2:"baseball",3:"rubby"}
dict8={4:"hockey",5:"Basketball",6:"cricket"}
dict7.update(dict8) # here dont use print cause dict8 is merged in dict7 so now we use print with dict7
print(dict7)
#{1: 'football', 2: 'baseball', 3: 'rubby', 4: 'hockey', 5: 'Basketball', 6: 'cricket'}

'8.setdefault()'
'it is dictionary method that returns the value of a key if it exists and if it does not '
'exists then it is return inserted default key value '
'its return value as tuple'

'syntax'
'dict_name.setdefault(key, defalut_value)'

dict9={1:"ranbir",2:True,3:(5+9j)}
print(dict9.setdefault(1,"You are not entered existing key to returnm values"))
#ranbir
'if key not exist its return default value'
print(dict9.setdefault(8,"You are not entered existing key to returnm values"))
#You are not entered existing key to returnm values                       