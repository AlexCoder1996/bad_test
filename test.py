import re

f1 = open('file1', 'r')
file1 = f1.read()
f1.close()
list1 = re.findall(r'(?<=user: )\w*', file1)

f2 = open('file2', 'r')
file2 = f2.read()
f2.close()
list2 = re.findall(r'(?<=user: )\w*', file2)

result = list(set(list1) - set(list2))
print(len(result))
print(result)

input('Press ENTER to exit') 