from features.rg import Rubbergod

from .cog import Meme


def setup(bot: Rubbergod):
    bot.add_cog(Meme(bot))
