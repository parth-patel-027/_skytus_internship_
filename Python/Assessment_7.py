#-----------------------------FILE HANDLING------------------------------------------------------#
#TASK 1
#write a program read file and display it content

f=open("intro.txt","r")
data=f.read()
f.close()
print(data)

#TASK 2
# #write a program to count number of line a read file

f=open("intro.txt","r")
count=0
for line in f:
    if line.strip():
     count+=1
f.close()
print(count)   

#TASK 3
#write a program to count each word appears in file

f = open("intro.txt", "r")
data=f.read()
word_count={}
for word in data.split():
    if word not in word_count:
         word_count[word]=1
    else:
         word_count[word] +=1
f.close()         
print(word_count)     

#TASK 4
#write a program 5 user write in a file

f=open("intro.txt","a")

for i in range(1,6):
    sentence=input("Enter Your Senetce:-")
    f.write(sentence + "\n")
f.close()

#TASK 5
#write a program append list of string to en exiting file.

f=open("intro.txt","a")
string_list=["mango","apple","banana","kiwi"]
for string in string_list:
 f.write(string + "\n")      
f.close()

#TASK 6
#write a program print only that line which contain particular word

f=open("intro.txt","r")
data=f.read()
for line in data.splitlines():
     if "python" in line:
        print(line)
     else:
        pass
f.close()    

#TASK 7
#write a program to replace specific word in file and save change.

f=open("intro.txt","r+")
data=f.read()
if "PYTHON" in data:
 new_line=data.replace("PYTHON","python") 
 f.seek(0)
 f.write(new_line)
 f.truncate()       
f.close()

#TASK 8
#write a program to merge two filw content in to third file

with open("frist_file.txt","r") as f1:
    data1=f1.read()
with open("sec_file.txt","r") as f2:
    data2=f2.read()
with open("third_file.txt","w+") as f3:
   f3.write(data1)
   f3.write("\n")
   f3.write(data2)

#TASK 9
#write a program to read CSV file and display it content in formated way.

import csv
with open("customers.csv","r") as f1:
    reader =csv.DictReader(f1)
    for i  in reader:
        print(i)
#TASK 10    
#write a program backup a file copying its contents into another file.

with open("third_file.txt","r") as f1:
     data1=f1.read()
with open("backup.txt","w+") as f2:
     data2=f2.write(data1)     
