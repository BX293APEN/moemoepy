from moemoe import AnimeAPI

if __name__ == "__main__":
    api = AnimeAPI()
    print(api.get_anime_by_cour(2023, "Spring"))