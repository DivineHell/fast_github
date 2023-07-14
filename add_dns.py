# *_*coding:utf-8 *_*
import logging
import os

from config import GIT_URL

marker = '# add github dns by fast_github'


def add_dns(file, update_dnses):
    with open(file, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        f.truncate()
        for line in lines:
            if line.strip('\n') == marker:
                continue

            x = line.strip('\n').split(' ')
            if len(x) < 2:
                f.write(line)
                continue

            # remove old dns
            if x[1] not in GIT_URL:
                f.write(line)

        logging.info(f'add dns to {file}')
        f.write(f'{marker}')
        # insert new dns
        for one in update_dnses:
            f.write(f'\n{one}')

    flush_dns()


def flush_dns():
    os.system('sudo -S killall -HUP mDNSResponder; echo "Flush dns successful!"')
