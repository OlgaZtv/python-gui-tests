from comtypes.client import CreateObject
import os

project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
#Путь к директории проекта


xl = CreateObject("Excel.Application")
#создать объект эксель
xl.Visible = 1
wb = xl.Workbooks.Add()
#новая рабоя книга
for i in range (10):
    xl.Range["A%s" % (i+1)].Value[()] = "group %s" % i
    #A%S - ячейка с переменным номером
wb.SaveAs(os.path.join(project_dir, "groups.xlxs"))
#сохраняем рабочую книгу и задачем имя файла
xl.Quit()
#закрыть эксель
