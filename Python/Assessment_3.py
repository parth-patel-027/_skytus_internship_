#write a string input and print its length 
string=str(input("Enter Your String:-"))
print(len(string))

#write a program to convert sentence in to lowecase
sentence="My Name Is PARTH Patel"
print(sentence.lower())

#write a program replace space with underscore
sentence="My name is Parth and i am student"
new_sentence=sentence.replace(" ","/")
print(new_sentence)

#extract the last and first character of string
string="parth"
print(string[0],string[4])

#reverse a string using sclicing

string="parthpatel"
print(string[::-1])

#count howmany times latter apears in a string

string="hii,my name is parth patel"
count_letter=string.count("a")
print(count_letter)

#write a program if word is present in sentence

sentence="hello,my name is parth and i am a student."
if "parth" in sentence:
    print("True")
else:
    print("False")

#take name and age and print using f string

Name=str(input("Enter Your Name:-"))
Age=int(input("Enter Your Age:-"))
print(f"My Name Is {Name}")
print(f"My Age Is {Age}")

#remove extra space starting and end of string
string="  python      "
print(string)
print(string.strip())

#join of list of word in single string - between them
list_word=["car","bike","cycle"]
join="-".join(list_word)
print(join)

#create a list five fevorite moive

movie_list=["k3","golmal","ABCD","dhoom","panchayat"]
print(movie_list)

 # for add new element in list
movie_list.append("bhootnath")
movie_list.remove("k3")
print(movie_list)

#sort the list of number acending order
list_number=[2,4,8,1,3,5,7,9,10]
list_number.sort()
print(list_number)

#reverse a list

list_number.reverse()
print(list_number)

#find the largest element in list

number=[3,5,4,8,90,65,33,21,22,1]
largest=max(number)
print(largest)

#marge two list in to one

list_car=["bmw","benz","maruti"]
list_prize=["8cr","1cr","10 lkh"]
list_car.extend(list_prize)
print(list_car)

#Access the last element of list without using index 
list_data=["list","tuple","set"]
last=list_data.pop()
print(last)

#created nested list and access inner element
list_car=["bmw","maruti",["hero","yamaha","hero"],"ford"]
inner_element=list_car[2][2]
print(inner_element)

#count how many times element apears in list
list_num=[2,3,4,5,5,56,7,2,2,4,3,2,34,2,2,2]
print(list_num.count(2))
