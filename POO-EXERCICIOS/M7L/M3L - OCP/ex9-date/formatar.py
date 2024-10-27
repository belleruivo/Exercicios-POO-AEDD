from date import Date

class FormatadorData:
    def formatar(self, data: Date):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses")

class FormatadorISO(FormatadorData):
    def formatar(self, data: Date):
        return f"{data.get_ano()}-{data.get_mes():02}-{data.get_dia():02}"

class FormatadorUS(FormatadorData):
    def formatar(self, data: Date):
        return f"{data.get_mes():02}/{data.get_dia():02}/{data.get_ano()}"

class FormatadorPadrao(FormatadorData):
    def formatar(self, data: Date):
        return f"{data.get_dia():02}/{data.get_mes():02}/{data.get_ano()}"