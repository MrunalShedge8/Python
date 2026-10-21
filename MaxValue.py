# Find max value using *args
def get_max(*num):
    if len(num)==0:
        return None
    max_num = num[0]
    for i in num:
        if i>max_num:
            max_num=i
        return max_num
print(get_max(3, 12 , 32, 45, 31))
print(get_max("Ro","ASHISH","Arush", "mrunal"))        