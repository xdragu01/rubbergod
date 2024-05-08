"""
Cog controlling bookmarks. React with bookmark emoji and the bot will send copy of message to user.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import disnake
from disnake.ext import commands

from cogs.base import Base

from .features import Features
from .modals import Modal
from .views import View

if TYPE_CHECKING:
    from rubbergod import Rubbergod


class Bookmark(Base, commands.Cog):
    def __init__(self, bot: Rubbergod):
        super().__init__()
        self.bot = bot

    @commands.message_command(name="Bookmark", guild_ids=[Base.config.guild_id])
    async def bookmark(self, inter: disnake.ApplicationCommandInteraction, message: disnake.Message):
        """Send modal with input for bookmark name and then send to user"""
        await inter.response.send_modal(modal=Modal(message))

    async def bookmark_reaction(self, ctx):
        embed, images, files_attached = await Features.create_bookmark_embed(self, ctx)
        if images:
            for image in images:
                embed.append(await Features.create_image_embed(self, ctx, image))
        # when sending sticker there can be overflow of files
        if len(files_attached) <= 10:
            await ctx.member.send(embeds=embed, view=View(ctx.message.jump_url), files=files_attached)
        else:
            await ctx.member.send(embeds=embed, view=View(ctx.message.jump_url), files=files_attached[:10])
            await ctx.member.send(files=files_attached[10:])
