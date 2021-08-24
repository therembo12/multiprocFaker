from faker import Faker
from faker.providers import BaseProvider

fake = Faker()


class Login(BaseProvider):
    def login(self):
        return 'Unknown login'


fake.add_provider(Login)


# data = fake.login()


# def text(data):
#     print(data)


# text(data)
count = 10000
data = []
for i in range(count+1):
    temp = {'name': fake.name(), 'login': fake.login(
    ), 'password': fake.password(), 'address': fake.address()}
    data.append(temp)

# for item in data:
#     print(item)
