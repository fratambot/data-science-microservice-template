FROM python:3.9 as base
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY ./app /app/.
CMD ["uvicorn", "main:app", "--reload", "--proxy-headers", "--host", "0.0.0.0", "--port", "8883"]
