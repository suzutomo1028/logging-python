#!/usr/bin/env python3

""" 外部ファイルでロギング環境を設定する例 """

import json
from logging import config, getLogger

# 設定ファイルを読込む
with open('logging_conf.json', 'r') as f:
    logging_conf = json.load(f)

# ロギング環境を設定する
config.dictConfig(logging_conf)

# 任意のロガーを生成する
logger_a = getLogger('Logger_A')
logger_b = getLogger('Logger_B')

# ロガーAでログを出力する
logger_a.debug('This is a debug message.')
logger_a.info('This is a info message.')
logger_a.warning('This is a warning message.')
logger_a.error('This is a error message.')
logger_a.critical('This is a critical message.')

# ロガーBでログを出力する
logger_b.debug('This is a debug message.')      # ログレベルに基づき出力されない
logger_b.info('This is a info message.')        # ログレベルに基づき出力されない
logger_b.warning('This is a warning message.')  # ログレベルに基づき出力されない
logger_b.error('This is a error message.')
logger_b.critical('This is a critical message.')
