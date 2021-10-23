from .. import loader
from asyncio import sleep
import random

class ChatHackV2Mod(loader.Module):
	strings = {"name": "ChatHackV2"}
	async def chathackv2cmd(self, message):
		i = 0
		vzlom = ("Взлом успешен! В базе данных можно посмотреть сворованные данные", "Взлом был провален... Пока мы взламывали нас заметила система защиты и поменяла все пароли")
		rand2 = random.choice(vzlom)
		while i != 100:
			await message.edit("Взлом чата выполнен на " + str(i) + "%")
			i += 1
			if i == 50:
				await message.respond("50% Достигнуто начинаеться взлом базы данных")
				await sleep(10)
			await sleep(0.1)
		await message.edit(rand2)
		