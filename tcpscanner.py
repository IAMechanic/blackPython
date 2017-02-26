import optparse
import socket
import time
import threading

screenlock=threading.Semaphore(value=1)
num=0
def connScan(tgthost,tgtport):

    try:
        
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((tgthost,tgtport))
        #num+=1
       # s.send('Violent python !!!\r\n')
        #result=s.recv(100)
        screenlock.acquire()
        print ('[+] %d / tcp open'  %tgtport)
       # print ('[+] '+str(result))
        
        screenlock.release()
        s.close()
        
    except:
        pass

          
def portScan(tgthost,tgtports):

    try :
         ip=socket.gethostbyname(tgthost)
    except:
         print ('[-] Unkonw  tgthost %d' %tgthost)
         return
    try:
         tgtname=socket.gethostbyaddr(ip)
         print ('\n [+] scan result for : '+tgtname(0) ) 
    except:
         print('\n[+] scan result for : '+ ip)
    socket.setdefaulttimeout(1)
    for tgtport in range(int(tgtports+1)):
        t=threading.Thread(target=connScan,args=(tgthost,tgtport))
        t.start()
        
        

def main():
    parse=optparse.OptionParser('usage %porg -H'+'<target host> -p <target port>')
    parse.add_option('-H',dest='tgthost',type='string',help='specify target host')
    parse.add_option('-P',dest='tgtport',type='int',help='specify target port')
    (options,args)=parse.parse_args()

    tgthost=options.tgthost
    tgtports=options.tgtport

    if (tgthost==None) | (tgtports==None)  :
      
       print (parse.usage)
       exit(0)
    portScan(tgthost,tgtports)
    
if __name__=="__main__":
    main()

