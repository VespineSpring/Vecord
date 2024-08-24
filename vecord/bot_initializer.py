# By Vespine | https://bit.ly/vespine

import discord
from discord.ext import commands


class Bot(commands.Bot):
    def __init__(self, command_prefix, intents: discord.Intents, **kwargs):
        super().__init__(
            command_prefix=commands.when_mentioned_or(command_prefix),
            intents=intents,
            **kwargs
        )

    async def on_ready(self):
        print(f'Logged on as {self.user} (ID: {self.user.id})')
        await self.tree.sync()

    def run(self, token: str):
        super().run(token=token)
