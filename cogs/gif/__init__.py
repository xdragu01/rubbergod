from features.rg import Rubbergod

from .cog import Gif


def setup(bot: Rubbergod):
    bot.add_cog(Gif(bot))
