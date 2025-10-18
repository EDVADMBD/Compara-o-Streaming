# Compara-o-Streaming
Projeto inicial em Python para coletar e comparar preços de serviços de streaming.
Storytelling: Descobrindo os Melhores Preços de Streaming

Imagine que você quer aproveitar suas séries e filmes favoritos sem gastar uma fortuna. Com tantas opções de streaming disponíveis — Netflix, Disney+, Prime Video, HBO Max, Globoplay — a dúvida é: qual serviço oferece o melhor custo-benefício?

Foi exatamente isso que motivou o nosso projeto. Criamos um robô inteligente em Python capaz de vasculhar todos os serviços de streaming, coletar os planos disponíveis e os preços, e transformar essas informações em dados claros e visuais.

O que descobrimos?

Menor preço por serviço
A primeira análise nos mostrou quais serviços têm o plano mais barato em cada plataforma. Alguns serviços surpreendem com opções econômicas, enquanto outros oferecem planos mais completos, mas com preço mais elevado.

Comparação detalhada de planos
Não se trata apenas de preço. Cada serviço oferece planos diferentes: qualidade de vídeo (HD, Full HD, 4K), número de telas simultâneas e recursos adicionais. Nosso projeto organiza tudo isso em uma tabela interativa, permitindo comparar lado a lado.

Visualização interativa
Criamos gráficos de barras interativos com Plotly, mostrando claramente qual plano vale mais a pena pelo preço, além de permitir explorar cada serviço, plano e suas características sem precisar ler longas listas de preços.

Dados acessíveis e atualizados
Todo o processo é automatizado: em alguns minutos, o código coleta os dados mais recentes, limpa e organiza, gerando arquivos CSV para análise futura ou integração em dashboards.

O impacto

Esse projeto ajuda qualquer usuário a tomar decisões inteligentes sobre onde investir seu dinheiro em streaming, evitando gastar mais do que precisa e aproveitando o melhor conteúdo de acordo com suas preferências.

Além disso, serve como um exemplo de ciência de dados aplicada a situações do dia a dia, combinando raspagem de dados, tratamento de informações, visualizações e interatividade em um único fluxo de trabalho.



# Projeto Stream Prices - Boilerplate
Projeto inicial em Python para coletar e comparar preços de serviços de streaming.
1. Estrutura do Repositório

<img width="819" height="460" alt="image" src="https://github.com/user-attachments/assets/e2933c21-4c82-410e-941e-266e57c6d0c4" />
2. Instalação e Execução

1. Crie um ambiente virtual:
   python -m venv .venv
   source .venv/bin/activate (Linux/Mac)
   .venv\Scripts\activate (Windows)

2. Instale as dependências:
   pip install -r requirements.txt

3. Instale o Playwright (se necessário):
   playwright install

4. Execute o script principal:
   python main.py

3. Principais Componentes

- fetchers/: classes responsáveis por buscar dados (API, HTML e JS dinâmico).
- normalizer.py: converte os dados brutos em formato padronizado.
- aggregator.py: define métricas e encontra o melhor preço.
- db.py: armazena as informações em SQLite.
- main.py: orquestra o fluxo de coleta e análise.

8. Próximos Passos

- Implementar parsers específicos para cada provedor (Netflix, Disney+, Prime, Globoplay, etc).
- Integrar API de câmbio para normalizar valores em diferentes moedas.
- Criar uma API com FastAPI para consultas externas.
- Adicionar testes unitários e suporte a Docker.



