FROM python:3.10-alpine3.17

WORKDIR /issue_tracker

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

# COPY issue_tracker/.env ./issue_tracker/.env
EXPOSE 8000/tcp

# RUN python manage.py makemigrations

# RUN python manage.py migrate

# RUN python manage.py collectstatic --noinput

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "issue_tracker.wsgi:application", "--bind", "0.0.0.0:8000"]
