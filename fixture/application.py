#main fixture
from pywinauto.application import Application as WinApplication
#для запуска программы
from fixture.group import GroupHelper


class Application:

    def __init__(self, target):
        #конструктор для инициализации тестируемого приложения target - путь к нему
        self.application = WinApplication(backend="win32").start(target)
        #вызвали конструктор импортируемого класса с параметром для вызова и старт с путем к исполяемому файлу
        self.main_window = self.application.window(title="Free Address Book")
        #сохранили метод с вызовом окна
        self.main_window.wait("visible")
        #ожидание видимости окна
        self.groups = GroupHelper(self)
        #сохраняем ссылку для используемого помощника c сылкой на текущий объект в качестве параметра

    def destroy(self):
        #останавливает тестируемое приложение(фикстуру разрушает)
        self.main_window.close()
        #находим основное окно программы с параметрами критерия поиска окна