# Ensure proper Python version
import sys
assert sys.version_info >= (3, 10), "Only Python 3.10 or newer supported"

import asyncio
import os
import discord
import dotenv
import logging

from hastur.app import HasturBot


def run():
    # Parent dir of this file
    base_path = os.path.dirname(os.path.realpath(__file__))

    bot = HasturBot()
    token = dotenv.dotenv_values(dotenv_path=os.path.join(base_path, "environ", ".env"))['TOKEN']

    formatter = logging.Formatter('[{asctime}] {levelname} - {name}: {message}', "%Y-%m-%d %H:%M:%S", style='{')

    file_handler = logging.FileHandler(filename=os.path.join(base_path, "discord.log"), encoding="utf-8", mode="a")
    file_handler.setFormatter(formatter)

    logger = logging.getLogger("discord")
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)

    try:
        bot.run(token, log_level=logging.INFO)
    except KeyboardInterrupt:
        # Gracefully logout and close
        loop = asyncio.get_event_loop()
        loop.run_until_complete(bot.change_presence(status=discord.Status.offline))
        loop.run_until_complete(bot.close())


if __name__ == '__main__':
    # TODO: more commands and options (use argparse)
    run()
