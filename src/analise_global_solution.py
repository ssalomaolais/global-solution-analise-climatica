import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import re
import unidecode

def limpar_nomes_colunas(df):
    novas_colunas = []
    for coluna in df.columns:
        nome_limpo = unidecode.unidecode(coluna)
        nome_limpo = nome_limpo.lower()
        nome_limpo = re.sub(r'[^a-z0-9]+', '_', nome_limpo)
        nome_limpo = re.sub(r'_+', '_', nome_limpo)
        nome_limpo = nome_limpo.strip('_')
        novas_colunas.append(nome_limpo)
    df.columns = novas_colunas
    return df

print("--- INICIANDO ANÁLISE: EXERCÍCIO 01 ---")
file_path = 'INMET_S_RS_A801_PORTO ALEGRE_22-09-2000_A_31-12-2000.csv'

try:
    df = pd.read_csv(file_path, sep=';', skiprows=8, decimal=',', encoding='latin-1')
    df = limpar_nomes_colunas(df)
    print("Nomes das colunas após a limpeza automática:")
    print(df.columns.tolist())
    df['timestamp'] = pd.to_datetime(df['data_yyyy_mm_dd'] + ' ' + df['hora_utc'], format='%Y-%m-%d %H:%M')
    df.set_index('timestamp', inplace=True)
    df_clean = df[['temperatura_maxima_na_hora_ant_aut_degc', 'precipitacao_total_horario_mm', 'vento_velocidade_horaria_m_s']].copy()
    df_clean.rename(columns={
        'temperatura_maxima_na_hora_ant_aut_degc': 'temp_max_c',
        'precipitacao_total_horario_mm': 'precipitacao_mm',
        'vento_velocidade_horaria_m_s': 'velocidade_vento_ms'
    }, inplace=True)
    df_clean.replace(-9999.0, np.nan, inplace=True)
    df_clean.dropna(subset=['temp_max_c', 'velocidade_vento_ms'], inplace=True)
    df_clean['mes'] = df_clean.index.month
    print("\nDados carregados e limpos com sucesso.\n")
except Exception as e:
    print(f"\nOcorreu um erro inesperado: {e}")
    exit()

print("\n--- EXERCÍCIO 02: TABELAS DE FREQUÊNCIA ---")
freq_mes = df_clean['mes'].value_counts().sort_index().reset_index()
freq_mes.columns = ['Mês', 'Frequência de Horas']
print("\na) Tabela de Frequência para Mês (Discreta):")
print(freq_mes.to_string(index=False))

temp_var = df_clean['temp_max_c']
num_classes = int(1 + 3.322 * np.log10(len(temp_var)))
bins = pd.cut(temp_var, bins=num_classes)
print("\nb) Tabela de Frequência para Temperatura Máxima (Contínua):")
print(bins.value_counts().sort_index().to_frame(name='Frequência').reset_index().rename(columns={'index':'Classe de Temperatura (°C)'}).to_string(index=False))

print("\n\n--- EXERCÍCIO 04: ESTATÍSTICA DESCRITIVA ---")
var_temp = df_clean['temp_max_c']
desc_stats = var_temp.describe()
print(f"Estatísticas Descritivas para a Temperatura Máxima Horária (°C):")
print(desc_stats.to_string())
print(f"Moda: {var_temp.mode()[0]:.2f}")
print(f"Variância: {var_temp.var():.2f}")
print(f"Coeficiente de Variação (CV): {(var_temp.std() / var_temp.mean()) * 100:.2f}%")

print("\n\n--- EXERCÍCIO 06: MODELO DE REGRESSÃO LINEAR ---")
X = df_clean[['velocidade_vento_ms']]
y = df_clean['temp_max_c']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
r_quadrado = model.score(X_test, y_test)
print(f"Modelo para prever Temperatura com base na Velocidade do Vento:")
print(f"  - Coeficiente de Determinação (R²): {r_quadrado:.4f}")
print(f"  - Equação: Temp_Max = {model.intercept_:.2f} + ({model.coef_[0]:.2f}) * Velocidade_Vento")

print("\n\n--- EXERCÍCIO 03: GERANDO GRÁFICOS ---")
sns.set_theme(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.countplot(x='mes', data=df_clean, palette='viridis', order=sorted(df_clean['mes'].unique()))
plt.title('Contagem de Registros Horários por Mês (Set-Dez 2000)', fontsize=16)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Contagem de Horas', fontsize=12)
plt.xticks(ticks=range(len(sorted(df_clean['mes'].unique()))), labels=['Setembro', 'Outubro', 'Novembro', 'Dezembro'])
plt.show()

plt.figure(figsize=(12, 6))
sns.histplot(df_clean['temp_max_c'], kde=True, bins=20, color='indianred')
plt.title('Distribuição das Temperaturas Máximas Horárias em Porto Alegre', fontsize=16)
plt.xlabel('Temperatura Máxima Horária (°C)', fontsize=12)
plt.ylabel('Frequência', fontsize=12)
plt.axvline(df_clean['temp_max_c'].mean(), color='blue', linestyle='--', label=f"Média: {df_clean['temp_max_c'].mean():.2f}°C")
plt.legend()
plt.show()

plt.figure(figsize=(12, 6))
plt.scatter(X, y, alpha=0.3, label='Dados Reais')
plt.plot(X_test, model.predict(X_test), color='black', linewidth=3, label='Linha de Regressão')
plt.title('Regressão: Temperatura Máxima vs. Velocidade do Vento', fontsize=16)
plt.xlabel('Velocidade do Vento (m/s)', fontsize=12)
plt.ylabel('Temperatura Máxima Horária (°C)', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()

print("\n--- ANÁLISE CONCLUÍDA ---")