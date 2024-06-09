from features.rg import Rubbergod

from .cog import Roles


def setup(bot: Rubbergod):
    bot.add_cog(Roles(bot))
