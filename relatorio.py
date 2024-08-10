import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader


class Relatorio:
    def __init__(self, questionario, data):
        self.questionario = questionario
        self.data = data

    def gerar_grafico(self, pontuacao):
        df = pd.DataFrame(list(pontuacao.items()), columns=['Categoria', 'Pontuação'])
        df.plot(kind='bar', x='Categoria', y='Pontuação', legend=False)
        plt.ylabel('Pontuação')
        plt.title('Pontuação por Categoria')
        plt.tight_layout()
        plt.savefig('grafico_pontuacao.png')

    def gerar_relatorio(self):
        pontuacao_total = sum(self.questionario.calcular_pontuacao().values())
        if  pontuacao_total < 20:
            classificacao = 'Sem Classificação'
        elif pontuacao_total <= 36:
            classificacao = 'Alerta'
        
        else:
            classificacao = 'Possível TDAH'

        relatorio_texto = (
            f"Relatório de Análise de TDAH\n\n"
            f"Nome do Aluno: {self.questionario.aluno.nome}\n"
            f"Data: {self.data}\n\n"
            f"Pontuação Total: {pontuacao_total}\n"
            f"Classificação: {classificacao}\n\n"
            f"Observações:\n\n"
            f"Com base na análise das 51 questões preenchidas pelo professor, o aluno {self.questionario.aluno.nome} apresentou uma pontuação total de {pontuacao_total}. "
            f"Esta pontuação classifica o aluno na categoria {classificacao}. \n\n"
            f"Recomendamos que este relatório seja encaminhado a um especialista para uma avaliação mais detalhada."
        )

        print("\n" + relatorio_texto)
        self.gerar_pdf(relatorio_texto, self.questionario.calcular_pontuacao())

    def gerar_pdf(self, relatorio_texto, pontuacao):
        self.gerar_grafico(pontuacao)
        
        c = canvas.Canvas(f"Relatorio_TDAH_{self.questionario.aluno.nome}.pdf", pagesize=letter)
        width, height = letter

        # Dividir o texto do relatório em linhas
        lines = relatorio_texto.split('\n')

        # Configurar a posição inicial do texto no PDF
        y = height - 40
        for line in lines:
            c.drawString(30, y, line)
            y -= 15  # Move para a próxima linha
            if y < 40:  # Adiciona uma nova página se o texto alcançar o fim da página
                c.showPage()
                y = height - 40

        # Adicionar o gráfico ao PDF
        c.showPage()  # Começar uma nova página
        c.drawImage(ImageReader('grafico_pontuacao.png'), 30, height / 2, width=width-60, height=height / 2 - 40)

        c.save()