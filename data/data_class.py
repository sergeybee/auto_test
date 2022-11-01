from dataclasses import dataclass


@dataclass
class Client:
    """ Используется с модулем generate/generate.py для генерации тестовых данных """

    first_name: str = None
    last_name: str = None
    middle_name: str = None
    passport: str = None


