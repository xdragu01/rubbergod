from features.rg import Rubbergod

from .cog import Karma


def setup(bot: Rubbergod):
    bot.add_cog(Karma(bot))
