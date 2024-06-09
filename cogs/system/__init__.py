from features.rg import Rubbergod

from .cog import System


def setup(bot: Rubbergod):
    bot.add_cog(System(bot))
