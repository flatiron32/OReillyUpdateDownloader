import sys
from datetime import date
from ftplib import FTP

if len(sys.argv) < 2:
    print("No username provided")
    exit(-1)
if len(sys.argv) < 3:
    print("No password provided")
    exit(-1)

ftp = FTP("direct-sfs-us-east-1.docevent.io")
ftp.login(sys.argv[1], sys.argv[2])
today = date.today()

for n in range(1, 4):
    filename = today.strftime(f"OR%a_{n}_%m%d%y").upper()
    fullname = f"{filename}.mp3"
    with open(fullname, "wb") as fp:
        print(f"Getting {fullname}")
        ftp.retrbinary(f"RETR {fullname}", fp.write)

ftp.quit()
