FROM python:3.13-slim
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["uvicorn", "crud:app", "--host", "0.0.0.0", "--port", "8002"]
