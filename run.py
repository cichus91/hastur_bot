# Ensure proper Python version
import sys
assert sys.version_info >= (3, 10), "Only Python 3.10 or newer supported"

from argparse import ArgumentParser, Namespace
from hastur.command import CommandModule, CommandRunner


runner = CommandRunner()


@runner.command('bot', help='Run bot with given config file')
class BotCommand(CommandModule):
    @staticmethod
    def configure_parser(parser: ArgumentParser):
        parser.add_argument('-c', '--config', type=str, required=True, help="config file path")
        parser.add_argument('-l', '--log', type=str, default=None, help="log file path (standard output by default)")

    @staticmethod
    def run(args: Namespace):
        import asyncio
        import discord
        import logging
        from hastur.app import HasturBot
        from hastur.config import Config

        config = Config.from_file(args.config)
        if not config.discord_api.token:
            raise AttributeError("Discord API token not present in config")

        BotCommand._set_logging(args)

        bot = HasturBot()
        try:
            bot.run(config.discord_api.token, log_level=logging.INFO)
        except KeyboardInterrupt:
            # Gracefully logout and close
            loop = asyncio.get_event_loop()
            loop.run_until_complete(bot.change_presence(status=discord.Status.offline))
            loop.run_until_complete(bot.close())

    @staticmethod
    def _set_logging(args):
        import logging
        import os
        logger = logging.getLogger("discord")
        logger.setLevel(logging.INFO)
        if args.log:
            formatter = logging.Formatter('[{asctime}] {levelname} - {name}: {message}', "%Y-%m-%d %H:%M:%S", style='{')
            file_handler = logging.FileHandler(filename=os.path.realpath(args.log), encoding="utf-8", mode="a")
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)


@runner.command('update_config', help='Update existing / create new config file with defaults')
class UpdateConfigCommand(CommandModule):
    @staticmethod
    def configure_parser(parser: ArgumentParser):
        parser.add_argument('-c', '--config', type=str, required=True, help="config file path")

    @staticmethod
    def run(args: Namespace):
        from hastur.config import Config
        Config.update_with_default(args.config)


if __name__ == '__main__':
    runner.run()
