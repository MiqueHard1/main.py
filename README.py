import csv
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# ==========================================
# 1. GERADOR DO DOCUMENTO DE REQUISITOS (PDF)
# ==========================================
def gerar_pdf_requisitos():
    nome_arquivo = "Levantamento_de_Requisitos_Entregable1.pdf"
    doc = SimpleDocTemplate(nome_arquivo, pagesize=letter,
                            rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    
    styles = getSampleStyleSheet()
    story = []

    # Estilos customizados
    titulo_style = ParagraphStyle('Titulo', parent=styles['Heading1'], fontSize=20, leading=24, textColor=colors.HexColor("#1A365D"), spaceAfter=15)
    subtitulo_style = ParagraphStyle('Subtitulo', parent=styles['Heading2'], fontSize=14, leading=18, textColor=colors.HexColor("#2B6CB0"), spaceBefore=12, spaceAfter=8)
    corpo_style = ParagraphStyle('Corpo', parent=styles['Normal'], fontSize=10, leading=14, spaceAfter=6)

    # Conteúdo do PDF
    story.append(Paragraph("DOCUMENTO DE LEVANTAMENTO DE REQUISITOS (ENTREGÁVEL 1)", titulo_style))
    story.append(Paragraph("<b>Ambiente de Execução:</b> Terminal do GitHub Codespaces (Python 3.x)", corpo_style))
    story.append(Spacer(1, 15))

    story.append(Paragraph("1. Requisitos Funcionais (RF)", subtitulo_style))
    rf_dados = [
        ["ID", "Descrição", "Implementação no Código"],
        ["RF01", "Menu Interativo", "Loop 'while' no terminal com validação de opções numéricas."],
        ["RF02", "Matriz de Controle", "Estrutura de dados bidimensional (lista de listas) para gerenciar dados."],
        ["RF03", "Leitura de Arquivo CSV", "Módulo 'csv' nativo para carregar dados externos dinamicamente."],
        ["RF04", "Cálculos Automatizados", "Funções matemáticas para somatória e médias dos elementos da matriz."],
        ["RF05", "Validação de Dados", "Tratamento de exceções (try/except) para entradas inválidas do usuário."]
    ]
    tabela_rf = Table(rf_dados, colWidths=[40, 160, 320])
    tabela_rf.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2B6CB0")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(tabela_rf)
    story.append(Spacer(1, 15))

    story.append(Paragraph("2. Requisitos Não Funcionais (RNF)", subtitulo_style))
    rnf_dados = [
        ["ID", "Categoria", "Propriedade", "Especificação Técnica"],
        ["RNF01", "Ambiente", "Plataforma", "Execução via CLI no GitHub Codespaces."],
        ["RNF02", "Linguagem", "Compatibilidade", "Desenvolvido estritamente em Python 3.x."],
        ["RNF03", "Portabilidade", "Dependências", "Uso de bibliotecas nativas (excepto reportlab para este PDF)."],
        ["RNF04", "Usabilidade", "Interface", "Interface de texto (CLI) clara, limpa e em português."]
    ]
    tabela_rnf = Table(rnf_dados, colWidths=[50, 70, 80, 320])
    tabela_rnf.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2D3748")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(tabela_rnf)

    doc.build(story)
    print(f"\n[✓] Sucesso: O arquivo '{nome_arquivo}' foi gerado com êxito!")

# ==========================================
# 2. SISTEMA INTERATIVO (MATRIZ E REQUISITOS)
# ==========================================
matriz_controle = []

def carregar_csv():
    global matriz_controle
    nome_csv = "dados.csv"
    
    # Criar um CSV de exemplo caso não exista para evitar erros
    if not os.path.exists(nome_csv):
        with open(nome_csv, mode='w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f)
            escritor.writerow(["ID", "Valor1", "Valor2"])
            escritor.writerow(["1", "10.5", "20.0"])
            escritor.writerow(["2", "15.0", "30.5"])
        print(f"[*] Arquivo '{nome_csv}' de exemplo criado automaticamente.")

    try:
        with open(nome_csv, mode='r', encoding='utf-8') as f:
            leitor = csv.reader(f)
            cabecalho = next(leitor)
            matriz_controle = [cabecalho] # Inclui o cabeçalho na matriz
            for linha in leitor:
                # Validação básica de conversão de dados
                id_linha = int(linha[0])
                v1 = float(linha[1])
                v2 = float(linha[2])
                matriz_controle.append([id_linha, v1, v2])
        print("[✓] CSV carregado com sucesso para a Matriz de Controle!")
    except Exception as e:
        print(f"[X] Erro ao ler o arquivo CSV: {e}")

def exibir_matriz():
    if not matriz_controle:
        print("[!] A matriz está vazia. Carregue o CSV primeiro (Opção 2).")
        return
    print("\n--- MATRIZ DE CONTROLE ATUAL ---")
    for linha in matriz_controle:
        print(f"| {str(linha[0]).ljust(6)} | {str(linha[1]).ljust(10)} | {str(linha[2]).ljust(10)} |")

def calcular_metricas():
    if len(matriz_controle) <= 1:
        print("[!] Dados insuficientes na matriz para realizar cálculos.")
        return
    
    valores_v1 = [linha[1] for i, linha in enumerate(matriz_controle) if i > 0]
    valores_v2 = [linha[2] for i, linha in enumerate(matriz_controle) if i > 0]
    
    soma_v1 = sum(valores_v1)
    media_v2 = sum(valores_v2) / len(valores_v2)
    
    print("\n--- RESULTADOS DOS CÁLCULOS ---")
    print(f" Somatória da coluna 'Valor1': {soma_v1:.2f}")
    print(f" Média aritmética da coluna 'Valor2': {media_v2:.2f}")

def menu():
    while True:
        print("\n=========================================")
        print("         SISTEMA DE GERENCIAMENTO        ")
        print("=========================================")
        print("[1] Gerar PDF de Levantamento de Requisitos")
        print("[2] Ler Arquivo CSV")
        print("[3] Visualizar Matriz de Controle")
        print("[4] Executar Cálculos e Métricas")
        print("[0] Sair do Sistema")
        print("=========================================")
        
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                gerar_pdf_requisitos()
            elif opcao == 2:
                carregar_csv()
            elif opcao == 3:
                exibir_matriz()
            elif opcao == 4:
                calcular_metricas()
            elif opcao == 0:
                print("Encerrando o sistema... Até logo!")
                break
            else:
                print("[X] Opção inválida! Escolha um número do menu.")
        except ValueError:
            print("[X] Entrada inválida! Por favor, digite apenas números inteiros.")

if __name__ == "__main__":
    menu()

