from ftplib import FTP as ftp_library #FTP Library from Python3 :D

def GetFTP_EU2():
    get_ftphtml = "ftp://ftp.europabarbarorum.org/CUF-src-dist.7z"
    return str(get_ftphtml)

def Main():
    ftplibr = ftp_library(host=GetFTP_EU2())
    ftplibr.login(user=str(""), passwd="")
    if ftplibr.connect(timeout=3000):
        print("Connected!!!")
        files = ftplibr.nlst()
        for file in files:
            print("Downloading!!! " + file)
            ftplibr.retrbinary("RETR " + file, open("C:\\EuropaBarbarorum2\\" + file, "wb").write)
    else:
        print("Failed to Connect FTP Site Europa Barbarorum II!!!")
        exit(3002)
if __name__ == "__main__":
    Main()