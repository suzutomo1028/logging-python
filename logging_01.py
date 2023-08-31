#!/usr/bin/env python3

""" ルートロガーを用いる例 (非推奨) """

import logging

# ルートログの基本設定を行う
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s')

# ログを出力する
logging.debug('This is a debug message.')
logging.info('This is a info message.')
logging.warning('This is a warning message.')
logging.error('This is a error message.')
logging.critical('This is a critical message.')
