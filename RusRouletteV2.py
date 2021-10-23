from .. import loader, utils
import random
from asyncio import sleep

class RusRouletteMod(loader.Module):
    strings = {"name": "RusRoul"}
    
    async def rusroulcmd(self, message):
        rurou = ["Ты умер!", "Ты выжил но за дверью тебя ждут люди)", "Ты выжил но следущая прокрутка была не холостой!", "Ты выжил но за дверью тебя ждут близкие не играй больше", "Ты выжил патрон был не настоящим!"]
        inviz = 0
        rand = random.choice(rurou)
        await message.edit(rand)
        await sleep(0.9)
        if rand == "Ты умер!":
            await message.edit("Твой аккаунт удалится через ...")
            await sleep(0.9)
            await message.edit("3...")
            await sleep(0.5)
            await message.edit("2..")
            await sleep(0.5)
            await message.edit("1.")
            await sleep(0.5)
            await message.edit("0")
            while inviz != 99:
                await message.edit("Удаления аккаунта выполнено на " + str(inviz) + "%")
                inviz += 1
            await sleep(0.5)
            await message.edit("АХХАХХАХ это фейк) Не бойся")
            await sleep(0.9)
            await message.delete()
            