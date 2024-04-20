# test-app

## local run

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

## run in container

```bash
docker build . -t test-app

docker run -p 8080:8080 test-app
```