from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    # return HttpResponse("Hello, world. You're at the react_app index.")

    # ./templates 以下のファイルパスを記述
    # ! '/main/...'と冒頭に'/'をつけるとエラーとなるので注意
    return render(request, 'main/index.html', {})
