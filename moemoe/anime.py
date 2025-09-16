import requests, json

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

    def __init__(self, data: dict):
        self.__raw          = data

    def all(self):
        return list(self.__raw.keys())

    def __repr__(self):
        attrs               = [f"{k}: {self.__raw.get(str(k))}" for k in list(self.__raw.keys())]
        return "<class:Anime " + ", ".join(attrs) + ">"
    
    def __str__(self):
        return self.__raw["title"]


    def __getattr__(self, name):
        return self.__raw.get(name, None)


class AnimeAPI:
    """APIリクエストクラス
    """

    def __init__(
        self, 
        url = "https://anime-api.deno.dev/anime/v1"
    ):
        self.API_BASE_URL   = url
        self.COURS          = ["", "Spring", "Summer", "Autumn", "Winter"]
    
    def _request(self, url: str):
        try : 
            return json.loads(requests.get(url).text)
        except:
            return []


    def cours_get(self, id: int):
        url                 = f"{self.API_BASE_URL}/master/cours"
        data                = self._request(url)
        return data.get(str(id), [])

    def get_year_overview(self, year: int) -> list:
        url                 = f"{self.API_BASE_URL}/master/{year}"
        data                = self._request(url=url)
        result              = [Anime(a) for a in data]
        return result

    def get_anime_by_cour(self, year: int, season: str) -> list:
        try:
            cour            = self.COURS.index(season)
        except:
            cour            = 0
        url                 = f"{self.API_BASE_URL}/master/{year}/{cour}"
        data                = self._request(url=url)
        result              = [Anime(a) for a in data]
        return result


if __name__ == "__main__":
    api = AnimeAPI()
    print(api.get_anime_by_cour(2023, "Spring"))