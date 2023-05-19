FROM python:3.9
COPY . /app
RUN pip install fastapi uvicorn httpx 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]