#!/usr/bin/python

import discord
import os
import random
import pkg_resources
from discord.ext import commands
import asyncio
import aiml

STARTUP_FILE = "std-startup.xml"
BOT_PREFIX = ('!')


class RinaBot:
    def __init__(self, channel_name, bot_token):
        self.channel_name = channel_name
        self.token = bot_token

        # Load AIML kernel
        self.kernel = aiml.Kernel()
        initial_dir = os.getcwd()
        os.chdir(pkg_resources.resource_filename(__name__, ''))  # Change directories to load AIML files properly
        startup_filename = pkg_resources.resource_filename(__name__, STARTUP_FILE)
        self.kernel.learn(startup_filename)
        self.kernel.respond("LOAD AIML B")
        os.chdir(initial_dir)

        # Set up Discord client
        self.client = discord.Client()
        self.bot = commands.Bot(command_prefix=BOT_PREFIX)
        self.setup()
        # create the background task and run it in the background
    def setup(self):
        @self.client.event
        async def on_ready():
            print("\n=============================")
            print("=    *** BOT ONLINE ***     =")
            print("=============================")
            print("NAMA BOT: {}".format(self.client.user.name))
            print("ID: {}".format(self.client.user.id))
            print("=============================\n")
        async def status_task(self):
            while True:
                await self.client.change_presence(activity=discord.Game(name='⬆️ Mau request bot sendiri?'))
                await asyncio.sleep(5)
                await self.client.change_presence(activity=discord.Game(name='↗️ Mau belajar buat bot sendiri?'))
                await asyncio.sleep(5)
                await self.client.change_presence(activity=discord.Game(name='➡️ Mau Tutorial free hosting botmu?'))
                await asyncio.sleep(5)
                await self.client.change_presence(activity=discord.Game(name='↘️ Mau jadi pacar Rendiix? 😍'))
                await asyncio.sleep(5)
                await self.client.change_presence(activity=discord.Game(name='⬇️ Boleh, tapi khusus cewek 😘'))
                await asyncio.sleep(5)
                await self.client.change_presence(activity=discord.Game(name='↙️ Caranya mudah 👌'))
                await asyncio.sleep(5)
                await self.client.change_presence(activity=discord.Game(name='⬅️ Hubungi 💌'))
                await asyncio.sleep(5)
                await self.client.change_presence(activity=discord.Game(name='↖️ 😎 Owner NewBieGamers 😎'))
                await asyncio.sleep(5)

        @self.client.event
        async def on_message(message):
            if message.author.bot or str(message.channel) != self.channel_name:
                return
            
            if message.content is None:
                return
            print("PESAN: " + str(message.content))

            if self.kernel.respond(message.content)  == "":
                return
            else:
                msg = ("<@" + str(message.author.id) + "> " + self.kernel.respond(message.content))
                print("RESPON: " + str(msg))
                await message.channel.send(msg)

    def loop(self):
        self.client.loop.create_task(status_task())

    def run(self):
        self.client.run(self.token)
