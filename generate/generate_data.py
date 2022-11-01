from faker import Faker
from data.data_class import Client

faker_ru = Faker('ru_RU')


def generated_client():
    return Client(
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        middle_name=faker_ru.middle_name()
    )
