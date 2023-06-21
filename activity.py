#CREATE A FILE
# file2 = open("Jamal.txt",'w')

#READ A FILE
file1 = open("anything.txt")
content = file1.read()
# linestorage = file1.readlines()
# for power in linestorage:
#     print(power)


#LIST 
fruits = ["pineapple", "banana", "apple"]
length = len(fruits)
fruits.append("Orange")
# print(fruits)
# print(fruits.pop(1))
# print(length)
# print(fruits[1])
# for ii in fruits: 
#     print(ii)


#SPLIT FUNCTION
apart = "Hallo! Welcome to Dubai!!"
words = apart.split()
# print(words)


def countwords():
    
  filename = input("Enter the file name: ")
  count = 0
  file = open(filename, 'r')
  for word in file:
    words = word.split()
    count = count + len(words)
  
  print("Number of words:", count)
    

countwords()