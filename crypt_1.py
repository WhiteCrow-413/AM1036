import base64
from Cryptodome.PublicKey import RSA
from Cryptodome import Random
from Cryptodome.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Cryptodome.Cipher import PKCS1_OAEP


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


def Symmetric_Encrypt(data, data_list): #이게 암호화인지 복호화인지 헷갈림
    dump_list = list(data)
    crypt_list = []
    
    for i in range(len(dump_list)):
        for j in range(len(data_list)):
            if(dump_list[i] >= 'A' and dump_list[i]<='Z'):
                if(int(ord(dump_list[i]))-65 == j): 
                    crypt_list.append(data_list[j])
                    if(crypt_list[i] >= 'a'):
                        crypt_list[i] = chr(int(ord(crypt_list[i]))-32)

            elif(dump_list[i] >= 'a' and dump_list[i]<='z'):
                if(int(ord(dump_list[i]))-97 == j):
                    crypt_list.append(data_list[j]) 
                    if(crypt_list[i] < 'a'):
                        crypt_list[i] = chr(int(ord(crypt_list[i]))+32)

            elif(dump_list[i] >= '!' and dump_list[i] <= '/'):
                if(int(ord(dump_list[i]))-7 == j):
                    crypt_list.append(data_list[j])
            
            elif(dump_list[i] >= ':' and dump_list[i] <= '@'):
                if(int(ord(dump_list[i]))-17 == j):
                    crypt_list.append(data_list[j])
            elif(dump_list[i] >= '[' and dump_list[i] <= '`'):
                if(int(ord(dump_list[i]))-43 == j):
                    crypt_list.append(data_list[j])
            elif(dump_list[i] >= '{' and dump_list[i] <= '~'):
                if(int(ord(dump_list[i]))-69 == j):
                    crypt_list.append(data_list[j])


    crypt_list = ''.join(crypt_list)

    return crypt_list
#복호화 만들어야지...
def Symmetric_Decrypt(data, data_list): #얘가 암호화냐 복호화냐...
    dump_list = list(data)
    crypt_list = []

    for i in range(len(dump_list)):
        for j in range(len(data_list)):
            if(dump_list[i] >= 'A' and dump_list[i]<='Z'):
                if(int(ord(dump_list[i]))== int(ord(data_list[j])) or int(ord(dump_list[i])) == int(ord(data_list[j]) - 32)): 
                    crypt_list.append(chr(65+j))

            elif(dump_list[i] >= 'a' and dump_list[i]<='z'):
                if(int(ord(dump_list[i])) == int(ord(data_list[j])) or int(ord(dump_list[i])) == int(ord(data_list[j]) + 32)):
                    crypt_list.append(chr(97+j)) 

            elif(dump_list[i] >= '!' and dump_list[i] <= '/'):
                if(int(ord(dump_list[i]))== int(ord(data_list[j]))):
                    crypt_list.append(chr(7+j))
            
            elif(dump_list[i] >= ':' and dump_list[i] <= '@'):
                if(int(ord(dump_list[i]))== int(ord(data_list[j]))):
                    crypt_list.append(chr(17+j))
            elif(dump_list[i] >= '[' and dump_list[i] <= '`'):
                if(int(ord(dump_list[i]))== int(ord(data_list[j]))):
                    crypt_list.append(chr(43+j))
            elif(dump_list[i] >= '{' and dump_list[i] <= '~'):
                if(int(ord(dump_list[i]))== int(ord(data_list[j]))):
                    crypt_list.append(chr(69+j))


    crypt_list = ''.join(crypt_list)

    return crypt_list

#RSA!!!!!!
'''******************
주의 사항 : 
-경로를 입력할 시에는 마지막에 /를 붙여줘야함,
입력하지 않을 경우는 필요 없음
암호화 텍스트 파일 이름을 무조건 encrypted_data.bin으로 설정해야 함
다른 키 값 파일들도 private.pem | public.pem으로 설정해야 함 -> 이 부분은 시간 남으면 이름 상관없이하도록 하겠음

사용법!!!!!!!!!!!!!!!!!!!!!!!!!
1. Create_Key함수에서 private키와 public키를 생성
2. 평문을 RSA_Encode함수를 사용하여 RSA로 암호화 - public키 사용
3. RSA암호문을 RSA_Decode함수로 복호화 - private키 사용
- '''

def Create_Key(path): #개인 키 생성 후 파일에 저장
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator)
    private_key = key.export_key()

    f = open(path+"private.pem",'wb')
    f.write(private_key)

    f.close()

    public_key = key.publickey().export_key()

    f = open(path+"public.pem",'wb')
    f.write(public_key)

    f.close()


#개인키 값 리턴하는 함수
def Read_Pri_Key(path):
    f = open(path+"private.pem",'rb')
    
    read_pri_key = f.read()
    
    read_pri_key = str(read_pri_key)
    read_pri_key = read_pri_key.replace("b'-----BEGIN RSA PRIVATE KEY-----","")
    read_pri_key = read_pri_key.replace("-----END RSA PRIVATE KEY-----'","")
    read_pri_key = read_pri_key.replace("\\n","")
    f.close()

    return read_pri_key

#공개키 값 리턴하는 함수
def Read_Pub_Key(path):
    f = open(path+"public.pem",'rb')

    read_pub_key = f.read()

    read_pub_key = str(read_pub_key)
    read_pub_key = read_pub_key.replace("b'-----BEGIN PUBLIC KEY-----","")
    read_pub_key = read_pub_key.replace("-----END PUBLIC KEY-----'","")
    read_pub_key = read_pub_key.replace("\\n","")
    
    f.close()

    return read_pub_key

    
#여기 암호화 참고 : https://pycryptodome.readthedocs.io/en/latest/src/examples.html#generate-an-rsa-key
#여기 복호화 참고2 : https://comdoc.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%95%94%ED%98%B8%ED%99%94
def RSA_PKCS1_v1_5_Encode(path,data):
    pub_key = RSA.import_key(open(path+"public.pem").read())

    cipher = Cipher_pkcs1_v1_5.new(pub_key)
    msg = data.encode('utf-8')

    default_encrypt_length = 245
    length = default_encrypt_length

    msg_list = [msg[i:i + length] for i in list(range(0,len(msg), length))]
    encrypt_msg_list = []
    encrypt_msg = []

    for msg_str in msg_list:
        cipher_text = base64.b64encode(cipher.encrypt(msg_str))
        encrypt_msg_list.append(cipher_text)
        
    
    f = open(path + "encrypted_data.txt",'wb')

    for i in encrypt_msg_list:
        f.write(i)

    f.close()
    encrypt_msg = "".join(str(encrypt_msg_list)).replace("[b'","")
    encrypt_msg = encrypt_msg.replace("']","")

    return encrypt_msg

def RSA_PKCS1_v1_5_Decode(path):
    try:
        random_generator = Random.new().read

        pri_key = RSA.importKey(open(path+"private.pem").read())

        cipher = Cipher_pkcs1_v1_5.new(pri_key)

        msg_list = []

        f = open(path+"encrypted_data.txt",'rb')

        encrypt_read = f.read()

        f.close()
    
        encrypt_msg_list = base64.decodebytes(encrypt_read)
        de_str = cipher.decrypt(encrypt_msg_list,random_generator)
        msg_list = de_str.decode('utf-8')

        return msg_list

    except BaseException:
        pass
#여기 위로는 인증에서 자주 사용되는 PKCS#1 v1.5 방식
#################################################################
#여기 아래로는 암호문으로 자주 사용되는 PKCS-OAEP방식
def RSA_OAEP_Encode(path, data):
    data_utf = data.encode('utf-8')
    public_key = RSA.importKey(open('public.pem').read())
    cipher = PKCS1_OAEP.new(public_key)
    cipher_text = base64.b64encode(cipher.encrypt(data_utf))
    

    f = open(path + "encrypted_data.txt",'wb')

    f.write(cipher_text)

    f.close()

    encypt_msg = str(cipher_text).replace("b'","")
    encypt_msg = encypt_msg.replace("'","")

    return encypt_msg

def RSA_OAEP_Decode(path):
    try:
        private_key = RSA.importKey(open('private.pem').read())
        cipher = PKCS1_OAEP.new(private_key)

        f = open(path + 'encrypted_data.txt', 'rb')

        encrypt_read = f.read()

        f.close()

        encrypt_msg_list = base64.decodebytes(encrypt_read)
        de_str = cipher.decrypt(encrypt_msg_list)
        msg_list = de_str.decode('utf-8')

        return msg_list

    except BaseException:
        pass


#대칭함수 순서 abcdefghijklmnopqrstuvwxyz!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 넣어야함