#create a tuples with 5 number

number_tuple=(1,2,3,4,5)

#access third element

third_ele=number_tuple[3]
print(third_ele)

#unpack tuples with sparte variable set

a,b,c,d,e=number_tuple
print(a)
print(b)
print(c)
print(d)
print(e)

#create a set of 5 fruits

fruits={"banana","apple","kiwi","orange","graps"}
print(fruits)

#add a new fruite in set
fruits.add("dragon fruit")
print(fruits)

#remove an element
fruits.remove("graps")
print(fruits)

#use of union intersection and subset

set_1={1,2,3,4,5,6,7,8,9,10}
set_2={1,2,3,7,10,11}

#union use
set_3=set_1.union(set_2)
print(set_3)

#intersection use 
set_4=set_1.intersection(set_2)
print(set_4)

#subset use
set_5=set_1.issubset(set_2)
print(set_5)

#create list with duplicate value then remove using set

duplicate_list=[2,3,1,1,2,2,4,4,5,5,5]
new_list=set(duplicate_list)
print(new_list)

#create Dictionary which contian student marks and name

Student={
    "vansh":90,
    "parth":80,
    "ronak":85,
    "shreyash":91
}

#Add new key and value
Student["parshu"]=96

#delete key value pair
Student.pop("parshu")
print(Student)

#marge two dictionary in one dictionry
Student={
    "vansh":90,
    "parth":80,
    "ronak":85,
    "shreyash":91
}
New_Student={
    "mit":95
}
Student.update(New_Student)
print(Student)

#cheak if a key exists 

Student={
    "vansh":90,
    "parth":80,
    "ronak":85,
    "shreyash":91
}
if "parth" in Student:
    print("key exists")
else:
    print("key not exists")

#count word frequency in string using dicitionry
string="python is popular programing language"
frequency={}
for i in string:
    if i not in frequency:
        frequency[i]=1
    else:
        frequency[i]+=1
print(frequency)     

#find the key with maximam value
Student={
    "vansh":90,
    "parth":80,
    "ronak":85,
    "shreyash":91
}
maximum_mark=0
name=""
for name,marks in Student.items():
      if marks > maximum_mark:
          maximum_mark=marks
          name=name
print(name) 

#reverse key and value in dicitionary
Student={
    "vansh":90,
    "parth":80,
    "ronak":85,
    "shreyash":91
}
new_dict={}
for name,marks in Student.items():
      new_dict[marks,name]=name,marks
print(new_dict)    

#update the specific key
Student={
     "parth":98,
     'vansh':89
         }
Student["ronak"]=Student["vansh"] #when change key first write new key then old then del statment
del Student["vansh"]
print(Student)

#convert list of tuples into a dicitionary
data = [("parth", 98), ("vansh", 89), ("ronak", 85),("mit",87)]
dic=dict(data)
print(dic)