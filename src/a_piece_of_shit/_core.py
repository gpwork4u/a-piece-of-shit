"""核心邏輯：把一堆沒用的東西全部 import 進來。"""

from __future__ import annotations

import importlib
import logging
import sys
import time
from types import SimpleNamespace

logger = logging.getLogger(__name__)

# 格式: (import_name, alias)
# 包含 PyPI 下載量前 100 大 + 經典加碼套件
_PACKAGES = [
    # ========================================
    # PyPI Top 100 (30-day downloads)
    # ========================================
    ('boto3', 'boto3'),
    ('packaging', 'packaging'),
    ('urllib3', 'urllib3'),
    ('setuptools', 'setuptools'),
    ('certifi', 'certifi'),
    ('requests', 'requests'),
    ('typing_extensions', 'typing_extensions'),
    ('botocore', 'botocore'),
    ('idna', 'idna'),
    ('charset_normalizer', 'charset_normalizer'),
    ('aiobotocore', 'aiobotocore'),
    ('dateutil', 'dateutil'),
    ('six', 'six'),
    ('cryptography', 'cryptography'),
    ('grpc_status', 'grpc_status'),
    ('cffi', 'cffi'),
    ('numpy', 'np'),
    ('yaml', 'yaml'),
    ('s3transfer', 's3transfer'),
    ('pycparser', 'pycparser'),
    ('pluggy', 'pluggy'),
    ('pydantic', 'pydantic'),
    ('pygments', 'pygments'),
    ('s3fs', 's3fs'),
    ('fsspec', 'fsspec'),
    ('click', 'click'),
    ('google.protobuf', 'protobuf'),
    ('pandas', 'pd'),
    ('attrs', 'attrs'),
    ('pydantic_core', 'pydantic_core'),
    ('pytest', 'pytest'),
    ('anyio', 'anyio'),
    ('markupsafe', 'markupsafe'),
    ('h11', 'h11'),
    ('iniconfig', 'iniconfig'),
    ('platformdirs', 'platformdirs'),
    ('jmespath', 'jmespath'),
    ('annotated_types', 'annotated_types'),
    ('filelock', 'filelock'),
    ('jinja2', 'jinja2'),
    ('importlib_metadata', 'importlib_metadata'),
    ('pathspec', 'pathspec'),
    ('jwt', 'jwt'),
    ('rsa', 'rsa'),
    ('httpx', 'httpx'),
    ('zipp', 'zipp'),
    ('pytz', 'pytz'),
    ('httpcore', 'httpcore'),
    ('typing_inspection', 'typing_inspection'),
    ('pyasn1', 'pyasn1'),
    ('aiohttp', 'aiohttp'),
    ('dotenv', 'dotenv'),
    ('rich', 'rich'),
    ('multidict', 'multidict'),
    ('jsonschema', 'jsonschema'),
    ('google.auth', 'google_auth'),
    ('tzdata', 'tzdata'),
    ('yarl', 'yarl'),
    ('colorama', 'colorama'),
    ('tqdm', 'tqdm'),
    ('google.api_core', 'google_api_core'),
    ('grpc', 'grpc'),
    ('tomli', 'tomli'),
    ('frozenlist', 'frozenlist'),
    ('propcache', 'propcache'),
    ('oauthlib', 'oauthlib'),
    ('markdown_it', 'markdown_it'),
    ('referencing', 'referencing'),
    ('aiosignal', 'aiosignal'),
    ('wrapt', 'wrapt'),
    ('greenlet', 'greenlet'),
    ('PIL', 'pil'),
    ('pyasn1_modules', 'pyasn1_modules'),
    ('sqlalchemy', 'sa'),
    ('mdurl', 'mdurl'),
    ('scipy', 'scipy'),
    ('pyarrow', 'pa'),
    ('uvicorn', 'uvicorn'),
    ('starlette', 'starlette'),
    ('psutil', 'psutil'),
    ('pyparsing', 'pyparsing'),
    ('fastapi', 'fastapi'),
    ('google.genai', 'google_genai'),
    ('cachetools', 'cachetools'),
    ('tenacity', 'tenacity'),
    ('et_xmlfile', 'et_xmlfile'),
    ('openpyxl', 'openpyxl'),
    ('tomlkit', 'tomlkit'),
    # ========================================
    # 加碼：經典你不能沒有的
    # ========================================
    ('sklearn', 'sklearn'),
    ('tensorflow', 'tf'),
    ('torch', 'torch'),
    ('transformers', 'transformers'),
    ('matplotlib', 'mpl'),
    ('matplotlib.pyplot', 'plt'),
    ('seaborn', 'sns'),
    ('plotly', 'plotly'),
    ('flask', 'flask'),
    ('django', 'django'),
    ('celery', 'celery'),
    ('redis', 'redis_'),
    ('bs4', 'bs4'),
    ('scrapy', 'scrapy'),
    ('polars', 'pl'),
    ('sympy', 'sympy'),
    ('networkx', 'nx'),
    ('spacy', 'spacy'),
    ('nltk', 'nltk'),
    ('xgboost', 'xgb'),
    ('lightgbm', 'lgb'),
    ('streamlit', 'st'),
    ('gradio', 'gr'),
    ('dash', 'dash'),
    ('cv2', 'cv2'),
    ('bokeh', 'bokeh'),
    ('loguru', 'loguru'),
    ('orjson', 'orjson'),
    ('msgpack', 'msgpack'),
    ('faker', 'faker'),
    ('hypothesis', 'hypothesis'),
    ('ray', 'ray'),
    ('joblib', 'joblib'),
    ('numba', 'numba'),
    ('lxml', 'lxml'),
    ('pendulum', 'pendulum'),
    ('arrow', 'arrow_'),
    ('humanize', 'humanize'),
    ('emoji', 'emoji_'),
    ('regex', 'regex'),
    ('wandb', 'wandb'),
    ('mlflow', 'mlflow'),
    ('optuna', 'optuna'),
]


def import_everything(
    verbose: bool = True,
    yolo: bool = False,
) -> SimpleNamespace:
    """把所有 dependency 都 import 進來，回傳一個 namespace。

    Args:
        verbose: 是否印出每個 import 的狀態（預設開啟，讓你看看你浪費了多少時間）
        yolo: 如果為 True，會直接把所有東西塞進 caller 的 global namespace

    Returns:
        一個 SimpleNamespace，裡面塞滿了你根本用不到的 module。
    """
    ns = SimpleNamespace()
    success = 0
    failed = 0
    start = time.time()

    if verbose:
        print('🚽 開始載入一堆沒用的東西...\n')

    for pkg_name, alias in _PACKAGES:
        try:
            mod = importlib.import_module(pkg_name)
            setattr(ns, alias, mod)
            success += 1
            if verbose:
                print(f'  ✅ {pkg_name} -> {alias}')
        except ImportError:
            failed += 1
            if verbose:
                print(f'  💩 {pkg_name} -> 裝了但還是爛掉')
        except Exception as e:
            failed += 1
            if verbose:
                print(f'  🔥 {pkg_name} -> {e}')

    elapsed = time.time() - start

    if verbose:
        print(f'\n{"=" * 50}')
        print(f'🎉 成功 import 了 {success} 個沒用的 package')
        print(f'💀 有 {failed} 個爛掉了')
        print(f'⏱️  總共浪費了你 {elapsed:.2f} 秒的生命')
        print(f'💾 目前 sys.modules 裡有 {len(sys.modules)} 個 module')
        print(f'{"=" * 50}')
        print('\n用法: env.np, env.pd, env.plt, env.torch ...')
        print('恭喜你，你的記憶體已經被塞滿了。\n')

    if yolo:
        # 直接污染 caller 的 namespace，真正的 YOLO
        import inspect

        frame = inspect.stack()[1]
        caller_globals = frame[0].f_globals
        for attr in dir(ns):
            if not attr.startswith('_'):
                caller_globals[attr] = getattr(ns, attr)
        if verbose:
            print('🔥 YOLO 模式：已污染你的 global namespace，祝你好運。')

    return ns
