import requests
from key import API_KEY

# 이터널리턴 API URL
api_url = "https://open-api.bser.io"

# API 헤더 (API 키 등 필요한 헤더 정보 추가)
headers = API_KEY

def tierCut():
    ranking = requests.get(f"{api_url}/v1/rank/top/19/3", headers=headers)
    data = ranking.json()
    eternityCut = 200
    for user in data["topRanks"]:
        if user["rank"] == eternityCut:
            eternity = user["mmr"]
            break
    demigodCut = 700
    for user in data["topRanks"]:
        if user["rank"] == demigodCut:
            demigod = user["mmr"]
            break
    return eternity, demigod        