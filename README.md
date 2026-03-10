📊 Análise de Dados: Booking de Corridas (NCR)
Este projeto foi desenvolvido durante o curso de Introdução à Inteligência Artificial no SCTEC. O objetivo principal foi realizar uma Análise Exploratória de Dados (AED) em um conjunto de dados de reservas de corridas, identificando padrões de comportamento e preparando o terreno para futuros modelos de IA.

📝 Sobre o Projeto
A ideia foi transformar dados brutos em informações visuais. Através da linguagem Python, analisei como as corridas se distribuem por status (concluídas, canceladas, etc.), qual o impacto do tipo de veículo no faturamento e como os motoristas estão sendo avaliados.

🛠️ Tecnologias Utilizadas
Python: Linguagem principal.
Pandas: Para manipulação e limpeza dos dados.
Matplotlib & Seaborn: Para a criação de gráficos e visualizações.
OS: Para automação da gestão de pastas e arquivos.

📈 Insights Gerados
Após o processamento dos dados, conseguimos identificar pontos-chave:
Eficiência Operacional: A maioria das corridas é concluída com sucesso, o que indica uma boa saúde do serviço.
Faturamento por Categoria: O tipo de veículo é um fator determinante no valor final da corrida.
Potencial para IA: Os dados estão prontos para alimentar modelos de Classificação (para prever cancelamentos) ou Regressão (para estimar preços de novas corridas).

📁 Estrutura do Repositório
ncr_ride_bookings.csv: Base de dados utilizada.
analise_corridas.py: Script Python com o código do projeto.
/visualizacoes: Pasta contendo os gráficos gerados automaticamente pelo código.