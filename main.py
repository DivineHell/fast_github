# *_*coding:utf-8 *_*
import logging
import sys

import add_dns
import request_dns
from config import DNS_FILE

logging.basicConfig(level=logging.INFO, stream=sys.stdout,
                    format="%(asctime)s %(levelname)s: %(message)s")

if __name__ == '__main__':
    dns_list = request_dns.resolve_dns()
    add_dns.add_dns(DNS_FILE, dns_list)
