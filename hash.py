import hashlib
import base64
from os import extsep
from urllib import parse

def Base64_Encode(data):
    try:
        e_code = base64.b64encode(data.encode("UTF-8"))
        base_encode = e_code.decode("UTF-8")
        return base_encode

    except BaseException:
        pass

def Base64_Decode(data):
    try:
        d_code = base64.b64decode(data.encode('utf-8'))
        base_decode = d_code.decode("UTF-8")
        return base_decode

    except BaseException:
        pass


def Url_Encode_Hangle(data):
    try:
        url_encode_hangle = parse.quote(data)
        return url_encode_hangle

    except BaseException:
        pass

def Url_Decode_Hangle(data):  # 미완
    try:
        url_decode_hangle = parse.unquote(data)
        return url_decode_hangle
    except BaseException:
        pass


def Url_Encode_English(data):
    try:
        length = 2
        url_dump = list()
        map(''.join, zip(*[iter(data)] * length))
        for i in data:
            url_dump.append('%' + hex(ord(i))[2:])

        url_dump = "".join(url_dump).replace(" ", "")
        return url_dump
    except BaseException:
        pass

def Url_Decode_English(data):
    try:
        length = 3
        url_dump = list()
        url_dump_hex = list()
        url_dump_dec = list()
        url_dump_ascii = list()
        data_dump = [data[i:i + length] for i in range(0, len(data), length)]
        for i in data_dump:
            url_dump.append(i.replace("%", ""))
        for i in url_dump:
            url_dump_hex.append("0x" + i)
        for i in url_dump_hex:
            url_dump_dec.append(int(i, 16))
        for i in url_dump_dec:
            url_dump_ascii.append(chr(i))
        url_decode = "".join(url_dump_ascii).replace(" ", "")
        return url_decode

    except BaseException:
        pass


def Ascii_Encode(data):
    try:
        length = 1
        ascii_dump = list()
        list_data = [data[i:i + length] for i in range(0, len(data), length)]
        for i in list_data:
            ascii_dump.append(str(ord(i)))
        ascii_encode = " ".join(ascii_dump)
        return ascii_encode

    except BaseException:
        pass

def Ascii_Decode(data):
    try:
        if ' ' in data:
            list_data = data.split(' ')
            ascii_dump = list()

            for i in list_data:
                ascii_dump.append(chr(int(i)))
            ascii_encode_list = "".join(ascii_dump)
            return ascii_encode_list
        else:
            ascii_decode = chr(int(data))
            return ascii_decode

    except BaseException:
        pass


def MD5_Encode(data):
    try:
        text = data.encode("UTF-8")
        m = hashlib.md5()
        m.update(text)
        md5_encode = m.hexdigest()
        return md5_encode
    
    except BaseException:
        pass

def MD5_Encode_F(data):
    try:
        f = open(data,'rb')

        f_data = f.read()
        md5_f_encode = hashlib.md5(f_data).hexdigest()
        return md5_f_encode
    
    except BaseException:
        pass


def SHA1_Encode(data):
    try:
        text = data.encode("UTF-8")
        m = hashlib.sha1()
        m.update(text)
        sha1_encode = m.hexdigest()
        return sha1_encode

    except BaseException:
        pass

def SHA1_Encode_F(data):
    try:
        f = open(data,'rb')

        f_data = f.read()
        sha1_f_encode = hashlib.sha1(f_data).hexdigest()
        return sha1_f_encode

    except BaseException:
        pass


def SHA256_Encode(data):
    try:
        text = data.encode("UTF-8")
        m = hashlib.sha256()
        m.update(text)
        sha256_encode = m.hexdigest()
        return sha256_encode

    except BaseException:
        pass

def SHA256_Encode_F(data):
    try:
        f = open(data,'rb')

        f_data = f.read()
        sha256_f_encode = hashlib.sha256(f_data).hexdigest()
        return sha256_f_encode

    except BaseException:
        pass


def SHA512_Encode(data):
    try:
        text = data.encode("UTF-8")
        m = hashlib.sha512()
        m.update(text)
        sha512_encode = m.hexdigest()
        return sha512_encode
    
    except BaseException:
        pass

def SHA512_Encode_F(data):
    try:
        f = open(data,'rb')

        f_data = f.read()
        sha512_f_encode = hashlib.sha512(f_data).hexdigest()
        return sha512_f_encode

    except BaseException:
        pass


'''
print(Bin_Number(input_data))
print(Oct_Number(input_data))
print(Hex_Number(input_data))
print(Base64_Encode(input_data))
print(Base64_Decode(input_data))
print(Ascii_Encode(input_data))
print(Ascii_Decode(input_data))
print(Url_Encode_English(input_data))
print(Url_Encode_Hangle(input_data))
print(Url_Decode_Hangle(input_data))
print(Url_Decode_English(input_data))
'''