# 找到1~input的所有質數
print("Please input a number:")
user_input = input()

print("是質數的數值")
# 算出以下有多少質數
check_number = int(user_input)
x = check_number
while x !=1:
    y = x
    check_result = False
    while y !=1:
        if(x%y==0 and x!=y):
            check_result=True
        y=y-1
    if(check_result == False):
        print(x)
    x = x-1
