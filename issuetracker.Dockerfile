FROM python:3.10-alpine3.17

WORKDIR /usr/data/issue_tracker

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

EXPOSE 8000/tcp

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
