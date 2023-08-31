#!/usr/bin/env python3

""" ひとつのロガーに複数のハンドラを登録する例 """

import logging

# 任意のロガーを生成する
logger = logging.getLogger(__name__)

# ロガーのログレベルを設定する
logger.setLevel(logging.DEBUG)

# ハンドラを生成する
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler(filename='logging_03.log', mode='w', encoding='utf-8')

# ハンドラのログレベルを設定する
stream_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.ERROR)

# ログフォーマットを生成する
fmt = logging.Formatter('%(asctime)s %(name)s [%(levelname)s] %(message)s')

# ハンドラにログフォーマットを登録する
stream_handler.setFormatter(fmt)
file_handler.setFormatter(fmt)

# ロガーにハンドラを登録する
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

# ログを出力する
logger.debug('This is a debug message.')        # ファイルへは出力されない
logger.info('This is a info message.')          # ファイルへは出力されない
logger.warning('This is a warning message.')    # ファイルへは出力されない
logger.error('This is a error message.')
logger.critical('This is a critical message.')
