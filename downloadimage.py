import random
import urllib.request

def download_image(url):
    x = random.randrange(1,10)
    a = str(x) + ".pdf"
    urllib.request.urlretrieve(url, a)

download_image("https://mail.google.com/mail/u/0/?ui=2&ik=e6453611be&view=att&th=15d87b55084f2063&attid=0.1&disp=safe&zw")