import random


class DataGenerator:
    first_names = ["ivan", "vladimir", "michail", "petr", "roman"]
    last_names = ["ivanov", "petrov", "sidorov", "bubnov", "listov"]

    @staticmethod
    def generate_random_name():
        first_name = random.choice(DataGenerator.first_names)
        last_name = random.choice(DataGenerator.last_names)
        return first_name, last_name

    @staticmethod
    def generate_email(cohort_number='17', domain="yandex.ru"):
        first_name, last_name = DataGenerator.generate_random_name()
        random_numbers = str(random.randint(100, 999))
        email = first_name + last_name + cohort_number + random_numbers + "@" + domain
        return email

    @staticmethod
    def generate_password():
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        password = ""
        for _ in range(6):
            password += random.choice(characters)
        return password

    @staticmethod
    def generate_short_password():

        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        password = ""
        for _ in range(5):
            password += random.choice(characters)
        return password
