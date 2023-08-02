file_names = ["demo1.txt","demo2.txt","demo3.txt"]
file_data = []
for file_name in file_names:
    with open(file_name,mode='r') as f:
        data = f.read()
        file_data.append(data)
    print(data)

with open("demo4.txt",mode='w') as f:
    for data in file_data:
        f.write(data)