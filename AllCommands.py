import discord
from discord.ext import commands
import asyncio
import json
from .check import checks
import aiohttp
import time
from cogs.utils.dataIO import dataIO
import os
import random

class Comm:
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))  	

    @commands.command(pass_context=True)
    async def discord(self,ctx):
        """DiscordForum"""
        embed = discord.Embed(
            title="**HelpMe**",
            color=0x7691eb,
            description="**getting started**")
        embed.set_thumbnail(url="http://www.ethicon.com/sites/all/themes/ethicon/img/ajax-loader.gif")    
        embed.set_author(name="DiscordHelp", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
        embed.add_field(name="🇫🇷👈👇", value="🔥**https://support.discordapp.com/hc/fr**🔥", inline=False)
        embed.add_field(name="🇺🇸👈👇", value="🔥**https://support.discordapp.com/hc/en-us**🔥", inline=False)
        embed.add_field(name="🇩🇪👈👇", value="🔥**https://support.discordapp.com/hc/de**🔥", inline=False)
        embed.add_field(name="🇪🇸👈👇", value="🔥**https://support.discordapp.com/hc/es**🔥", inline=False)
        embed.add_field(name="🇮🇹👈👇", value="🔥**https://support.discordapp.com/hc/it**🔥", inline=False)
        await self.bot.send_message(discord.Object(ctx.message.channel.id), embed=embed)
		
    @commands.command(pass_context=True)
    async def ping(self,ctx):
        """ping"""
        channel = ctx.message.channel
        t1 = time.perf_counter()
        await self.bot.send_typing(channel)
        t2 = time.perf_counter()
        await self.bot.send_typing(channel)
        embed = discord.Embed(
            title="**<:omgtroll:299208059685961728>PONG🏓**",
            color=0xff2429,
            description="{}ms<:NoNoNo:312251052902842370>".format(round((t2-t1)*1000)))
        t3 = time.perf_counter()
        await self.bot.send_message(discord.Object(ctx.message.channel.id), embed=embed)

    @commands.command(pass_context=True)
    async def regles(self,ctx):
        """regles"""
        embed=discord.Embed(
            title="Merci de lire attentivement les règles suivantes :",
            description="l",
            color=0xf7ff51)
        embed.set_author(name="Règles ! ", icon_url='https://www.emojibase.com/resources/img/emojis/hangouts/270c.png')
        embed.set_thumbnail(url='https://www.emojibase.com/resources/img/emojis/hangouts/270c.png')
        embed.add_field(name="1⃣", value="*Respectez vous, pas d'insultes, pas de harcèlement. ", inline=False)
        embed.add_field(name="2⃣", value="*Ne spammez pas. ", inline=False)
        embed.add_field(name="3⃣", value="*Pas de contenu gore, porn ou choquant.", inline=False)
        embed.add_field(name="4⃣", value="**Pas de pub pour votre serveur ou autre.", inline=False)
        embed.add_field(name="5⃣", value="Utilisez les bons channels ! ", inline=False)
        embed.add_field(name="6⃣", value="Une question ? Tag un @MoDo ! ", inline=False)
        embed.add_field(name="7⃣", value="Des émotes son à votre disposition respecter les MERCI!", inline=False)
        embed.add_field(name="8⃣", value="Pas de spam envers les @MoDo. ", inline=False)
        embed.add_field(name="9⃣", value="Soyez actifs ! ", inline=False)
        embed.add_field(name="🔟", value="Respectez les règles. ", inline=False)
        embed.add_field(name="Sanction ! ⚠", value="1 Warn , 2 Warns , 3 Warns=Kick, 5 Warns=BAN", inline=False)
        embed.add_field(name="* = Warn pour non respect de la règle ! ", value="<:staff:340076038832783362><:Stop:309724359461830658>", inline=True)
        await self.bot.send_message(discord.Object(ctx.message.channel.id), embed=embed)

    @commands.command(pass_context=True)        
    @checks.is_owner()
    async def new(self,ctx):
        embed=discord.Embed(
            title="News ! HAHA YESSS",
            color=0x180776,
            description="News #rules")
        embed.set_author(name="Update", icon_url='https://cdn.discordapp.com/attachments/357926498654617602/361617459683524609/LOGOo.png')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/357926498654617602/361617802953490432/News.png')
        embed.set_footer(text="24/09/17 23h00")
        await self.bot.send_message(discord.Object(ctx.message.channel.id), embed=embed)    	
		
    @commands.command(pass_context=True)        
    @checks.is_owner()
    async def French(self,ctx):
        embed=discord.Embed(
            title="RIIIIIP FRENCH DISCORD",
            color=0x180776,
            description="La chaine TF1 s'est offert un bad buzz ce week-end en présentant le service Discord comme un logiciel créé par les militants de la France Insoumise... https://www.generation-nt.com/journal-televise-tf1-annonce-discord-cree-france-insoumise-actualite ")
        embed.set_author(name="France Is Bad", icon_url='https://cdn.discordapp.com/attachments/357926498654617602/361617459683524609/LOGOo.png')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/357926498654617602/361617802953490432/News.png')
        embed.set_footer(text="Nope")
        await self.bot.send_message(discord.Object(ctx.message.channel.id), embed=embed) 

    @commands.command()
    async def love(self):
        """Idk"""
        if self.bot.user.bot:
            await self.bot.whisper("I love youu <3")
        else:
            await self.bot.say("I love you <3") 		
		
def setup(bot):
    bot.add_cog(Comm(bot))