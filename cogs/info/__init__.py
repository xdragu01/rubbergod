from __future__ import annotations

from typing import TYPE_CHECKING

from .cog import Info

if TYPE_CHECKING:
    from rubbergod import Rubbergod


def setup(bot: Rubbergod):
    bot.add_cog(Info(bot))
