from features.rg import Rubbergod

from .cog import Forum


def setup(bot: Rubbergod):
    bot.add_cog(Forum(bot))
