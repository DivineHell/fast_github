# *_*coding:utf-8 *_*
import add_dns

dns_list = ['140.82.113.3 github.com', '151.101.129.194 github.global.ssl.fastly.net',
            '151.101.193.194 github.global.ssl.fastly.net',
            '151.101.1.194 github.global.ssl.fastly.net',
            '151.101.65.194 github.global.ssl.fastly.net']


def test_add_dns():
    add_dns.add_dns('../<your test dns file>', dns_list)


if __name__ == '__main__':
    test_add_dns()