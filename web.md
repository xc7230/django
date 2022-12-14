# web
## Html Django에 연결하기

- templates 생성<br/>
![image](./image/web/1.png)<br/>
프로젝트 파일 밑에 templates 디렉토리를 생성하고 html파일 하나를 만든다.<br/>
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>안녕하세요</h1>
</body>
</html>
```

- templates 적용
![image](./image/web/2.png)<br/>
`config` 디렉토리 밑에 있는 `settings.py`의 설정을 다음과 같이 바꿔준다.<br/>
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'], # 여기 추가
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

- 앱 수정<br/>
만들어 놓은 앱 폴더에 `view.py`를 다음과 같이 작성한다.<br/>
![image](./image/web/3.png)<br/>
```python
def asdf(request):
    print("test 입니다.")
    return render(request, 'test.html')
```

- 앱 연결하기<br/>
![image](./image/web/4.png)<br/>
`config`디렉토리 안에 있는 `urls.py`에 들어가 설정을 바꿔준다.<br/>
```python
from django.contrib import admin
from django.urls import path
import test1.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('qwert/', test1.views.asdf), # 여기 추가
]
```

- 실행
```shell
python manage.py runserver
```
![image](./image/web/5.png)<br/>

## 클라이언트 서버 데이터 주고 받기

### 클라이언트가 서버에서<br/>
- html에서 보낸 정보를 받을 변수를 설정해준다.<br/>
`test1/view.py`
```python
def input_page(request):
    return render(request, 'input.html')
```
- 저장된 변수를 출력하기 위해 서버에 연동해준다.<br/>
`config/urls.py`
```python
path('input_page/', test1.views.input_page), # urlpatterns에 추가
```


- 데이터를 보낼 html 하나를 만든다.<br/>
`templates/input.html`
```html
<body>
      GET 방식으로 요청
      <a href="/get_data?num1=10&num2=20">보내기</a> <br>

      POST 방식으로 요청
      <form action="/get_data/" method="post">
          {% csrf_token %}
          <input type="text" name="num1"> <br>
          <input type="text" name="num2">
          <button>보내기</button>
      </form>
</body>
```

- 확인<br/>
![image](./image/web/6.png)<br/>

### 데이터를 받은 서버가 다시 클라이언트에 출력<br/>
- 서버 보낸 정보를 클라이언트에서 받을 변수를 설정해준다.<br/>
`test1/view.py`
```python
def get_data_func(request):
    if request.method == 'GET':
        num1 = request.GET.get('num1', None)
        num2 = request.GET.get('num2', None)
    else :
        num1 = request.POST.get('num1', None)
        num2 = request.POST.get('num1', None)

    sum = int(num1) + int(num2)
    context ={"sum" : sum}

    return render(request, 'result.html', context)
```

- 저장된 변수를 출력하기 위해 서버에 연동해준다.<br/>
`config/urls.py`
```python
path('get_data/', test1.views.get_data_func),   # urlpatterns에 추가
```

- 데이터를 받아 출력할 html 하나를 만든다.<br/>
`templates/result.html`
```html
<body>
		잘 받았음
		{{ sum }}
</body>
```

- 확인
    - Get방식
    ![image](./image/web/7.png)<br/>
    ![image](./image/web/8.png)<br/>

    - Post방식
    ![image](./image/web/9.png)<br/>
    ![image](./image/web/10.png)<br/>


### 포스트 방식으로 서버에게 title과 contents를 전달.

- 입력 페이지
`templates/input.html`
```html
<!-- 추가 -->
데이터 입력
      <form action="/get_data2/" method="post">
          {% csrf_token %}
          title<br>
          <input type="text" name="title"> <br>
          contents<br>
          <input type="text" name="contents">
          <button>보내기</button>
      </form>
```      
- 변수 설정
`test1/view.py`
```python
def get_data_func2(request):
    title = request.POST.get('title', None)
    contents = request.POST.get('contents', None)

    context2 = {"title" : title, "contents" : contents}

    print(title)
    print(contents)
    print(context2)

    return render(request, 'result2.html', context2)
```

- 서버 연동
`config/urls.py`
```python
path('get_data2/', test1.views.get_data_func2), # urlpatterns에 추가
```

- 출력 페이지
`templates/result2.html`
```html
<body>

		잘 받았음 <br/>
		{{ title }}<br/>
        {{ contents }}

</body>
```

- 확인<br/>
    - 데이터 입력<br/>
    ![image](./image/web/11.png)<br/>

    - 출력<br/>
    ![image](./image/web/12.png)<br/>
