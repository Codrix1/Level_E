def ans_1():
    string = "encode"
    encoded = string.encode("utf-8")
    decoded = encoded.decode("utf-8")
    print(encoded)
    print(decoded)
    return


def ans_2():
    string = 890
    hexdecimal = hex(string)
    print(hexdecimal)
    return


def ans_3():
    # Import hashlib library (md5 method is part of it)
    import hashlib

    # File to check
    file_name = 'filename.exe'
    with open(file_name, 'rb') as file_to_check:
        data = file_to_check.read()    
        md5_returned = hashlib.md5(data).hexdigest()
    return

def main():
    # ans_1()
    ans_2()
    # ans_3()
    # ans_4()
    # ans_5()
    # ans_6()    
    # ans_7()
    # ans_8()
    # ans_9()
    # ans_10()
    return


if __name__ == "__main__":
    main()