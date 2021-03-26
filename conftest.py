import pytest

from fixture.application import Application


# сделали текстуру глобальной чтобы она запускалась один раз для всех тестов
@pytest.fixture(scope="session")
def app(request):
    fixture = Application('D:\\Teach\\Addressbook\\AddressBook.exe')
    # двойные бэкслеши для экранирования
    request.addfinalizer(fixture.destroy)
    # инициализируем финалайзер не вызываем метод дестрой, а передаем ссылку на него
    return fixture
