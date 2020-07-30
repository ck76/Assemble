import os

files=os.listdir()
result_files=[]
for item in files:
    haha=item.split(".")[0]
    result_files.append(haha)
print(result_files)
print(files)

print(type(files[0]))
print(type(result_files[0]))
bookname="result"
print(bookname in result_files)
