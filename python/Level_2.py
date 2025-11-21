def ans_1():
    password = input("enter the password: ")
    if(password == "s3cr3t"):
        print("correct")
    else:
        print("incorrect")
        ans_1()
    return

def ans_2():
    for i in range (1 , 101 , 1):
        if i % 4 != 0:
            print("i \n")
    return

def ans_3():
    for i in range(0 , 10000 , 1):
        if i < 10:
            print(f'000{str(i)}')
        elif i < 100:
            print(f'00{str(i)}')
        elif i <1000:
            print(f'0{str(i)}')
        else :
            print(i)    
    return

def ans_4():
    year = int(input("enter year: "))
    if year % 4 == 0 and year % 100 != 0:
        print("leap year")
    else:
        print("not leap year")
    return

def ans_5():
    number = int(input("enter number: "))
    prime = []
    notprime = []
    for i in range(2 , number+1 ,1):
        if not i in notprime:
            prime.append(i)
            product = 0
            inc = i
            while product < (number + 1):
                product = inc * i 
                print (product)
                notprime.append(product)
                inc += 1
    print(prime)            

def ans_6():
    def retry(tries):
        password = input("enter the password: ")
        if(password == "s3cr3t"):
            print("correct")
        else:
            print("incorrect")
            if tries > 1:
                tries -= 1 
                retry(tries)
        return
    retry(3)
    print("used up three attempts")
    return

import random
def ans_7():
    ran = random.randrange(0 , 11 , 1)
    guess = int(input("guess a number between 0 and 10: "))
    if ran == guess:
        print("correct")
        return
    print("incorrect")
    return

def ans_8():
    for i in range(1 , 101 , 1):
        word = str(i)
        if i % 3 == 0:
            word = "fizz"
        if i % 5 == 0:
            if word == "fizz":
                word = "fizzbuzz"
            else:
                word = "buzz"
        print(word)
def ans_9():
    def retry():
        password = input("enter the password: ")
        if(password == "s3cr3t"):
            print("correct")
        else:
            print("incorrect retry")
            retry()
        return
    retry()
    return
def ans_10():
    def reverse(string):
        reverse = ""
        for i in range (len(string)-1 , -1 , -1):
            reverse += string[i]
        return reverse
    string = input("enter the palindrome string: ")
    if string == reverse(string):
        print ("palindrome")
    else:
        print("not a palindrome")
    return
def main():
    ans_1()
    # ans_2()
    # ans_3()
    # ans_4()
    # ans_5()
    # ans_6()    
    # ans_7()
    # ans_8()
    # ans_9()
    # ans_10()

 
if __name__ == "__main__":
    main()