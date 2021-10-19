from .. import loader
import random

class testMod(loader.Module):
    strings = {"name": "Test"}
    async def testcmd(self, message):
         rand = random.randint(0, 100)
         await message.respond("Ты гей на " + str(rand) + "%")
