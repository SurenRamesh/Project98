print("Choose the file number")
print("1. sample1.txt")
print("2. smaple2.txt")
file1 = int(input("Enter your file to take the data from:"))
file2 = int(input("Enter the file to where you want to transfer your data:"))


def swapFileData(data_a, data_b):
    with open("sample1.txt", "r") as a:
        data_a = a.read()

    with open("sample2.txt", "r") as b:
        data_b = b.read()
    
    with open("sample1.txt", "w") as a:
        a.write(data_b)
    
    with open("sample2.txt", "w") as b:
        b.write(data_a)

swapFileData(file1, file2)

    