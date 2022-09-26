
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
RUN apt-get update && apt-get install build-essential -y

RUN pip install --upgrade pip
RUN #pip install -U spacy
RUN pip install -U sentence-transformers
RUN #pip install -U gensim
RUN pip install IPython
RUN pip install fastapi
RUN pip install "uvicorn[standard]"
RUN pip install sklearn joblib
RUN pip install pandas

COPY ./app /app

WORKDIR /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.2", "--port", "8002"]
