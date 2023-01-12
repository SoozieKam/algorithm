import json
from pprint import pprint

# 아래 코드 수정 금지
movies_json = open("movies.json", encoding="UTF8")
movies_list = json.load(movies_json)

# 이하 문제 해결을 위한 코드 작성

movie_list = {}
required = ["id", "title", "poster_path",
            "vote_average", "overview", "genre_ids"]
collect = []

collect.append(movie_list)
print(collect, id(collect[0]))

for info in required:
    movie_list[info] = movies_list[0][info]

print(collect, id(collect[0]))

for info in required:
    movie_list[info] = movies_list[1][info]

pprint(collect, id(collect[0]))
