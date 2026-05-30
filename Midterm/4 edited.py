num = int(input('Enter 16-digit credit card number: '))
total = 0

for digit in str(num):
    total += int(digit)

print(total)

first_second = 2*int((num / (10**14))%10)
total -= int((num / (10**14))%10)
if first_second > 9:
    first_second = int((first_second/10) + (first_second%10))
    
sec_second = 2*int((num / (10**12))%10)
total -= int((num / (10**12))%10)
if sec_second > 9:
    sec_second = int((sec_second/10) + (sec_second%10))
    
third_second = 2*int((num / (10**10))%10)
total -= int((num / (10**10))%10)
if third_second > 9:
    third_second = int((third_second/10) + (third_second%10))
    
fourth_second = 2*int((num / (10**8))%10)
total -= int((num / (10**8))%10)
if fourth_second > 9:
    fourth_second = int((fourth_second/10) + (fourth_second%10))
    
fifth_second = 2*int((num / (10**6))%10)
total -= int((num / (10**6))%10)
if fifth_second > 9:
    fifth_second = int((fifth_second/10) + (fifth_second%10))
    
sixth_second = 2*int((num / (10**4))%10)
total -= int((num / (10**4))%10)
if sixth_second > 9:
    sixth_second = int((sixth_second/10) + (sixth_second%10))
    
seventh_second = 2*int((num / (10**2))%10)
total -= int((num / (10**2))%10)
if seventh_second > 9:
    seventh_second = int((seventh_second/10) + (seventh_second%10))
    
last_digit = int(num%10)
print(last_digit)
print(seventh_second)

print(total)
total += (first_second + sec_second + third_second + fourth_second + fifth_second + sixth_second + seventh_second)
print(total)
total += last_digit
print(total)

if total % 10 == 0:
    print("This is a valid card number.")
else:
    print("This is not a valid card number.")
