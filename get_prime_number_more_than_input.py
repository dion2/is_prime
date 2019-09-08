# 找到筆輸入值更大的第一個質數
print("Please input a number:")
user_input = input()

print("找比輸入值更大的第一個")
# 找出質數的function
def is_prime(x):
    check_result = False
    y=x
    while y != 1:
        if(x % y == 0 and x != y):
            check_result = True
        y = y-1
    if(check_result == False):
        return True
    else:
        return False

check_number = int(user_input)
x = check_number
check_result = False
while (check_result == False):
    x = x+1
    check_result = is_prime(x)

print (x)