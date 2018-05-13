import ftplib
import os
import socket

HOST="ftp.mozilla.org"
DIRN="pub/mozilla.org/webtools"
FILE="bugzilla-LATEST.tar.gz"

def mian():
    try:
        f=ftplib.FTP(HOST)
    except(socket.error,socket.gaierror)as e:
        print("ERROR:cannot reach %s"%HOST)
        return
    print("***Connected to host %s"%HOST)

    try:
        f.login()
    except ftplib.error_perm:
        print("ERROR:connot login anonymousely")
        f.quit()
        return
    print("***Login in as 'anonymousely'")

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print("ERROR:cannot cd to %s"%DIRN)
        f.quit()
        return
    print("***Changed to %s folder"%DIRN)
    fp=open(r"D:/txt/FILE","wb")
    try:
        f.retrbinary("RETR %s"%FILE,fp.write())
    except ftplib.error_perm:
        print("ERROR:connot read file %s"%FILE)
        os.unlink(FILE)
    else:
        print("***Downloaded %s to CWD"%FILE)
    f.quit()
if __name__=="__main__":
    mian()