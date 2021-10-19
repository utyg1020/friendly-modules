from .. import loader
import random
async def client_ready(self, client, db):
        self.db = db 

class testMod(loader.Module):
    strings = {"name": "Test"}
    async def testcmd(self, message):
         await message.respond("Ты гей на " + str(0,100))
