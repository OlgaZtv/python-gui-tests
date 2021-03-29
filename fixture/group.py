class GroupHelper:

    def __init__(self, app):
        self.app = app

    def get_group_list(self):
        self.open_group_editor()
        #открыть диалог
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        #получаем у дерева корневой узел
        group_list = [node.text() for node in root.children()]
        # получаем у дерева вложенные узлы - формируем список, сохраняем в список, который будет возвращать метод get_group_list в качестве результата
        self.close_group_editor()
        #закрыть диалог
        return group_list


    def add_new_group(self, name):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        input = self.group_editor.window(class_name="Edit")
        #поле ввода
        input.set_text(name)
        # ввели имя
        input.type_keys("\n")
        # нажали enter
        self.close_group_editor()


    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        #кликнули по кнопке добавить группу
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible")
        #ждем пока диалоговое окно станет видимым

    def close_group_editor(self):
        self.group_editor.close()
        #закрыли диалоговое окно
