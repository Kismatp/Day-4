# # Creating a set 

# set1= set ()
# print(set1)
# print(type(set1))

# set2={1,2,3,3,4,4}
# print(set2)
# print(type(set2))

# # adding element in set 
# set2.add(5)
# print(set2)

# # Removing element from set 

# set2.discard(3)
# print(set2)

# set2.remove(5)
# print(set2)

# set2.discard(3)
# print(set2)

# Operations on set 
set3={1,2,3,4}
set4={3,4,5,6}
intersetction_set= set3.intersection(set4)
print(f"Intersection set: {intersetction_set}")

union_set= set3.union(set4)
print(f"Union set is: {union_set}")

difference_set=set4.difference(set3)
print(f"The difference set is: {difference_set}")

# Use case of set 
list1={"Kismat","ram","hari","sita","krishna","narayana"}
list2={"Kismat","ram","hari","krishna"}

set1=set(list1)
set2=set(list2)

common_std=set1.intersection(set2)
common_std=list(common_std)
print(f"The common students are: {common_std}")







