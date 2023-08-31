#!/usr/bin/env python3

""" 複数のロガーに同じハンドラを登録する例 """

import logging

# 任意のロガーを生成する
logger_a = logging.getLogger('Logger_A')
logger_b = logging.getLogger('Logger_B')

# ロガーのログレベルを設定する
logger_a.setLevel(logging.DEBUG)
logger_b.setLevel(logging.WARNING)

# ハンドラを生成する
stream_handler = logging.StreamHandler()

# ハンドラのログレベルを設定する
stream_handler.setLevel(logging.DEBUG)

# ログフォーマットを生成する
fmt = logging.Formatter('%(asctime)s %(name)s [%(levelname)s] %(message)s')

# ハンドラにログフォーマットを登録する
stream_handler.setFormatter(fmt)

# ロガーにハンドラを登録する
logger_a.addHandler(stream_handler)
logger_b.addHandler(stream_handler)

# ロガーAでログを出力する
logger_a.debug('This is a debug message.')
logger_a.info('This is a info message.')
logger_a.warning('This is a warning message.')
logger_a.error('This is a error message.')
logger_a.critical('This is a critical message.')

# ロガーBでログを出力する
logger_b.debug('This is a debug message.')      # ログレベルに基づき出力されない
logger_b.info('This is a info message.')        # ログレベルに基づき出力されない
logger_b.warning('This is a warning message.')
logger_b.error('This is a error message.')
logger_b.critical('This is a critical message.')
