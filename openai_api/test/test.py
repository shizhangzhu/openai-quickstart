list_demo = [1,2,3,4,[5,6]]
print(list_demo[0])
print(type(list_demo))
list_demo.insert(0,"first")
print(list_demo)
list_demo.extend("lastone")
print(list_demo)
list_demo.remove("first")
print(list_demo)
list_demo.reverse()
print(list_demo)
yuan = (1,2,3,4)
print(yuan)
set_demo = {1,2,3,4,5}
print(
    set_demo
)
set_demo.add(7)
print(set_demo)
set_demo.add(7)
print(set_demo)
dirt_demo = {'one':1,'two':2}
print(dirt_demo)
print(dirt_demo.items())
for key,value in dirt_demo.items():
    print(key)
    print(value)

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>下面是文件读取")
import pandas as pd
data = pd.read_csv("test.csv")
print(data)


with open("test.csv") as f:
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>开始读取文件")
    file_data = f.readlines()
    print(file_data)


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>开始存储db信息")
from tinydb import TinyDB

friend1 = {"name":file_data[0].split(",")[0], "source":file_data[0].split(",")[1], 'tel':file_data[0].split(",")[2]}
friend2 = {"name":file_data[1].split(",")[0], "source":file_data[1].split(",")[1], 'tel':file_data[1].split(",")[2]}
friend3 = {"name":file_data[2].split(",")[0], "source":file_data[2].split(",")[1], 'tel':file_data[2].split(",")[2]}

db = TinyDB("./db.json");
db.insert_multiple([
    friend1,
    friend2,
    friend3
])
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>输出db中数据")
print(db.all())

from tinydb import Query
friend = Query()
friend_info = db.search(friend.name == '张三')
print(friend_info)

if False :
    print("条件成立")
else:
    print("不成立")

http_respose_status = 404
match(http_respose_status):
    case 400:
        print("bad request")
    case 404:
        print("无法访问页面")

print(">>>>>>>>>>>>>>>>>>>这里开始输出while的函数")
number = 0
while number < 3:
    print(f"number is {number}")
    print(f"name={file_data[number].split(',')[0]},source={file_data[number].split(',')[1]},tel={file_data[number].split(',')[2]}")
    number +=1

list1 = [1,2,3,4,5,6,7]
while list1:
    print(list1.pop())

for key,value in friend1. items():
    print(key.capitalize())
    print(value)

for i in enumerate(friend1):
    print(i)