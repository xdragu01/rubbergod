from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

import disnake

from buttons.base import BaseView
from config.app_config import config
from permissions import permission_check

if TYPE_CHECKING:
    from rubbergod import Rubbergod


class View(BaseView):
    def __init__(self, bot: Rubbergod):
        super().__init__(timeout=None)
        self.bot = bot

    @cached_property
    def contest_vote_channel(self) -> disnake.TextChannel:
        return self.bot.get_channel(config.contest_vote_channel)

    async def interaction_check(self, inter: disnake.Interaction) -> bool:
        return permission_check.submod_plus(inter)

    @disnake.ui.button(
        label="Přijmout návrh",
        emoji="✅",
        style=disnake.ButtonStyle.secondary,
        custom_id="contestvote:accept",
    )
    async def answer(self, button: disnake.ui.Button, inter: disnake.MessageInteraction) -> None:
        file = await inter.message.attachments[0].to_file()
        await self.contest_vote_channel.send(inter.message.content, file=file)
        await inter.message.edit(view=None)
        await inter.message.unpin()
