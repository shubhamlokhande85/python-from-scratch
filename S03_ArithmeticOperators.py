'# operators '

'# i) operands '
'# a value or a variable on which a specific operation is performed '

'# ii) operator '
'# its specifies which operation is to be performed on operands '

'#iii) precendence '
'# sequence of precedence **, %, //, / , *, -, +'
# python solve equation this way(precendence) like in maths BODMAS used to solve equations
 
 
'# a) arithmetic operators '
'''
-Arithmetic operators in Python are used to perform mathematical calculations like addition, 
subtraction, multiplication, and division

-
| Operator | Meaning             | Example       |
| -------- | ------------------- | ------------- |
| `+`      | Addition            | `5 + 3 → 8`   |
| `-`      | Subtraction         | `5 - 3 → 2`   |
| `*`      | Multiplication      | `5 * 3 → 15`  |
| `/`      | Division            | `6 / 3 → 2.0` |
| `%`      | Modulus (Remainder) | `7 % 3 → 1`   |
| `//`     | Floor Division      | `7 // 3 → 2`  |
| `**`     | Power (Exponent)    | `2 ** 3 → 8`  |

'''


'# i) ** - exponentiation'

'# its is used to raise one number to the power of another  '
#eg 
a = 3**5 # 3*3*3*3*3
print(a)   
#243

#eg
b=5**3 # 5*5*5
print(b)
#125

'# ii) %  - modulus/remainder '
'# its return remainder after dividing one number by another '
#eg
remainder = 13%10 
print(remainder)
#3 

'# iii) // - floor division '
'# its return quotient as integer value even if quotient float number '
#eg
quotientAsInteger = 153 // 10 
print(quotientAsInteger) # its return 15 but actual is 15.3
# 15

'# iv) / - division '
'# its divide one number by another but its returns value in floating number '
#eg
division=45/6
print(division)
#7.5

'# v) * - Multiplication '
'# its used to multiply one number to another '
#eg 01
multi=7*7
print(multi)
#49

'# imp - its also used with string to replicate strings '
#eg 02
replica = "shubham"* 3
print(replica)
#shubhamshubhamshubham


'# vi) - _ subtractions or difference operator '
#eg
diff = 10 -5
print(diff)
# 5

'# vii) + - addition '
'# its used to add one number with another '
#eg 01
add = 3 + 4
print(add)
# 7 
'''
NOTE
# imp - its also used with string for strig concatnetion 
'''
#eg 02
concat = "shubham" + "Lokhande"
print(concat)
# shubhamLokhande

#eg 03 

# concat2="shubham" + 2
# print(concat2)
' it will TypeError cause string and interger cannot added cause both  datatype are diffrent  '

''''we will learn datatypes in upcoming session's '''