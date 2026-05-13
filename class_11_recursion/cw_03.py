def sum_p(num):
    if num<10:
        return num
    return (num%10)+sum_p(num//10)
print(sum_p(1234))