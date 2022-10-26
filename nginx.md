# nginx
## 설치
### nginx 설치
```shell
# 방화벽 해제
systemctl stop firewalld
systemctl disable firewalld
setenforce 0

# nginx 설치
yum install -y nginx
# nginx 실행
systemctl restart nginx
```
### python, flask 설치
```shell
yum install -y python3-pip python3-devel gcc
alias python=python3
alias pip=pip3

pip install virtualenv
pip install flask flask_cors
```

### flask 실행
```shell
mkdir web
cd web
vi main.py
```
`main.py`
```python
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/hello")
def hello():
    result = {"code" : 200, "message":"hello flask"}
    return result

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1111)
```

```shell
python main.py
```


### gunicorn 설치및 실행
```shell
pip install gunicorn


