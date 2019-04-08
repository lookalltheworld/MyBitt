import os

def release_port(port):
    cmd='netstat -ano | findstr %s'%port
    print(cmd)
    result=os.popen(cmd).read()
    print(result)
    print(type(result))
    if str(port) and 'LISTENING' in result:
        i=result.index('LISTENING')
        start=i+len('LISTENING')+7
        end=result.index('\n')
        pid=result[start:end]
        cmd_kill='taskkill -f -pid %s'%pid
        print(cmd_kill)
        os.popen(cmd_kill)
    else:
        print('port %s is availabe!'%port)

if __name__=='__main__':
    release_port(4725)


