import random

import disnake
from disnake.ext import commands

from config import cooldowns
from config.app_config import config
from config.messages import Messages
import utils


class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cooldowns.short_cooldown
    @commands.command(brief=Messages.random_pick_brief, usage=Messages.random_pick_usage)
    async def pick(self, ctx, *args):
        """"Pick an option"""
        for i, arg in enumerate(args):
            if "?" in arg:
                args = args[i + 1:]
                break
        if not len(args):
            await ctx.send(utils.get_command_signature(ctx))
            return

        option = disnake.utils.escape_mentions(random.choice(args))
        if option:
            await ctx.send(f"{option[:1900]} {ctx.author.mention}")

    @cooldowns.short_cooldown
    @commands.slash_command(name="flip", description=Messages.random_flip_brief)
    async def flip(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(random.choice(["True", "False"]))

    @cooldowns.short_cooldown
    @commands.slash_command(name="roll", description=Messages.rng_generator_format)
    async def roll(self, inter: disnake.ApplicationCommandInteraction, first: int, second: int = 0):
        if first > second:
            first, second = second, first

        option = str(random.randint(first, second))
        await inter.response.send_message(option)

    @pick.error
    @roll.error
    @flip.error
    async def command_error(self, ctx, error):
        if isinstance(error, (commands.MissingRequiredArgument, commands.BadArgument)):
            await ctx.send(utils.get_command_signature(ctx))
        if isinstance(error, commands.CheckFailure):
            await ctx.message.channel.send(
                utils.fill_message("bot_room_redirect", user=ctx.message.author.id, bot_room=config.bot_room)
            )

    def _channel_id(self, ctx):
        return ctx.channel.parent_id if type(ctx.channel) == disnake.Thread else ctx.channel.id

    async def cog_after_invoke(self, ctx):
        channel_id = self._channel_id(ctx)
        if channel_id not in config.allowed_channels:
            await ctx.message.channel.send(
                utils.fill_message("bot_room_redirect", user=ctx.message.author.id, bot_room=config.bot_room)
            )

    async def cog_check(self, ctx):
        if not config.enable_room_check:
            return True
        if not ctx.guild:
            return True
        return self._channel_id(ctx) in config.allowed_channels


def setup(bot):
    bot.add_cog(Random(bot))
