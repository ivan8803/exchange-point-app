FROM python:3.10.5-slim

RUN mkdir app
WORKDIR /app

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install fastapi
RUN pip install uvicorn
RUN pip install pydantic
RUN pip install requests

COPY src/ .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]