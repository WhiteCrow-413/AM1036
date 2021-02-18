# 2진수 
def Oct_Number_BIN(data):
    try:
        list_data = data.split(' ')
        bin_conversion = list()
        dec_conversion = list()
        oct_dump = list()

        for i in list_data:
            bin_conversion.append("0b"+i)
        for i in bin_conversion:
            dec_conversion.append(int(i,2))
        for i in dec_conversion:
            oct_dump.append(oct(i))
            
        oct_num_list = " ".join(oct_dump)
        return oct_num_list

    except BaseException:
        pass

def Dec_Number_BIN(data):
    try:
        list_data = data.split(' ')
        bin_conversion = list()
        str_conversion = list()
        dec_dump = list()

        for i in list_data:
            bin_conversion.append("0b"+i)
        for i in bin_conversion:
            dec_dump.append(int(i,2))
        for i in dec_dump:
            str_conversion.append(str(i))
            
        dec_num_list = " ".join(str_conversion)
        return dec_num_list
    
    except BaseException:
        pass

def Hex_Number_BIN(data):
    try:
        list_data = data.split(' ')
        bin_conversion = list()
        dec_conversion = list()
        hex_dump = list()

        for i in list_data:
            bin_conversion.append("0b" + i)
        for i in bin_conversion:
            dec_conversion.append(int(i,2))
        for i in dec_conversion:
            hex_dump.append(hex(i))
            
        hex_num_list = " ".join(hex_dump)
        return hex_num_list
    
    except BaseException:
        pass

# 8진수
def Bin_Number_OCT(data):
    try:
        list_data = data.split(' ')
        oct_convertion = list()
        dec_convertion = list()
        bin_dump = list()

        for i in list_data:
            oct_convertion.append("0o"+i)
        for i in oct_convertion:
            dec_convertion.append(int(i,8))
        for i in dec_convertion:
            bin_dump.append(bin(i))
            
        bin_num_list = " ".join(bin_dump)
        return bin_num_list
    
    except BaseException:
        pass

def Dec_Number_OCT(data):
    try:
        list_data = data.split(' ')
        oct_conversion = list()
        str_conversion = list()
        dec_dump = list()

        for i in list_data:
            oct_conversion.append("0o"+i)
        for i in oct_conversion:
            dec_dump.append(int(i,8))
        for i in dec_dump:
            str_conversion.append(str(i))
            
        dec_num_list = " ".join(str_conversion)
        return dec_num_list
    
    except BaseException:
        pass

def Hex_Number_OCT(data):
    try:
        list_data = data.split(' ')
        oct_conversion = list()
        dec_conversion = list()
        hex_dump = list()

        for i in list_data:
            oct_conversion.append("0o" + i)
        for i in oct_conversion:
            dec_conversion.append(int(i,8))
        for i in dec_conversion:
            hex_dump.append(hex(i))
        
        hex_num_list = " ".join(hex_dump)
        return hex_num_list
    
    except BaseException:
        pass

# 10진수 
def Bin_Number_DEC(data):
    try:
        list_data = data.split(' ')
        bin_dump = list()

        for i in list_data:
            bin_dump.append(bin(int(i)))

        bin_num_list = " ".join(bin_dump)
        return bin_num_list
    except BaseException:
        pass

def Oct_Number_DEC(data):
    try:
        list_data = data.split(' ')
        oct_dump = list()


        for i in list_data:
            oct_dump.append(oct(int(i)))

        oct_num_list = " ".join(oct_dump)
        return oct_num_list

    except BaseException:
        pass

def Hex_Number_DEC(data):
    try:
        list_data = data.split(' ')
        hex_dump = list()

        for i in list_data:
            hex_dump.append(hex(int(i)))

        hex_num_list = " ".join(hex_dump)
        return hex_num_list

    except BaseException:
        pass
        
# 16진수
def Bin_Number_HEX(data):
    try:
        list_data = data.split(' ')
        dec_convertion = list()
        hex_convertion = list()
        bin_dump = list()

        for i in list_data:
            hex_convertion.append("0x"+i)
        for i in hex_convertion:
            dec_convertion.append(int(i,16))
        for i in dec_convertion:
            bin_dump.append(bin(i))
        
        bin_num_list = " ".join(bin_dump)
        return bin_num_list
    
    except BaseException:
        pass

def Oct_Number_HEX(data):
    try:
        list_data = data.split(' ')
        dec_conversion = list()
        hex_conversion = list()
        oct_dump = list()

        for i in list_data:
            hex_conversion.append("0x"+i)
        for i in hex_conversion:
            dec_conversion.append(int(i,16))
        for i in dec_conversion:
            oct_dump.append(oct(i))
        
        oct_num_list = " ".join(oct_dump)
        return oct_num_list

    except BaseException:
        pass

def Dec_Number_HEX(data):
    try:
        list_data = data.split(' ')
        hex_conversion = list()
        str_conversion = list()
        dec_dump = list()

        for i in list_data:
            hex_conversion.append("0x"+i)
        for i in hex_conversion:
            dec_dump.append(int(i,16))
        for i in dec_dump:
            str_conversion.append(str(i))
        
        dec_num_list = " ".join(str_conversion)
        return dec_num_list
        
    except BaseException:
        pass