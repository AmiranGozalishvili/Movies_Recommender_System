from sentence_transformers import SentenceTransformer


MODEL_PREFIX = "sentence_transformer"


def init_model():
    return SentenceTransformer('all-MiniLM-L6-v2')


def encode_sentences(model, sentences):
    embeddings = model.encode(sentences)

    return embeddings

def encode_sentences_from_dataframe(model, dataframe, column="overview"):
    """Encodes texts in given column and returns updated dataframe"""

    encoded = encode_sentences(model=model, sentences=dataframe[column])
    dataframe[f"{column}_{MODEL_PREFIX}_encoded"] = encoded.tolist()

    return dataframe