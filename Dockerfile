FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

RUN pip install git+https://github.com/suno-ai/bark.git

COPY ./app /app