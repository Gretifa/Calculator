FROM python:3.8
WORKDIR /usr/src/app
COPY Calculator/ .
CMD ["python", "./calculator.py"]