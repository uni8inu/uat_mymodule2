# This is sample of test module
# input() * 5 times / print() * 5 times

my_dic = {}
for i in range(5):
    my_dic[str(i)] = input()

for i in range(5):
    print("out: " , my_dic[str(i)])
