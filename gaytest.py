from .. import loader
import random

class gayMod(loader.Module):
    """Этот модуль позволит вам узнать на сколько вы гей)"""
    strings = {"name": "GayTest"}
    async def gaycmd(self, message):
         rand = random.randint(0, 100)
         await message.delete()
         await message.respond("Ты гей на " + str(rand) + "%")