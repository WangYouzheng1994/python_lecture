import json

from record_define import Record

"""
文件读取类的定义
"""


class FileReader:
    def read_data(self) -> list[Record]:
        pass


"""
文件读取接口实现--普通文本读取
"""
class TextFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        with open(self.path, "r", encoding="UTF-8") as file:
            readlines = file.readlines()
            for line in readlines:
                print(line.rstrip())

"""
文件读取接口实现--JSON文本读取
"""

class JSONFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        """
        读取数据，
        :return:
        """
        read_list = []
        with open(self.path, "r", encoding="UTF-8") as file:
            for line in file.readlines():
                loads = json.loads(line.rstrip().rstrip(","))
                # 这里也能看出来 python面向对象操作真的是很弱。。。
                read_list.append(self.dict_2_obj(loads, Record()))
        return read_list

    def read_data_full(self) -> list[Record]:
        """

        :return:
        """
        with open(self.path, "r", encoding="UTF-8") as file:
            full_text = file.read()
            # for jsonline in readlines:
            #     JSONDecoder.decode(line)
            print(json.loads(full_text))
            print(type(json.loads(full_text)))

    def dict_2_obj(self, source_dict, target_obj) -> object:
        """
        将dict类型转换成object
        :param source_dict:
        :param target_obj:
        :return:
        """
        for key in source_dict:
            # 反射
            hasattr(target_obj, key)
            setattr(target_obj, key, source_dict[key])
        else:
            return target_obj


# 测试代码
if __name__ == '__main__':

    # print("start--读取文档文件")
    # text_file_reader = TextFileReader("D:\\python实训\\12-面向对象三要素\\数据分析工程化案例\\test.json")
    # text_file_reader.read_data()
    # print("end--读取文档文件")
    #
    # print("start--读取json文档文件")
    # json_file_reader = JSONFileReader("D:\\python实训\\12-面向对象三要素\\数据分析工程化案例\\test.json")
    # print("#####start--行的方式读取json文档文件")
    # for record in json_file_reader.read_data():
    #     print(record)
    # print("#####end--行的方式读取json文档文件")
    # record = Record(name='123')
    # print(record)
    #
    print("#####start--批量的方式读取json文档文件")
    json_file_reader = JSONFileReader("D:\\python实训\\12-面向对象三要素\\数据分析工程化案例\\test_full.json")
    json_file_reader.read_data_full()
    print("#####end--批量的方式读取json文档文件")

    print("end--读取json文档文件")
