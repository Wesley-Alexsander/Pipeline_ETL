import csv
import json


class Dados:
    def __init__(self, dados) -> None:
        self.dados = dados
        self.name_columns = self.__get_columns()
        self.len_rows = self.__size_data()

    @staticmethod
    def __load_json(path):
        with open(path, "r", encoding='utf-8') as file:
            dados = json.load(file)
            return dados

    @staticmethod
    def __load_csv(path):
        dados = []
        with open(path, "r", encoding='utf-8') as file:
            spamreader = csv.DictReader(file, delimiter=",")
            for row in spamreader:
                dados.append(row)
        return dados

    def __get_columns(self):
        return list(self.dados[-1].keys())

    def __size_data(self):
        return len(self.dados)

    def __transform_tablelist(self):
        table_data = [self.name_columns]
        for row in self.dados:
            linha = []
            for colunm in self.name_columns:
                linha.append(row.get(colunm, "Indisponivel"))
            table_data.append(linha)
        return table_data

    def rename_columns(self, key_map):
        self.dados = [
            {key_map[old_key]: value for old_key, value in old_dict.items()}
            for old_dict in self.dados
        ]
        self.name_columns = self.__get_columns()

    def save_csv(self, path):
        combined_table = self.__transform_tablelist()

        with open(path, "w", encoding="utf-8-sig", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(combined_table)

    @classmethod
    def load_data(cls, path, data_type):
        dados = []
        if data_type.lower() == 'csv':
            dados = cls.__load_csv(path)
        elif data_type.lower() == 'json':
            dados = cls.__load_json(path)
        return cls(dados)

    @classmethod
    def merge(cls, first_sample, second_sample):
        combined_list = []
        combined_list.extend(first_sample.dados)
        combined_list.extend(second_sample.dados)
        return cls(combined_list)

    # @staticmethod
    # def merge(first_sample, second_sample):
    #     combined_list = []
    #     combined_list.extend(first_sample.dados)
    #     combined_list.extend(second_sample.dados)
    #     return Dados(combined_list)
