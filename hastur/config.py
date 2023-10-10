import os
from abc import ABC, abstractmethod
from configparser import ConfigParser
from typing import Callable, Optional, TypeVar

# Generic type for hints
T = TypeVar("T")

class ConfigSection(ABC):
    SECTION = None

    @abstractmethod
    def __init__(self, config: ConfigParser):
        assert self.SECTION is not None, f"Missing SECTION for {self.__class__.__name__}" 
        self._config = config

    @classmethod
    @abstractmethod
    def update_with_default(cls, config: ConfigParser):
        raise NotImplemented

    def _get_key(self, key: str) -> str:
        return self._config.get(self.SECTION, key)

    def _try_get_key(self, key: str) -> Optional[str]:
        return self._config.get(self.SECTION, key, fallback=None)

    def _get_key_as(self, key: str, converter: Callable[[str], T]) -> T:
        return converter(self._config.get(self.SECTION, key))

    def _try_get_key_as(self, key: str, converter: Callable[[str], T]) -> Optional[T]:
        try:
            return converter(self._config.get(self.SECTION, key))
        except Exception:
            return None

    @classmethod
    def _update_key(cls, config: ConfigParser, key: str, value: str):
        if not config.has_option(cls.SECTION, key):
            config.set(cls.SECTION, key, value)


class DiscordApiConfig(ConfigSection):
    SECTION = "DiscordAPI"

    def __init__(self, config: ConfigParser):
        super(DiscordApiConfig, self).__init__(config)
        self.token = self._get_key('token')

    @classmethod
    def update_with_default(cls, config: ConfigParser):
        cls._update_key(config, 'token', '')


class Config(object):
    def __init__(self, config: ConfigParser):
        self.discord_api = DiscordApiConfig(config)

    @staticmethod
    def from_file(filename: str) -> "Config":
        config_path = os.path.realpath(filename)
        if not os.path.exists(config_path):
            raise OSError(f"{config_path} doesn't exist")
        if not os.path.isfile(config_path):
            raise OSError(f"{config_path} is not a file")

        config = ConfigParser()
        config.read(config_path)
        return Config(config)

    @staticmethod
    def update_with_default(filename: str):
        config = ConfigParser()
        config_path = os.path.realpath(filename)
        if os.path.exists(config_path):
            config.read(config_path)

        for section in [DiscordApiConfig]:
            if not config.has_section(section.SECTION):
                config.add_section(section.SECTION)
            section.update_with_default(config)

        with open(config_path, 'w') as f:
            config.write(f)
