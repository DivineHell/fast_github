# *_*coding:utf-8 *_*
import logging
import re
import sys

import requests

from config import GIT_URL, DNS_WEB

http_header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}


def resolve_dns():
    dns_result = []
    for url in GIT_URL:
        link = f'{DNS_WEB}/site/{url}'
        try:
            res = requests.get(link, headers=http_header)
            ips = parse(res.text)
            for i in ips:
                dns_result.append(f'{i} {url}')
        except Exception as e:
            logging.error(e)
            sys.exit(1)

    logging.info('will add dns:\n\t{res}'.format(res='\n\t'.join(dns_result)))
    return dns_result


def parse(raw):
    res = re.findall(r'<strong>((?:\d+\.){3}\d+)</strong>', raw)
    return set(res)
