#String-------------------
print("METHODS FOR STRING")
s = "Tan_Patel"
 
s1 = s.upper()
print(s1)
s2 = s.lower()
print(s2)
s3 = s.capitalize()
print(s3)
s4 = s.title()
print(s4)
s5 = s.replace("_", " ")
print(s5)
s6 = s.split("_")
print(s6)
s7 = s.count("a")
print(s7)
s8 = s.find("Patel")
print(s8)
s9 = s.startswith("Tan")
print(s9)
s10 = s.endswith("Patel")
print(s10)
print()


#LIST-------------------
print("METHODS FOR LIST")
List=[24,9,2006]

l1=len(List)
print(l1)

List.append(2025)
print(List)

List.insert(1,15)
print(List)

List.remove(9)
print(List)

l2=List.pop()
print(l2)
print(List)

l3=List.index(24)
print(l3)

l4=List.count(24)
print(l4)

List.sort()
print(List)

List.reverse()
print(List)
print()



#TUPLE-------------------
print("METHODS FOR TUPLE")
Tuple=(24,9,2006,9)

t1=Tuple.count(9)
print(t1)

t2=Tuple.index(2006)
print(t2)
print()


#DICT-------------------
print("METHODS FOR DICT")
Dict={"Name":"Tan Patel","Age":19}

d1=Dict.keys()
print(d1)

d2=Dict.values()
print(d2)

d3=Dict.items()
print(d3)

d4=Dict.get("Name")
print(d4)

Dict.update({"Age":20})
print(Dict)

Dict.pop("Age")
print(Dict)
print()



#SETS--------------------------
print("METHODS FOR SETS")
Set={1,2,3}

Set.add(4)
print(Set)
print()

Set.update([5,6])
print(Set)
print()

Set.remove(2)
print(Set)
print()

Set.discard(10)
print(Set)
print()

s1=Set.union({7,8})
print(s1)
print()

s2=Set.intersection({3,4,5})
print(s2)
print()