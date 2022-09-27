import pandas as pd

from sentence_transformers_recommender import encode_sentences_from_dataframe as sentence_transformers_encode
from sentence_transformers_recommender import init_model as sentence_transformers_init


def load_dataframe(path="data/movies_metadata.csv"):
    if path.endswith(".csv"):
        return pd.read_csv(path)
    elif path.endswith(".json"):
        return pd.read_json(path)

def store_dataframe(dataframe, path):
    if path.endswith(".csv"):
        dataframe.to_csv(path)
    elif path.endswith(".json"):
        dataframe.to_json(path)

if __name__ == '__main__':
    df = load_dataframe(path="data/movies_metadata.csv")
    model = sentence_transformers_init()
    df_encoded = sentence_transformers_encode(model=model, dataframe=df)
    store_dataframe(dataframe=df, path="data/movies_metadata_sentence_transformers.json")
