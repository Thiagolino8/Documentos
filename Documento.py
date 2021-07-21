from validate_docbr import CPF, CNPJ, CNS


class Documento:
    @staticmethod
    def cria(documento):
        if len(documento) == 11:
            return Cpf(documento)
        elif len(documento) == 14:
            return Cnpj(documento)
        elif len(documento) == 15:
            return Cns(documento)
        else: raise ValueError("DOCUMENTO INVÁLIDO!")



class Cpf:
    def __init__(self, cpf):
        if self.cpf_é_válido(cpf):
            self._cpf = cpf
        else:
            raise ValueError("CPF INVÁLIDO!")

    def cpf_é_válido(self, cpf):
        validador = CPF()
        return validador.validate(cpf)

    def __str__(self):
        return self.cpf_formatado()

    def cpf_formatado(self):
        formatador = CPF()
        return formatador.mask(self._cpf)


class Cnpj:
    def __init__(self, cnpj):
        if self.cnpj_é_válido(cnpj):
            self._cnpj = cnpj
        else:
            raise ValueError("CNPJ INVÁLIDO!")

    def cnpj_é_válido(self, cnpj):
        validador = CNPJ()
        return validador.validate(cnpj)

    def __str__(self):
        return self.cnpj_formatado()

    def cnpj_formatado(self):
        formatador = CNPJ()
        return formatador.mask(self._cnpj)


class Cns:
    def __init__(self, cns):
        if self.cns_é_válido(cns):
            self._cns = cns
        else:
            raise ValueError("CNS INVÁLIDO!")

    def cns_é_válido(self, cns):
        validador = CNS()
        return validador.validate(cns)

    def __str__(self):
        return self.cns_formatado()

    def cns_formatado(self):
        formatador = CNS()
        return formatador.mask(self._cns)
