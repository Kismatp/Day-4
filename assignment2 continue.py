# ----------Q.No.6

# strings=input("Enter a string: ")
# print(type(strings))
# length=len(strings)
# count=0
# vowels={'a','e','i','o','u','A','E','I','O','U'}
# for string in strings:
#     for char in vowels:
#         if string==char:
#             count=count+1

# print(count)

# -----------Q.No.7
# num=input("Enter a number: ")
# length=len(num)
# num=int(num)
# sum=0

# for i in range(length):
#     p=num%10
#     sum=sum+p
#     num=num//10

# print(sum)


# ------------Q.no.8


# for char in num1:

    
#     if char=='I' or char=='i':
#         num=num+1
#     if char=='v' or char=='V':
#         num=num+5
#     if char=='x' or char=='X':
#         num=num+10
#     if char=='L' or char=='l':
#         num=num+50
#     if char=='c' or char=='C':
#         num=num+100
#     if char=='d' or char=='D':
#         num=num+500
#     if char=='m' or char=='M':
#         num=num+1000

roman= input ("Enter a Roman numeral: ")
length = len(roman)
dec_number = []
sum = 0
i = 0

for char in roman:
    if char == 'I':
        dec_number.append(1)
    elif char == 'V':
        dec_number.append(5)
    elif char == 'X':
        dec_number.append(10)
    elif char == 'L': 
        dec_number.append(50)
    elif char == 'C':
        dec_number.append(100)
    elif char == 'D':
        dec_number.append(500)
    elif char == 'M':
        dec_number.append(1000)
    else:
        print("Invalid input")
dec_number.append(0)

for i in range(length):
    if dec_number[i+1] > dec_number[i]:
        sum = sum - dec_number[i]
    
    else:
        sum = sum + dec_number[i]

print(f"Equivalent number of roman numeral {roman} is : {sum}")

 # -----------------------Q.No.9

# brackets = input("Enter some sequence of brackets(),{},[]: ")
# bracket = []

# for char in brackets:
#     if char == '(' or char == '{' or char == '[':
#         bracket.append(char)
    
#     elif char == ')' and bracket[-1] == '(':
#         bracket.pop()
    
#     elif char == ']' and bracket[-1] == '[':
#         bracket.pop()
    
#     elif char == '}' and bracket[-1] == '{':
#         bracket.pop()
    
#     else:
#         bracket.append(char)

# if len(bracket) == 0:
#     print(f"{brackets} is valid")

# else:
#       print(f"{brackets} is not valid")