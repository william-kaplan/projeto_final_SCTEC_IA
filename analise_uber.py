import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Carregar os dados
df = pd.read_csv('ncr_ride_bookings.csv')

# Limpeza e Preparação Simples
df = df.dropna()

# Análise Exploratória (AED)
print("Resumo dos Dados")
print(df.describe())
print("Contagem de Status de Corrida")
status_counts = df['Booking Status'].value_counts()
print(status_counts)

# Visualizações
# Criar pasta para salvar as imagens se não existir
if not os.path.exists('visualizacoes'):
    os.makedirs('visualizacoes')

# Gráfico 1: Distribuição dos Status das Corridas
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Booking Status', hue='Booking Status', palette='viridis', legend=False)
plt.title('Distribuição do Status das Corridas')
plt.xlabel('Status')
plt.ylabel('Quantidade')
plt.savefig('visualizacoes/status_corridas.png')
plt.close()

# Gráfico 2: Valor das Corridas por Tipo de Veículo
plt.figure(figsize=(12, 6))
sns.barplot(
    data=df, 
    x='Vehicle Type', 
    y='Booking Value', 
    hue='Vehicle Type', 
    estimator=sum, 
    palette='magma', 
    legend=False)
plt.title('Valor Total por Tipo de Veículo')
plt.xlabel('Tipo de Veículo')
plt.ylabel('Valor Total (R$)')
plt.savefig('visualizacoes/valor_por_veiculo.png')
plt.close()

# Gráfico 3: Distribuição das Avaliações dos Motoristas
plt.figure(figsize=(8, 5))
df['Driver Ratings'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title('Distribuição das Avaliações dos Motoristas')
plt.xlabel('Avaliação (1-5)')
plt.ylabel('Número de Corridas')
plt.savefig('visualizacoes/avaliacoes_motoristas.png')
plt.close()

print("Análise concluída! As visualizações foram salvas na pasta 'visualizacoes'.")

# Conclusões para a IA
print("Insights para Modelos de IA")
print("1. Padrão Identificado: A maioria das corridas é concluída com sucesso.")
print("2. Variável Relevante: O 'Vehicle Type' influencia diretamente no 'Booking Value'.")
print("3. Aplicação Futura: Estes dados podem ser usados para prever cancelamentos (Classificação) ou estimar o preço da corrida (Regressão).")
