# Global Solution 2025: Modelo Preditivo para Eventos Climáticos

![Python](https://img.shields.io/badge/Python-3776AB?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3776AB?logo=matplotlib)
![Scikit-learn](https://img.shields.io/badge/SciKit--Learn-F7931E?logo=scikit-learn)

## 📖 Contexto do Projeto

Este projeto foi desenvolvido como parte da **Global Solution do 1º Semestre de 2025**, que desafia os estudantes a criar soluções tecnológicas para enfrentar os impactos de eventos climáticos extremos.

O objetivo deste trabalho é desenvolver um modelo preditivo de IA capaz de antecipar eventos como enchentes e ondas de calor, utilizando dados meteorológicos históricos.

## 📝 Metodologia e Análise

A análise foi conduzida utilizando um conjunto de dados históricos do **INMET (Instituto Nacional de Meteorologia)** para a estação de Porto Alegre - RS. O script em Python realiza as seguintes etapas:

1.  **Análise de Frequência:** Criação de tabelas de distribuição de frequências para variáveis quantitativas discretas e contínuas.
2.  **Visualização de Dados:** Geração de dois gráficos distintos para explorar visualmente as variáveis do dataset.
3.  **Estatística Descritiva:** Realização de análises univariadas, calculando medidas de tendência central (média, mediana, moda), dispersão (variância, desvio padrão) e separatrizes (quartis).
4.  **Modelagem Preditiva:** Desenvolvimento de um modelo de **Regressão Linear Simples** para prever uma variável de interesse com base em outra.

Todos os resultados, tabelas, gráficos e interpretações foram consolidados em um relatório estatístico detalhado.

## 🚀 Como Executar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU-USUARIO/global-solution-analise-climatica.git](https://github.com/SEU-USUARIO/global-solution-analise-climatica.git)
    cd global-solution-analise-climatica
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o script de análise:**
    ```bash
    python src/analise_global_solution.py
    ```

