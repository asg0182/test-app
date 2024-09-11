FROM python:3.12.3
MAINTAINER Alex Gladkov <asg0182@gmail.com>

RUN useradd app -d /app
RUN mkdir -pv app && chown -R app:app /app
USER app
COPY . /app
WORKDIR /app
RUN pip install --user app -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]
