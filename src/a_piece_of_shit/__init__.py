"""
A Piece of Shit - 一個沒什麼屁用的 Python package。

唯一的功能：幫你 import 一堆你根本不需要的東西。

Usage:
    from a_piece_of_shit import import_everything
    env = import_everything()

    # 現在你可以用 env.np, env.pd, env.requests ... 等等
    # 恭喜你，你剛剛浪費了 3GB 的記憶體。
"""

from a_piece_of_shit._core import import_everything

__all__ = ['import_everything']
__version__ = '0.1.0'
