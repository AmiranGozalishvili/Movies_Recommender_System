from fastapi import FastAPI

from data import load_dataframe
from recommender import cosine_similarity_ranking
from sentence_transformers_recommender import MODEL_PREFIX as SENTENCE_TRANSFORMER_PREFIX
from sentence_transformers_recommender import encode_sentences as sentence_transformers_encode
from sentence_transformers_recommender import init_model as sentence_transformer_model_init

app = FastAPI()

model = sentence_transformer_model_init()

@app.get('/')
def get_root():
	return {'message': 'Welcome to movies recommender system API'}


@app.get('/predict')
def predict(query_sentence, topk:int=5):

	# 1. load model
	# 2. load dataframe
	# 3. encode sentence
	# 4. top k selection
	# 5. return dataframe

	df = load_dataframe(path="data/movies_metadata_sentence_transformers.json")
	# return df.head().to_csv()

	model = sentence_transformer_model_init()

	sentence_encoding = sentence_transformers_encode(model=model, sentences=[query_sentence])[0]

	topk_indices = cosine_similarity_ranking(query=sentence_encoding, items=df[f"overview_{SENTENCE_TRANSFORMER_PREFIX}_encoded"], top_k=topk)
	print(topk_indices)
	# return df.loc[topk_indices, :].to_csv()
	return df[["overview", 'original_title', 'genres']].iloc[topk_indices]     #df.columns, topk_indices,

# print(predict("dog", topk=5))
# # print(model)
