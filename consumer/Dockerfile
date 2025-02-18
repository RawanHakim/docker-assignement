FROM python:3.9-slim
WORKDIR /app
COPY app.py  .
RUN pip install requests
VOLUME ["/data"]
CMD ["python","app.py"]
