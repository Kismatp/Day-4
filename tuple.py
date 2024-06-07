# creating a tuple 
tuple1 = (1,2,3,4,7,7,4,3,4,56,6) #Empty tuple
print (tuple1)
print (type(tuple1))

tuple2 = ("Ram", 21,100)
first_element=tuple2[0]
last_element = tuple2[-1]
print(f"First element of tuple: {first_element}")
print(f"Last element of tuple: {last_element}")

print (f"First two element of tuple; {tuple2[:2]}")
# tuple2[0]="shyam"
# print(f"New tuple: {tuple2}")

# Above lines generates error

for item in tuple2:
    print (item)



