# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created by CWENG at 2020-11-04
Current project: VeldiPython


"""

import argparse
from server_communication_handler import post_message

parser = argparse.ArgumentParser(description='Process input arg.')
parser.add_argument('--signal',
                    help='python main.py --signal "your message"')

args = parser.parse_args()

print(post_message(r'http://127.0.0.1:5000/', {'signal': args.signal}))
