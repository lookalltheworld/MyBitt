import  socket

def check_port(host,port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((host,port))
        s.shutdown(2)
    except OSError as msg:
        print('port %s is availble!'%port)
        print(msg)
        return True
    else:
        print('port %s is in use !'%port)
        return False

if __name__=='__main__':
    host='127.0.0.1'
    port=4725
    check_port(host,port)
