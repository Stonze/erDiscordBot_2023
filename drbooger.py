import discord
from discord.ext import commands
from api import userStats
import emoji
import key
from get_tier import getTier

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix= ".", intents= intents)

#Discord 이모지 사용
e = emoji.emojize(":small_blue_diamond:")
e_str = str(e)
TOKEN = key.TOKEN

#봇 명령어 지정
@bot.command(name='검색')

async def search(ctx, *args):
    nickname = ' '.join(args)
    user_stats_result = userStats(nickname)
    user_name = user_stats_result[0]
    total_games = user_stats_result[1]
    mmr = user_stats_result[2]
    win_rate = user_stats_result[3]
    korean_name1 = user_stats_result[4]
    m1totalGames = user_stats_result[5]
    m1WinRate = user_stats_result[6]
    korean_name2 = user_stats_result[7]
    m2totalGames = user_stats_result[8]
    m2WinRate = user_stats_result[9]
    korean_name3 = user_stats_result[10]
    m3totalGames = user_stats_result[11]
    m3WinRate = user_stats_result[12]
    code = user_stats_result[13]
    
    embedSucess = discord.Embed(title=user_name, 
                          description=f'{e_str}게임 수: {total_games}게임\n{e_str}RP: {mmr}RP ({getTier(mmr)})\n{e_str}승률: {win_rate}%',
                          color=discord.Color.green())
    embedSucess.set_author(name="이터널 리턴 유저 검색 결과")
    embedSucess.add_field(name=korean_name1, 
                    value=f'{e_str}게임 수: {m1totalGames}게임\n{e_str}승률: {m1WinRate}%', 
                    inline=False)
    embedSucess.add_field(name=korean_name2, 
                    value=f'{e_str}게임 수: {m2totalGames}게임\n{e_str}승률: {m2WinRate}%', 
                    inline=False)
    embedSucess.add_field(name=korean_name3, 
                    value=f'{e_str}게임 수: {m3totalGames}게임\n{e_str}승률: {m3WinRate}%\n[dak.gg 링크](<https://dak.gg/er/players/{nickname}/>)', 
                    inline=False)
    embedSucess.set_thumbnail(url="https://upload3.inven.co.kr/upload/2022/08/05/bbs/i14286896481.jpg")
    
    embedError = discord.Embed(title="해당 유저를 검색할 수 없습니다.", 
                               description="닉네임을 다시 한 번 확인하거나 잠시 후에 검색해주세요.",
                               color=discord.Color.red())
    embedError.set_thumbnail(url="https://upload3.inven.co.kr/upload/2022/08/05/bbs/i14266620862.jpg")
    
    await ctx.send(embed = embedSucess)


bot.run(TOKEN)            
