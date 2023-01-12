import json
from pprint import pprint

# 아래 코드 수정 금지
movie_json = open("movie.json", encoding="UTF8")
movie = json.load(movie_json)

genres_json = open("genres.json", encoding="UTF8")
genres_list = json.load(genres_json)

# 이하 문제 해결을 위한 코드 작성

genres_num = []
for i in genres_list:
    if movie["genre_ids"][0] == genres_list["id"]:
        genres_num.append(genres_list["id"])
    if movie["genre_ids"][1] == genres_list["id"]:
        genres_num.append(genres_list["id"])

pprint(genres_num)
