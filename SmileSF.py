from .. import loader, utils
import random
from asyncio import sleep

class SmileSFMod(loader.Module):
    strings = {"name": "SmileSF"}
    
    async def smilesfcmd(self, message):
        """write .smilesf help/Напишите .smilesf хелп"""
        args = utils.get_args_raw(message)
        if args == "создатель":
            await message.respond("Создатель: @score_fr")
        if args == "help":
            await message.edit("This module is designed to display animated emoticons.\n\nCommands:\n.smilesf 1 - 😁😄😃😀😆😅\n.smilesf 2 - ♥ ️❣️️❣️️💓💕💖💞\n.smilesf 3 - 👉👊💦")
        if args == "хелп":
            await message.edit("Этот модуль создан для вывода анимированных смайликов.\n\nКоманды:\n.smilesf 1 — 😁😄😃😀😆😅\n.smilesf 2 — ♥️❣️❤️💓💞\n.smilesf 3 — 👉👊💦")
        if args == "1":
            for _ in range(15):
                await message.edit("🤣😊😁😂😜")
                await sleep(0.3)
                await message.edit("😁😂🤣😊😜")
                await sleep(0.3)
                await message.edit("😁🤣😜😊😂")
                await sleep(0.3)
                await message.edit("😁😜😆😃😆")
                await sleep(0.3)
                await message.edit("😁😉😂😊😆")
                await sleep(0.3)
                await message.edit("😆🤣😁😃😉")
        if args == "2":
            for _ in range(15):
                await message.edit("💖💗💓❤😍💖")
                await sleep(0.3)
                await message.edit("🧡😍💖❣💗❣❤")
                await sleep(0.3)
                await message.edit("💖😍❣💓💖🧡💓")
                await sleep(0.3)
                await message.edit("💗😍💖❣❤🧡😍")
                await sleep(0.3)
                await message.edit("💓😍❤🧡💖💗")
                await sleep(0.3)
                await message.edit("🧡💓❤❣💓🧡😘")
        if args == "3":
            for _ in range(21):
                await message.edit("👉ᅠᅠᅠᅠᅠ👊")
                await sleep(0.3)
                await message.edit("👉ᅠᅠᅠᅠ👊")
                await sleep(0.3)
                await message.edit("👉ᅠᅠᅠ👊")
                await sleep(0.3)
                await message.edit("👉ᅠᅠ👊")
                await sleep(0.3)
                await message.edit("👉ᅠ👊")
                await sleep(0.3)
                await message.edit("👉👊")
                await sleep(0.3)
                await message.edit("👉👊💦")
                await sleep(0.3)
                await message.edit("👉👊💦💦")
                await sleep(0.3)
                await message.edit("👉👊💦💦💦")
                await sleep(0.3)
