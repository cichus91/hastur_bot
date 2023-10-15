from abc import ABC, abstractmethod
from argparse import ArgumentParser, Namespace
from typing import Callable, Optional, Type


class CommandModule(ABC):

    @staticmethod
    def configure_parser(parser: ArgumentParser):
        pass

    @staticmethod
    @abstractmethod
    def run(args: Namespace):
        raise NotImplemented


class CommandRunner(object):

    def __init__(self):
        self._parser = ArgumentParser()
        self._subparsers = self._parser.add_subparsers(required=True)

    def command(self, name: str, help: Optional[str] = None) -> Callable[[Type[CommandModule]], Type[CommandModule]]:
        """
        Wrapper for Module classes for registering commands
        """
        def module_wrapper(cls: Type[CommandModule]) -> Type[CommandModule]:
            subparser = self._subparsers.add_parser(name, help=help)
            cls.configure_parser(subparser)
            subparser.set_defaults(_run=cls.run)
            return cls
        return module_wrapper

    def run(self):
        args = self._parser.parse_args()
        args._run(args)
