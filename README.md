# Djangoトライアル―Reactとの連携

## 参考

- [DjangoとReactの構築及びAPI連携について～構築編～](https://qiita.com/shiranon/items/8182445975dff4cf19a6)
- [Djangoとwebpackを連携して､ モダンなフロントエンド環境を構築する](https://zenn.dev/kimuson/articles/b2a96d7c8729659379d3)

# 概要

- webpackをつかって、DjangoからReactで構築した画面を利用する検証
- ReactからDjango DBの参照も行えるようDjango REST frameworkを使用してDBのAPI化も行っている

# 検証環境

- Windows10 pro
- Python v3.9.5
- Django v3.1.5
- Node.js v14.15.4
- React.js v17.0.2

(django-webpack-loader v0.7.0)

# 必要パッケージの導入

## バックエンド側：Pythonモジュール

``` 
$ cd ./backend
$ py -m pip install -r requirements.txt
```

## フロントエンド側：npmパッケージ

```
$ cd ./frontend/django-front
$ npm ci
```

# 描画の動き

```python backend/react_app/views.py
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/index.html', {})
```
上記index関数で/templates以下のhtmlテンプレートを指定し、描画する

```html backend/react_app/templates/main/index.html
<!DOCTYPE html>

{% load static %}

<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>React</title>
</head>
<body>
    <div id="app"></div>
    <script type="text/javascript" src="{% static 'js/bundle.js' %}"></script>
</body>
</html>
```
上のHTMLファイル、scriptタグで 'js/bundle.js'のstaticが記述されているが、これがReactからwebpackでbundleしたJavaScriptファイル。

当該ファイルは backend/static/js/bundle.js があたる。
