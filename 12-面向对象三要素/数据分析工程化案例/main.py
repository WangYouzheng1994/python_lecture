from file_reader_define import JSONFileReader, TextFileReader
from record_define import Record

file_reader = TextFileReader('D:\\python实训\\12-面向对象三要素\\数据分析工程化案例\\test.json')
# json_reader = JSONFileReader('D:\\python实训\\12-面向对象三要素\\数据分析工程化案例\\test_full.json')

data = file_reader.read_data()
# read_data = json_reader.read_data()

print(data)



