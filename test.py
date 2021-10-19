from .. import loader, utils

import logging
import asyncio
import time

class test(loader.Module):
    strings = {"name": "Test"}
    async def testcmd(self, message):
        await message.respond("Привет это мой модуль!")
