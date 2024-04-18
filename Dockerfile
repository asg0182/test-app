FROM python:3.12.3
MAINTAINER Alex Gladkov <asg0182@gmail.com>

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]
