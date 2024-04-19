# test-app

## local run

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

## docker

```bash
docker build . -t test-app
docker run -d -p 8080:5000 test-app
```
