import requests
import os
import json
API_BASE_URL = "http://api.moemoe.tokyo/anime/v1"

COURS = ["", "Springs", "Summer", "Autumn", "Winter"]


def _request(url: str):
    res = requests.get(url, headers={'content-type': 'application/json'})
    if res.ok:
        return res.json()


class Anime:
    """APIで取得できるアニメ情報クラス

    Params
    --------

    data : dict
        APIから受け取ったjson

    Examples
    --------

    Anime(JSON).title : str
        アニメタイトル

    Anime(JSON).public_url : str
        公式サイトURL

    取得可能な属性は以下参照
    https://github.com/Project-ShangriLa/sora-playframework-scala#base-object-1
    """

    def __init__(self, data: json):
        self.__raw = data

    def all(self):
        return list(self.__raw.keys())

    def __repr__(self):
        attrs = []
        [attrs.append(f"{k}: {self.__raw.get(str(k))}")
         for k in list(self.__raw.keys())]
        return "<class:Anime " + ", ".join(attrs) + ">"

    def __getattr__(self, name):
        return self.__raw.get(name)


class Cour:
    def __init__(self):
        pass

    def get(self, id: int):
        url = f"{API_BASE_URL}/master/cours"
        data = _request(url)
        print(data.get(str(id)))


class AnimeAPI:
    """APIリクエストクラス
    """

    def __init__(self):
        pass

    def get_year_overview(self, year: int) -> list:
        result = []
        url = f"{API_BASE_URL}/master/{year}"
        data = _request(url=url)
        [result.append(Anime(a)) for a in data]
        return result

    def get_anime_by_cour(self, year: int, cour: int) -> list:
        result = []
        url = f"{API_BASE_URL}/master/{year}/{cour}"
        data = _request(url=url)
        [result.append(Anime(a)) for a in data]
        return result
