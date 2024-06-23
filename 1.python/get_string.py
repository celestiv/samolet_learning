from typing import Callable, Any
import logging


def html(tag: str) -> Callable[...,Any]:
    def decorator(func: Callable):
        def wrapper() -> str:
            return f"<{tag}>{func()}</{tag}>"
        return wrapper
    return decorator


@html("h1")
@html("p")
def get_string() -> str:
    return "this is a string"


@html("h2")
def get_string_two() -> str:
    return "this is another string"


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info(get_string())
