#coding=utf-8
from discord.ext import commands
import discord, requests, traceback

class GeneralCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mcs(self, ctx, server_ip = None):
        api_link = f"https://api.mcsrvstat.us/2/{server_ip}"
        try:
            res = requests.get(api_link).json()
            e = discord.Embed(title = f"{server_ip} の情報", description = f">>> サーバーIP: **`{server_ip}`**\nポート: **`{res['port']}`**\nMOTD: ```\n{res['motd']['raw']}\n```\nバージョン: **`{res['version']}`**\nサーバー人数: **`{res['players']['online']} / {res['players']['max']}`**\nホストサーバーIP: **`{res['hostname']}`**", color = discord.Color.random())
        except:
            e = discord.Embed(title = "エラー", description = f">>> サーバー情報を取得できませんでした！", color = 0xff0000)
        await ctx.send(embed = e)

    @mcs.error
    async def mcs_error(self, ctx, error):
        e = discord.Embed(title = "例外エラーが発生しました", description = f">>> ```\n{traceback.format_exc()}\n```", color = 0xff0000)
        await ctx.send(embed = e)
        return

def setup(bot):
    bot.add_cog(GeneralCog(bot))