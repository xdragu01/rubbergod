from features.rg import Rubbergod

from .cog import Nameday


def setup(bot: Rubbergod):
    bot.add_cog(Nameday(bot))
