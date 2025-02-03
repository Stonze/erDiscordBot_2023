import requests
from codemapping import code_name_mapping
from key import API_KEY
# 이터널리턴 API URL
api_url = "https://open-api.bser.io"

# API 헤더
headers = API_KEY

#이터널 리턴 유저 검색
def userStats(nickname):
    search_query = nickname
    response = requests.get(f"{api_url}/v1/user/nickname?query={search_query}", headers=headers)
    data = response.json()
    user_num = data["user"]["userNum"]
    code = data["code"]
    stats = requests.get(f"{api_url}/v1/user/stats/{user_num}/19", headers=headers)
    stats_data = stats.json()
    user_name = stats_data["userStats"][0]["nickname"]
    total_games = stats_data["userStats"][0]["totalGames"]
    mmr = stats_data["userStats"][0]["mmr"]
    total_wins = stats_data["userStats"][0]["totalWins"]
    win_rate = round(total_wins/total_games * 100, 1)
    m1chCode = stats_data["userStats"][0]["characterStats"][0]["characterCode"]
    m1totalGames = stats_data["userStats"][0]["characterStats"][0]["totalGames"]
    m1Wins = stats_data["userStats"][0]["characterStats"][0]["wins"]
    m1WinRate = round(m1Wins/m1totalGames * 100, 1)
    m2chCode = stats_data["userStats"][0]["characterStats"][1]["characterCode"]
    m2totalGames = stats_data["userStats"][0]["characterStats"][1]["totalGames"]
    m2Wins = stats_data["userStats"][0]["characterStats"][1]["wins"]
    m2WinRate = round(m2Wins/m2totalGames * 100, 1)
    m3chCode = stats_data["userStats"][0]["characterStats"][2]["characterCode"]
    m3totalGames = stats_data["userStats"][0]["characterStats"][2]["totalGames"]
    m3Wins = stats_data["userStats"][0]["characterStats"][2]["wins"]
    m3WinRate = round(m3Wins/m3totalGames * 100, 1)
    korean_name1 = code_name_mapping.get(m1chCode, "알 수 없음")
    korean_name2 = code_name_mapping.get(m2chCode, "알 수 없음")
    korean_name3 = code_name_mapping.get(m3chCode, "알 수 없음")
    return (user_name, total_games, mmr, win_rate, 
            korean_name1, m1totalGames, m1WinRate,
            korean_name2, m2totalGames, m2WinRate,
            korean_name3, m3totalGames, m3WinRate, code)
