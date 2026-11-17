FROM python:3.14.7-slim

ENV PYTHONNUNBUFFERED=TRUE

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir --verbose pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy --ignore-pipfile

COPY stockout_predict.py ./
COPY model/ ./model/

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "stockout_predict:app"]