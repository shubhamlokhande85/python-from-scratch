'Regular Expression (Regex)'
'''
-A Regular Expression (Regex) is a sequence of special characters and symbols used to search,
 match, and manipulate patterns in text
-Regex is a tool used to find a particular pattern inside a string

-Advantages of Regular Expressions
 -Used for data validation
 -Fast searching of text patterns
 -Helps in data cleaning
 -Reduces programming effort
 -Useful in text processing

-syntax 

import re

re.function(pattern, string)

where,
pattern → The rule or format we want to search
string  → The text in which we want to search

-Common Regex Symbols

| Symbol | Meaning               | Example             |
| ------ | --------------------- | ------------------- |
| `.`    | Any single character  | `a.b` matches "acb" |
| `^`    | Starts with           | `^Hello`            |
| `$`    | Ends with             | `world$`            |
| `*`    | Zero or more times    | `ab*`               |
| `+`    | One or more times     | `ab+`               |
| `?`    | Zero or one time      | `colou?r`           |
| `[]`   | Set of characters     | `[abc]`             |
| `{}`   | Number of repetitions | `a{3}`              |

-Function 

| Function             | Purpose                                          | Syntax                             | Example                                |
| -------------------- | ------------------------------------------------ | ---------------------------------- | -------------------------------------- |
| **`re.match()`**     | Checks pattern only at the beginning of a string | `re.match(pattern, string)`        | `re.match("Hi", "Hi Python")`          |
| **`re.search()`**    | Searches pattern anywhere in the string          | `re.search(pattern, string)`       | `re.search("Python", "I like Python")` |
| **`re.findall()`**   | Finds all matching patterns and returns a list   | `re.findall(pattern, string)`      | `re.findall("\d+", "Age 20 and 30")`   |
| **`re.finditer()`**  | Returns all matches as match objects             | `re.finditer(pattern, string)`     | `re.finditer("\d+", "123 456")`        |
| **`re.split()`**     | Splits string where pattern matches              | `re.split(pattern, string)`        | `re.split(",", "A,B,C")`               |
| **`re.sub()`**       | Replaces matching patterns                       | `re.sub(pattern, replace, string)` | `re.sub("cat","dog","cat")`            |
| **`re.fullmatch()`** | Checks if the complete string matches pattern    | `re.fullmatch(pattern, string)`    | `re.fullmatch("\d+", "123")`           |
| **`re.compile()`**   | Creates a reusable regex pattern                 | `re.compile(pattern)`              | `p = re.compile("\d+")`                |



'''

'1. re.search()'

'''
-Searches for a pattern anywhere in the string
-In re.search(), the function does not directly return the pattern value. It returns a Match object
-ecause the Match object contains extra information about the search result
'''

#Eg

import re

text="hey hi there how coding was going"

search=re.search("coding",text)
print(search)

#<re.Match object; span=(17, 23), match='coding'>

'2. re.match()'


'''
-Checks the pattern only at the beginning of the string.
'''

#Eg 
text2="Python is interperted language "
match=re.match('Py',text2)
print(match)
# <re.Match object; span=(0, 2), match='Py'>

'3. re.findall()'
'''
-Returns all matching patterns
'''

#Eg

text3="My address : Street 07, Secondry school 01, IND - 422565"
findall=re.findall("[0-9]",text3)
print(findall)
# ['0', '7', '0', '1', '4', '2', '2', '5', '6', '5']


'4. re.sub()'
'''Replaces matched patterns.

syntax
re.sub(pattern, replacement, string)

where,

| Parameter     | Meaning                                            |
| ------------- | -------------------------------------------------- |
| `pattern`     | The text or pattern to find                        |
| `replacement` | The new text that replaces the pattern             |
| `string`      | The original string where replacement is performed |
'''

#Eg 
text4="hello world 1234 "
sub=re.sub("[0-9]","*",text4)
print(sub)
# hello world ****


