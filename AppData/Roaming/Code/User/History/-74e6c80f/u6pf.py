import json
from pprint import pprint

# 아래 코드 수정 금지
movie_json = open("movie.json", encoding="UTF8")
movie = json.load(movie_json)

genres_json = open("genres.json", encoding="UTF8")
genres_list = json.load(genres_json)

# 이하 문제 해결을 위한 코드 작성

genres_num = []
for genres in genres_list:
    for k in movie["genre_ids"]:
        if k == genres["id"]:
            genres_num.append(genres["name"])

pprint(genres_num)
