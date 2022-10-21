import win32api
import win32file
#Модуль для работы с файлами и папками
import shutil
import os

#Определение информации о дисках
def is_drive_ready(drive_name):
    try:
        win32api.GetVolumeInformation(drive_name) 
        return True
    except:
        return False



print("  Информация о логических дисках")
#Получение названий дисков системы

drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
print(drives)
for letter in drives:
    print("Название: ", letter)
    print("Тип: ", win32file.GetDriveType(letter))
 
    if is_drive_ready(letter):
        total, used, free = shutil.disk_usage(letter)
        print("Всего: %d ГБ" % (total // (2 ** 30)))
        print("Использовано: %d ГБ" % (used // (2 ** 30)))
        print("Свободно: %d ГБ" % (free // (2 ** 30)))
        t = win32api.GetVolumeInformation(letter)
        print("Метка:", t[0])
    print("------------------------------")

# Работа с файлом
print("  Работа с файлом")
my_file = open("Files.txt", "w+")
print("Введите строку для записи:")
string = input()
my_file.write(string)
my_file.close()
my_file = open("Files.txt", "r")
print("Текст записан в файл")
print("Содержание файла: ", end="")
print(my_file.read())
my_file.close()
os.remove(my_file.name)

# JSON файл
import json

print("  Работа с JSON")
print("Name = ", end="")
Name_ = input()
print("Age = ", end="")
data = {'Name': Name_, 'Age': input()}
outfile = open('data.json', 'w+')
json.dump(data, outfile)
outfile.close()
outfile = open('data.json', 'r+')
print("Текст записан в файл")
print(outfile.read())
outfile.close()
os.remove(outfile.name)

# HTML файл

import xml.etree.ElementTree as ET

print("  Работа с XML")
print("Родитель = ", end="")
par = ET.Element(input())

#Добавляем элементы
print("Ребенок1 = ", end="")
child = ET.SubElement(par,input())
tree = ET.ElementTree(par)
tree.write("HTML.xml")

tree = ET.parse('HTML.xml')
root = tree.getroot()
element = root[0]
print("Ребенок2 = ", end="")
ET.SubElement(element, input())
print("Текст записан в файл")
print("Содержание файла XML:")
tree.write("HTML.xml")



ET.dump(tree)

os.remove('HTML.xml')

# Zip-архив
import zipfile
print("  ZIP архив")
newzip = zipfile.ZipFile('ZED.zip', 'w',zipfile.ZIP_DEFLATED)
print("Файл ZipZip.txt заархивирован")
newzip.write('ZipZip.txt')
newzip.close()

newzip = zipfile.ZipFile('ZED.zip', 'r',zipfile.ZIP_DEFLATED)

newzip.extractall()
print("Содержание ZIP-файла:")
newzip.printdir()
newzip.close()
os.remove('ZED.zip')
