import argparse

parser = argparse.ArgumentParser(description="这个程序是用来演示的")
parser.add_argument("-number1",type=int,default=10,help="这是第一个数字")
parser.add_argument("-number2",type=int,default=20,help="这是一个数字")
args = parser.parse_args()
print(f"你输入的参数是{args.number1+args.number2}")