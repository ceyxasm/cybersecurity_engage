
#client side
#symmetric

import socket, os
from Crypto.Cipher import AES

host= "127.0.0.1"
port= 1337
key= b'sixteen bit key_'

def encrypt( data, key, iv):
    data+= ' '*( 16- len(data)%16) #padding
    cipher= AES.new( key, AES.MODE_CBC, iv)
    #cipher block chaining
    return cipher.encrypt( bytes(data, 'utf-8'))

message= 'very important confidential message'

with socket.socket( socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect( ( host, port))
    iv= os.urandom(16)
    s.send( iv)
    s.send( bytes( [len(message)]))
    encrypted= encrypt( message, key, iv)
    print('sending %s' %encrypted.hex())
    s.sendall( encrypted) 