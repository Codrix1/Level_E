def ans_1():
    print("hello Hacker")
    return

def ans_2():
    name = input("enter your name")
    print(f'Welcome, {name} ')
    return

def ans_3():
    string = "1337"
    number = int(string) + 10
    print(number)
    return

def ans_4():
    first = int(input("enter first number"))
    second = int(input ("eneter second number"))
    print(f'''
          Sum: {first+second}
          difference: {abs((first-second))}
          Product: {first * second}
          quotient: {first // second}    
          ''')
    return

def ans_5():
    def reverse(string):
        reverse = ""
        for i in range (len(string)-1 , -1 , -1):
            reverse += string[i]
        return reverse
    string = "rekcah_repus"
    print(reverse(string))
    return

def ans_6():
    def isodd(number):
        if number % 2 == 0:
            return False
        else:
            return True
    number = int(input("enter number:"))
    if (isodd(number)):
        print("number is odd")
    else: 
        print("number is even")
    return

def ans_7():
    store = True
    print(store)
    return 

def ans_8():
    string = "100101"
    dec = float(string)
    print(dec)
    return 

def ans_9():
    string = "H4ck3r"
    new=""
    for i in range(0,len(string)-1,2):
        new += string[i].lower()
        new += string[i+1].upper()
    print(new)
    return

def ans_10():
    string = "password"
    new = string
    for i in range( 0 , len(string) , 1):
        if string[i] in "aeiou":
            print (string[i])
            new = new.replace(string[i], "*" , -1)

    print(new)
    return


def main():
    ans_1()
    ans_2()
    ans_3()
    ans_4()
    ans_5()
    ans_6()
    ans_7()
    ans_8()
    ans_9()
    ans_10()

 
if __name__ == "__main__":
    main()