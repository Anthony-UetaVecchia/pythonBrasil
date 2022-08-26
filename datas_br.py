from datetime import datetime, timedelta


class DatasBr:
    def __init__(self):
        self.momento_cadastrado = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro", "fevereiro", "marco",
            "abril", "maio", "junho", "julho",
            "agosto", "setembro", "outubro",
            "novembro", "dezembro"
        ]
        mes_cadastro = self.momento_cadastrado.month - 1
        return meses_do_ano[mes_cadastro]

    def dia_semana(self):
        dia_da_semana = [
            "domingo", "segunda", "terca",
            "quarta", "quinta", "sexta", "sabado"
        ]
        dia_semana = self.momento_cadastrado.weekday() + 1
        return dia_da_semana[dia_semana]

    def format_data(self):
        data_formatada = self.momento_cadastrado.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_cadastrado
        return tempo_cadastro
