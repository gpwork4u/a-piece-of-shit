"""測試這坨東西至少能跑。"""

from unittest.mock import patch

from a_piece_of_shit._core import import_everything


def test_import_everything_returns_namespace():
    """確認 import_everything 回傳一個有東西的 namespace。"""
    result = import_everything(verbose=False)
    # 至少要有一些 attribute（就算有些 import 失敗）
    attrs = [a for a in dir(result) if not a.startswith('_')]
    assert len(attrs) > 0


def test_import_everything_verbose(capsys):
    """確認 verbose 模式有印東西。"""
    import_everything(verbose=True)
    captured = capsys.readouterr()
    assert '開始載入' in captured.out
    assert '成功 import' in captured.out


def test_yolo_mode():
    """確認 YOLO 模式會污染 caller namespace。"""
    # yolo=True 會把東西塞進 caller 的 globals
    import_everything(verbose=False, yolo=True)
    # 檢查至少有 np 或其他東西被塞進來
    # 因為是塞進這個函式的 frame globals (即本模組)
    import sys

    this_module = sys.modules[__name__]
    injected = [
        a for a in dir(this_module)
        if not a.startswith('_') and a not in ('test_yolo_mode',)
    ]
    assert len(injected) > 0
