import json

# 아래 코드 수정 금지
movie_json = open("movie.json", encoding="UTF8")
movie = json.load(movie_json)

genres_json = open("genres.json", encoding="UTF8")
genres_list = json.load(genres_json)

# 이하 문제 해결을 위한 코드 작성
genres_names = []
for genres in genres_list:
    for k in movie["genre_ids"]:
        if k == genres["id"]:
            genres_names.append(genres["name"])

movie_info = {
    "id": movie["id"],
    "title": movie["title"],
    "vote_average": movie["vote_average"],
    "overview": movie["overview"],
    "genre_names": genres_names
}

print(movie_info)
