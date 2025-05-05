from enum import StrEnum
import re

class Color(StrEnum):
    # Text Colors
    BLACK       = "\033[30m"
    RED         = "\033[31m"
    GREEN       = "\033[32m"
    YELLOW      = "\033[33m"
    BLUE        = "\033[34m"
    MAGENTA     = "\033[35m"
    CYAN        = "\033[36m"
    WHITE       = "\033[37m"
    RESET       = "\033[0m"

    # Bright Text Colors
    BRIGHT_BLACK   = "\033[90m"
    BRIGHT_RED     = "\033[91m"
    BRIGHT_GREEN   = "\033[92m"
    BRIGHT_YELLOW  = "\033[93m"
    BRIGHT_BLUE    = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN    = "\033[96m"
    BRIGHT_WHITE   = "\033[97m"

    # Background Colors
    BG_BLACK   = "\033[40m"
    BG_RED     = "\033[41m"
    BG_GREEN   = "\033[42m"
    BG_YELLOW  = "\033[43m"
    BG_BLUE    = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN    = "\033[46m"
    BG_WHITE   = "\033[47m"

from enum import StrEnum

class TextStyle(StrEnum):
    # Styles
    BOLD       = "\033[1m"
    UNDERLINE  = "\033[4m"
    REVERSED   = "\033[7m"

class msg:

    @staticmethod
    def warn(message: str,
             prefix_str: bool = True) -> None:
        """
        Function to display warning message
        """
        if prefix_str:
            print("{}{}Warning: {}{}".format(TextStyle.BOLD, Color.YELLOW, message, Color.RESET))
        else:
            print("{}{}{}{}".format(TextStyle.BOLD, Color.YELLOW, message, Color.RESET))

    @staticmethod
    def error(message: str,
              prefix_str: bool = True) -> None:
        """
        Function to display error message
        """
        if prefix_str:
            print("{}{}Error: {}{}".format(TextStyle.BOLD, Color.RED, message, Color.RESET))
        else:
            print("{}{}{}{}".format(TextStyle.BOLD, Color.RED, message, Color.RESET))

def resize_images_to_max_dim(images):
    pass

def resize_images_to_min_dim(images):
    pass

def __natural_sort_key(s):
    # Split the string into chunks of digits and non-digits
    return [int(text) if text.isdigit() else text.lower() for text in re.split('(\d+)', s)]

def natural_sort(lst):
    return sorted(lst, key=__natural_sort_key)
