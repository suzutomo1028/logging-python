#!/usr/bin/env python3

""" ルートから生成したロガーを用いる例 (通常の手順) """

import logging

# 任意のロガーを生成する
logger = logging.getLogger(__name__)

# ロガーのログレベルを設定する
logger.setLevel(logging.DEBUG)

# ハンドラを生成する
handler = logging.StreamHandler()

# ハンドラのログレベルを設定する
handler.setLevel(logging.WARNING)

# ログフォーマットを生成する
fmt = logging.Formatter('%(asctime)s %(name)s [%(levelname)s] %(message)s')

# ハンドラにログフォーマットを登録する
handler.setFormatter(fmt)

# ロガーにハンドラを登録する
logger.addHandler(handler)

# ログを出力する
logger.debug('This is a debug message.')    # ログレベルに基づき出力されない
logger.info('This is a info message.')      # ログレベルに基づき出力されない
logger.warning('This is a warning message.')
logger.error('This is a error message.')
logger.critical('This is a critical message.')
