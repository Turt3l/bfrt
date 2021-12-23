import os
path = r"C:\Users\Liāna\PycharmProjects\pythonProject7"
os.chdir("folder")
count = 0
ui = input("Enter a prefix: ")
#time complexity: O(1)
for i in os.listdir():
    file_name, file_extension = os.path.splitext(i)
    print(file_extension)
    count += 1
    os.rename(i, str(ui)+str(count)+str(file_extension))
