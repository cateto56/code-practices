# palingdrome detector

def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return True
    else:
        return False

def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = (yield num)
            print(i)
            if i is not None:
                print("value of i: ",i)
                num = i
        num += 1        
                        
pal_gen = infinite_palindromes()
for j in pal_gen:
    digits = len(str(j))
    print(j)
    #pal_gen.send(10 ** (digits))