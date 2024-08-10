import datetime

class DataEspecifica:
    def __init__(self, data_str):
        self.data = self.validar_data(data_str)

    def validar_data(self, data_str):
        try:
            data = datetime.datetime.strptime(data_str, "%d/%m/%y")
            return data
        except ValueError:
            raise ValueError("Data inválida. Use o formato dd/mm/aa.")

    def __str__(self):
        return self.data.strftime("%d/%m/%y")