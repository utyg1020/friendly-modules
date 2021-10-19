from .. import loader

class testMod(loader.Module):
    strings = {"name": "Test"}
    async def testcmd(self, message):
        await message.respond("Привет это мой модуль!")
