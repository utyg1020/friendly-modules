from .. import loader, utils

import logging
import asyncio
import time

class Test(loader.Module):
    strings = {"name": "Test"}

    async def testcmd(self, message):
        await client.send_message('chat_id', 'Привет это мой модуль!')