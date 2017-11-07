import aiohttp
from discord.ext import commands
import discord

class Subss:
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))
        # self.message = '**{}** Subscribers|Subscribe  -> :link: __**https://www.youtube.com/channel/UCnFHsZfaCwgBzbmt89Nmj3A**__ '

    def subs_emb(self, subs):
        emb = discord.Embed(title="**{}** Subscribers|Subscribe 👇".format(subs),
                            description="🔗 **[ClickHere](https://www.youtube.com/channel/UCnFHsZfaCwgBzbmt89Nmj3A)**<:kk:332133470572642317><:mg:332139374244265984> ",
                            color=0x4634e7)
        emb.set_author(name="MaGeClan", url="https://www.youtube.com/channel/UCnFHsZfaCwgBzbmt89Nmj3A", icon_url="https://yt3.ggpht.com/-palNhXtV33c/AAAAAAAAAAI/AAAAAAAAAAA/DgJik9EDvqA/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")
        emb.set_thumbnail(url='https://yt3.ggpht.com/-palNhXtV33c/AAAAAAAAAAI/AAAAAAAAAAA/DgJik9EDvqA/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
        emb.set_footer(text="MaGeClan", icon_url="https://cdn.discordapp.com/emojis/329991214327660544.png")
        return emb

    @commands.command(pass_context=True)
    async def subsmage(self, ctx):
        parameters = {"id": "UCnFHsZfaCwgBzbmt89Nmj3A", "key": "AIzaSyCssyjjfIcJpvl4CYoD20LbKcWIxQPNvw8", "part": "statistics",
                      "fields": "items/statistics/subscriberCount"}
        async with aiohttp.ClientSession() as session:
            async with session.get("https://www.googleapis.com/youtube/v3/channels", params=parameters) as r:
                if r.status == 200:
                    json_data = await r.json()
                    sub_count = json_data['items'][0]['statistics']['subscriberCount']
                    await self.bot.send_message(ctx.message.channel, embed=self.subs_emb(sub_count))
                else:
                    await self.bot.say('Error: Status {}, contact the creator'.format(r.status))
					
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))
        # self.message = '**{}** Subscribers|Subscribe  -> :link: __**https://www.youtube.com/channel/UCiJMqxVi_vSVbIcuGwVQybg**__ '

    def subs_emb(self, subs):
        emb = discord.Embed(title="**{}** Subscribers|Subscribe 👇".format(subs),
                            description="🔗 **[ClickHere](https://www.youtube.com/channel/UCiJMqxVi_vSVbIcuGwVQybg)**<:kk:332133470572642317><:reaper:332139179276238859>",                            color=0x2626f0)
        emb.set_author(name="The Reaper", url="https://www.youtube.com/channel/UCiJMqxVi_vSVbIcuGwVQybg", icon_url="https://yt3.ggpht.com/-MpWlOugIa0U/AAAAAAAAAAI/AAAAAAAAAAA/FsRxyfe8Fxo/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")
        emb.set_thumbnail(url='https://yt3.ggpht.com/-MpWlOugIa0U/AAAAAAAAAAI/AAAAAAAAAAA/FsRxyfe8Fxo/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
        emb.set_footer(text="The Reaper", icon_url="https://cdn.discordapp.com/emojis/329991214327660544.png")
        return emb

    @commands.command(pass_context=True)
    async def subsreaper(self, ctx):
        parameters = {"id": "UCiJMqxVi_vSVbIcuGwVQybg", "key": "AIzaSyCssyjjfIcJpvl4CYoD20LbKcWIxQPNvw8", "part": "statistics",
                      "fields": "items/statistics/subscriberCount"}
        async with aiohttp.ClientSession() as session:
            async with session.get("https://www.googleapis.com/youtube/v3/channels", params=parameters) as r:
                if r.status == 200:
                    json_data = await r.json()
                    sub_count = json_data['items'][0]['statistics']['subscriberCount']
                    await self.bot.send_message(ctx.message.channel, embed=self.subs_emb(sub_count))
                else:
                    await self.bot.say('Error: Status {}, contact the creator'.format(r.status))

    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))
        # self.message = '**{}** Subscribers|Subscribe  -> :link: __**https://www.youtube.com/channel/UCyGpuvdM27Lfi4lzSgdY9eA**__ '

    def subs_emb(self, subs):
        emb = discord.Embed(title="**{}** Subscribers|Subscribe 👇".format(subs),
                            description="🔗 **[ClickHere](https://www.youtube.com/channel/UCyGpuvdM27Lfi4lzSgdY9eA)**<:kk:332133470572642317><:ray:332139291348172811>",
                            color=0x930003)
        emb.set_author(name="Ray", url="https://www.youtube.com/channel/UCyGpuvdM27Lfi4lzSgdY9eA", icon_url="https://yt3.ggpht.com/-UqJIQBQ6o5Q/AAAAAAAAAAI/AAAAAAAAAAA/cnNVA1EX5L4/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")

        emb.set_thumbnail(url='https://yt3.ggpht.com/-UqJIQBQ6o5Q/AAAAAAAAAAI/AAAAAAAAAAA/cnNVA1EX5L4/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
        emb.set_footer(text="Ray", icon_url="https://cdn.discordapp.com/emojis/329991214327660544.png")
        return emb

    @commands.command(pass_context=True)
    async def subsray(self, ctx):
        parameters = {"id": "UCyGpuvdM27Lfi4lzSgdY9eA", "key": "AIzaSyCssyjjfIcJpvl4CYoD20LbKcWIxQPNvw8", "part": "statistics",
                      "fields": "items/statistics/subscriberCount"}
        async with aiohttp.ClientSession() as session:
            async with session.get("https://www.googleapis.com/youtube/v3/channels", params=parameters) as r:
                if r.status == 200:
                    json_data = await r.json()
                    sub_count = json_data['items'][0]['statistics']['subscriberCount']
                    await self.bot.send_message(ctx.message.channel, embed=self.subs_emb(sub_count))
                else:
                    await self.bot.say('Error: Status {}, contact the creator'.format(r.status))

    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))
        # self.message = '**{}** Subscribers|Subscribe  -> :link: __**https://www.youtube.com/channel/UCnFHsZfaCwgBzbmt89Nmj3A**__ '

    def subs_emb(self, subs):
        emb = discord.Embed(title="**{}** Subscribers|Subscribe 👇".format(subs),
                            description="🔗 **[ClickHere](https://www.youtube.com/c/ManGoYTB)**<:kk:332133470572642317><:mango:336914223462612992><:croown:336916788703133707> ",
                            color=0x4634e7)
        emb.set_author(name="ManGoYT", url="https://www.youtube.com/c/ManGoYTB", icon_url="https://yt3.ggpht.com/-CRZ_NLhRUEs/AAAAAAAAAAI/AAAAAAAAAAA/sDANm7rogzE/s48-c-k-no-mo-rj-c0xffffff/photo.jpg")
        emb.set_thumbnail(url='https://yt3.ggpht.com/-CRZ_NLhRUEs/AAAAAAAAAAI/AAAAAAAAAAA/sDANm7rogzE/s48-c-k-no-mo-rj-c0xffffff/photo.jpg')
        emb.set_footer(text="ManGoYT", icon_url="https://cdn.discordapp.com/emojis/329991214327660544.png")
        return emb

    @commands.command(pass_context=True)
    async def subsmango(self, ctx):
        parameters = {"id": "UC8HsUgcQ5OCB6CPAiGtOjQg", "key": "AIzaSyCssyjjfIcJpvl4CYoD20LbKcWIxQPNvw8", "part": "statistics",
                      "fields": "items/statistics/subscriberCount"}
        async with aiohttp.ClientSession() as session:
            async with session.get("https://www.googleapis.com/youtube/v3/channels", params=parameters) as r:
                if r.status == 200:
                    json_data = await r.json()
                    sub_count = json_data['items'][0]['statistics']['subscriberCount']
                    await self.bot.send_message(ctx.message.channel, embed=self.subs_emb(sub_count))
                else:
                    await self.bot.say('Error: Status {}, contact the creator'.format(r.status))

    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))
        # self.message = '**{}** Subscribers|Subscribe  -> :link: __**https://www.youtube.com/channel/UCdBgaPUcYkOEooVlV5rxrXw**__ '

    def subs_emb(self, subs):
        emb = discord.Embed(title="**{}** Subscribers|Subscribe 👇".format(subs),
                            description="🔗 **[ClickHere](https://www.youtube.com/channel/UCdBgaPUcYkOEooVlV5rxrXw)**<:kk:332133470572642317><:abdel:332139225107660802>",
                            color=0x9e30c2)
        emb.set_author(name="Abdel64", url="https://www.youtube.com/channel/UCdBgaPUcYkOEooVlV5rxrXw", icon_url="https://yt3.ggpht.com/-8JmQnUV5SU0/AAAAAAAAAAI/AAAAAAAAAAA/iXdHsJl4X3M/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")
        emb.set_thumbnail(url='https://yt3.ggpht.com/-8JmQnUV5SU0/AAAAAAAAAAI/AAAAAAAAAAA/iXdHsJl4X3M/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
        emb.set_footer(text="lol", icon_url="https://cdn.discordapp.com/emojis/329991214327660544.png")
        return emb

    @commands.command(pass_context=True)
    async def subsabdel(self, ctx):
        parameters = {"id": "UCdBgaPUcYkOEooVlV5rxrXw", "key": "AIzaSyCssyjjfIcJpvl4CYoD20LbKcWIxQPNvw8", "part": "statistics",
                      "fields": "items/statistics/subscriberCount"}
        async with aiohttp.ClientSession() as session:
            async with session.get("https://www.googleapis.com/youtube/v3/channels", params=parameters) as r:
                if r.status == 200:
                    json_data = await r.json()
                    sub_count = json_data['items'][0]['statistics']['subscriberCount']
                    await self.bot.send_message(ctx.message.channel, embed=self.subs_emb(sub_count))
                else:
                    await self.bot.say('Error: Status {}, contact the creator'.format(r.status))

    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))
        # self.message = '**{}** Subscribers|Subscribe  -> :link: __**https://www.youtube.com/channel/UCdBgaPUcYkOEooVlV5rxrXw**__ '

    def subs_emb(self, subs):
        emb = discord.Embed(title="**{}** Subscribers|Subscribe 👇".format(subs),
                            description="🔗 **[ClickHere](https://www.youtube.com/channel/UCdBgaPUcYkOEooVlV5rxrXw)**<:kk:332133470572642317><:abdel:332139225107660802>",
                            color=0x9e30c2)
        emb.set_author(name="Abdel64", url="https://www.youtube.com/channel/UCdBgaPUcYkOEooVlV5rxrXw", icon_url="https://yt3.ggpht.com/-8JmQnUV5SU0/AAAAAAAAAAI/AAAAAAAAAAA/iXdHsJl4X3M/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")
        emb.set_thumbnail(url='https://yt3.ggpht.com/-8JmQnUV5SU0/AAAAAAAAAAI/AAAAAAAAAAA/iXdHsJl4X3M/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
        emb.set_footer(text="lol", icon_url="https://cdn.discordapp.com/emojis/329991214327660544.png")
        return emb					


def setup(bot):
    bot.add_cog(Subss(bot))