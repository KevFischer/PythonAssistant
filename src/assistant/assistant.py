import os
import ctypes
import locale
import platform
import configparser


class Assistant:

    def __init__(self, debug: bool = False) -> None:
        """
        Initialize assistant instance.
        :param debug: Debug mode for more detailed logs.
        """

        self.debug = debug
        self.user = os.getlogin()
        self.config = configparser.ConfigParser()
        self.config.read("./cfg/assistant.cfg")

        # Set language, different methods for different OS
        if "Windows" in platform.system():
            windll = ctypes.windll.kernel32
            windll.GetUserDefaultUILanguage()
            self.language = locale.windows_locale[windll.GetUserDefaultUILanguage()]
        else:
            self.language = os.getenv('LANG')

        return

    def setup(self):
        print(self.config)

    def run(self) -> None:
        """
        Actual program loop, after setup
        :return: None
        """
        if self.config["Default"]["Name"] == "":
            self.setup()
        return
