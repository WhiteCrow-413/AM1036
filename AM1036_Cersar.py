def Ceasar_Crypt(data, number):
    dump_list = list(data)
    ascii_list = []
    string_list = []
    number = int(number)

    for i in range(len(dump_list)):
        ascii_list.append(ord(dump_list[i]))
        if(ascii_list[i] >= 65 and ascii_list[i] <= 90):
            ascii_list[i] += (number % 26)

            if(ascii_list[i] > 90):
                ascii_list[i] -= 26

            elif(ascii_list[i] < 65):
                ascii_list[i] += 26

        elif(ascii_list[i] >= 97 and ascii_list[i] <= 122):
            ascii_list[i] += (number % 26)

            if(ascii_list[i] > 122):
                ascii_list[i] -= 26
                
            elif(ascii_list[i] < 97):
                ascii_list[i] += 26

        string_list.append(chr(ascii_list[i]))
    
    dump = "".join(string_list).replace(" ", "")
        
    return dump