# Movies_Recommender_System
[problem definition](/docs/problem)

# Solution
The solution has been developed using FastAPI for defining API endpoints.

using command we will get API endpoint.
```
docker-compose up
```

In order to access API endpoint, navigate to http://0.0.0.0:8000/docs
![image](https://github.com/AmiranGozalishvili/Movies_Recommender_System/blob/main/resources/Fastapi%20welcome.png)

After launch API we have to fill in some parameters.
![image](https://github.com/AmiranGozalishvili/Movies_Recommender_System/blob/main/resources/Fastapi%20with%20query%20sentence.png)
  1. Query sentence, in example ‘a heroe movie in europe’.
  2. topk: number of recommended movies

If all parameters are filled correctly, we will get responce like this:
![image](https://github.com/AmiranGozalishvili/Movies_Recommender_System/blob/main/resources/Fastapi%20prediction%20responce.png)

# Steps of building recommender API
  1. Loading data.
  2. With help of Sentence Transformer encode sentences.
  3. Store data to json format data frame.
  4. Calculate cosine similarity indices between query sentence and stored data.
 
# References 
https://towardsdatascience.com/build-a-text-recommendation-system-with-python-e8b95d9f251c

https://towardsdatascience.com/introduction-to-recommender-systems-6c66cf15ada

# TODOs
add word2vec model
