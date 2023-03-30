# Question: How to access elements of a set.
#Example 1
m={2,1,4,6}
print(4 in m)

#Example 2
a={"apple","banana","mango"}
print("kiwi" in a)

# Question: Difference between remove and discard functions in set.

#discard:- If the item to remove does not exist, discard() will not raise an error.
a={"apple","banana","mango"}
a.discard("banana")
print(a)
a.discard("kiwi")
print(a)

#remove:- If the item to remove does not exist, remove() will raise an error.
m={2,1,4,6}
m.remove(1)
print(m)
#m.remove(5)
#print(m)

# Question:- intersection_update()
a={"India","US","Korea"}
b={"UK","India"}
a.intersection_update(b)
print(a)

# Question:- symmetric_difference()
a={"India","US","Korea"}
b={"UK","India"}
a.symmetric_difference(b)
print(a)

#Question:- symmetric_difference_update()
a={"India","US","Korea"}
b={"UK","India"}
a.symmetric_difference_update(b)
print(a)

#Question:- dict()
x = dict(name = "Ankita", age = 23, country = "India")
print(x)
