from data import DataEspecifica
from aluno import Aluno
from questionario import Questionario
from relatorio import Relatorio


def main():
    nome_aluno = input("Digite o nome do aluno: ")
    aluno = Aluno(nome_aluno)

    data_str = input("Digite a data no formato dd/mm/aa: ")
    try:
        data = DataEspecifica(data_str)
    except ValueError as e:
        print(e)
        return

    questionario = Questionario(aluno)
    questionario.coletar_respostas()
    
    relatorio = Relatorio(questionario, data)
    relatorio.gerar_relatorio()

if __name__ == "__main__":
    main()
