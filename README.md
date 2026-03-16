# 💩 a-piece-of-shit

> 一個沒什麼屁用的 Python package。

## 這是什麼？

這是一個會拉 **100+ 個 dependency** 的 Python package，唯一的功能是幫你一次 import 所有東西。

安裝完大概會吃掉你 **5GB** 的硬碟空間和 **3GB** 的記憶體。

## 安裝

```bash
pip install a-piece-of-shit
```

然後去泡杯咖啡，回來應該還沒裝完。

## 使用方式

```python
from a_piece_of_shit import import_everything

# 基本用法 - 回傳一個 namespace
env = import_everything()

# 現在你可以這樣用
env.np.array([1, 2, 3])
env.pd.DataFrame({'a': [1, 2, 3]})
env.plt.plot([1, 2, 3])
env.requests.get('https://example.com')
env.torch.tensor([1, 2, 3])

# YOLO 模式 - 直接污染你的 global namespace
import_everything(yolo=True)

# 現在直接用，不用加 env.
np.array([1, 2, 3])  # 直接就能用了
pd.DataFrame({'a': [1, 2, 3]})
```

## 到底 import 了什麼？

numpy, pandas, polars, scipy, sympy, sklearn, tensorflow, torch, transformers,
xgboost, lightgbm, catboost, matplotlib, seaborn, plotly, bokeh, flask, django,
fastapi, streamlit, gradio, requests, httpx, beautifulsoup4, scrapy, sqlalchemy,
redis, celery, kafka, boto3, rich, typer, click, pydantic, cryptography, opencv,
spacy, nltk, gensim, networkx, ray ... 還有一堆。

完整清單請看 `pyproject.toml`，反正你也不會看。

## 為什麼要做這個？

因為可以。

## License

WTFPL - Do What The Fuck You Want To Public License
