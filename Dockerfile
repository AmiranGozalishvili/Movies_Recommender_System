
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./app /app
COPY ./requirements.txt /app

WORKDIR /app

RUN apt-get update && apt-get install build-essential -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


# RUN #pip install -U spacy
# RUN pip install -U sentence-transformers
# RUN pip install -U gensim
# RUN pip install IPython
# RUN pip install fastapi
# RUN pip install "uvicorn[standard]"
# RUN pip install -U scikit-learn
# RUN pip install joblib
# RUN pip install pandas
