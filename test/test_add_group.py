def test_add_group(app):
    old_list = app.groups.get_group_list()
    #получаем старый список групп
    app.groups.add_new_group("my group")
    new_list = app.groups.get_group_list()
    #получаем новый список групп
    old_list.append("my group")
    #отличается одним элементом
    assert sorted(old_list) == sorted(new_list)
    #сортируются просто списки строк поэтому дополнительных функций для сортировки не нужно
