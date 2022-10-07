# CRUD
## DB연결(가상머신)
1. 방화벽 해제
```shell
systemctl stop firewalld
systemctl disable firewalld
setenforce 0
```
2. mysql 설치 및 초기 설정
```shell
yum install -y mysql-server

systemctl restart mysqld

mysql_secure_installation 

mysql -u root -p #mysql접속
```

```sql
CREATE DATABASE blog;
CREATE USER 'kjh'@'%' IDENTIFIED BY 'qwer1234';
GRANT ALL PRIVILEGES ON blog.* TO 'kjh'@'%';
FLUSH PRIVILEGES;
EXIT;
```
3. 확인
![image](./image/crud/1.png)<br/>
![image](./image/crud/2.png)<br/>

4. Django와 연결<br/>
` config/settings.py `
```python
# DATABASES 내용 지우고 추가
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'kjh',
        'PASSWORD': 'qwer1234',
        'HOST': '192.168.197.50',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
        }
    }
}
```

```shell
python manage.py migrate
```
![image](./image/crud/3.png)<br/>


5. Django와 DB연결 확인<br/>
![image](./image/crud/4.png)<br/>
내가 생성한 DB에 Django의 테이블이 생성된걸 확인 할 수 있다.<br/>

6. 테이블 생성해보기(연습)<br/>
` board/models.py `에 다음 명령어 추가<br/>
```python
class Fruits(models.Model):
    name = models.CharField(max_length=50)
    descript = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    cdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'id : {},name : {},description : {}'.format(self.id, self.name, self.descript)
```
![image](./image/crud/5.png)<br/>

` config/settings.py`에 앱 추가.<br/>
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'board',    # 여기 추가
]
```
![image](./image/crud/6.png)<br/>
- 테이블 적용<br/>
```shell
python manage.py makemigrations board # 앱 이름
python manage.py migrate
```
- 확인
![image](./image/crud/7.png)<br/>

## 게시판 만들기
1. DB에 게시판 테이블 생성<br/>
` board/models.py `에 다음 명령어 추가<br/>
```python
class Board(models.Model):
    title = models.CharField(max_length=200)
    contents = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.title
```
- 적용<br/>
```shell
python manage.py makemigrations board # 앱 이름
python manage.py migrate
```
![image](./image/crud/8.png)<br/>

2. 모델폼 생성
- 앱폴더(board)에 `forms.py`생성<br/>
![image](./image/crud/9.png)<br/>

- 폼 작성<br/>
```python
from django import forms
from .models import Board

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('title', 'contents')
```



