import hashlib
import base64
from os import extsep
from urllib import parse

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