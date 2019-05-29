#!/usr/bin/env python

##線上收聽古典音樂台
import time
import base64
import hashlib
import urllib
from urllib.parse import urlparse, urlencode, urljoin
#import urllib2
from urllib.request import urlopen
import subprocess
from collections import OrderedDict

def gen_token(path, timestamp, ip_addr, token_ord):
    const_str = 'radio@himediaservice#t'
    cat_str = path + str(timestamp) + ip_addr.decode('utf-8') + const_str + str(token_ord)
    hashed = hashlib.md5(cat_str.encode('utf-8')).digest()
    b64_md5hash = base64.b64encode(hashed)
    return b64_md5hash.decode('utf-8').replace('+', '-').replace('/', '_').replace('=', '')

def build_url():
    base_url = 'https://radio-hichannel.cdn.hinet.net/'
    ip_addr = urlopen('http://ipinfo.io/ip').read().rstrip()
    path = '/live/pool/hich-ra000081/ra-hls/'
    expire1 = int(time.time())
    expire2 = expire1 + (60 * 60 * 8)
    params = OrderedDict([
        ('token1', gen_token(path, expire1, ip_addr, 1)),
        ('token2', gen_token(path, expire2, ip_addr, 2)),
        ('expire1', expire1),
        ('expire2', expire2)
    ])
    params_str = urlencode(params)
    return urljoin(base_url, path + 'hich-ra000081-audio_track=128000.m3u8?') + '?' + params_str

def check_url_alive(url):
    try:
        urlopen(url)
        return True
    except urllib.error.HTTPError:
        return False

def ffplay(source):
    _prefix_url = "ffmpeg://{}".format(source)
    print("HIT RETURN TO QUIT\n")
    subprocess.call(['mplayer', '-msglevel', 'all=-1',
                     '-cache', '1024', _prefix_url])

def main():
    is_alive = None
    while is_alive != True:
        url = build_url()
        print(url)
        is_alive = check_url_alive(url)

    try:
        ffplay(url)
    except KeyboardInterrupt:
        exit()

if __name__ == '__main__':
    main()
