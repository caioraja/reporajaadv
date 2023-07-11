from src.config import *
from src.edicao_servicos import *
import docx
from src.COFquest_servicos import *


def main():
    while True:
        escolha = int(
            input(
                "Qual o documento será gerado? (1 - COF de serviços / 2 - COF de produtos / 3 - Contrato de serviços / 4 - Contrato de produtos / 5 - Pre Contrato): "
            )
        )
        if escolha == 1:
            doc = docx.Document(
                "D:/Programas/reporajaadv/src/modelos/COFSERVICOSv00.docx"
            )
            break
        elif escolha == 2:
            doc = docx.Document(
                "D:/Programas/reporajaadv/src/modelos/COFPRODUTOSv00.docx"
            )
            break
        else:
            print("Comando inválido /n")

    dc = questionario()
    log(dc)
    MARCA_DO_CLIENTE = dc["historia"][0]
    change_marca_cliente(doc, MARCA_DO_CLIENTE)
    for i in range(dc["n_Modelos"][0]):
        change_modelo(doc, f"M.O. 0{i+1}", dc[f"Modelo{i+1}"][0])
    ed_texto(doc, dc)


if __name__ == "__main__":
    main()
