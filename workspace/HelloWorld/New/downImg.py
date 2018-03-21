import random
import urllib.request

def download(url):
    n=random.randrange(1,1000)
    fn=str(n)+".jpg"
    urllib.request.urlretrieve(url,fn)
download("http://dailydropcap.com/images/N-7")