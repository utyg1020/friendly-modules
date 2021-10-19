from .. import loader
async def client_ready(self, client, db):
        self.db = db 

class testMod(loader.Module):
    strings = {"name": "Test"}
    async def testcmd(self, message):
        await message.respond("Привет это мой модуль!")
