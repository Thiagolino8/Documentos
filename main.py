from Documento import Documento


while True:
    documento = (input("Insira seu documento: ")).strip()
    documento = Documento.cria(documento)
    if not documento:
        continue
    break

print(documento)
