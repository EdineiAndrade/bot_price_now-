# Bot_price_now:

# Desenvolvido em Python para comparar o preço de um produto em dois site distintos. 💻🌐

<h3>Desenvolvido no programa Destrava Dev - 11, do Dev Aprender | Jhonatan de Souza 🚀🚀</h3>
<div>
<img src="https://cdn.areademembros.com/image?p=instancia_2872%2Fimage%2FFTi9KwFXtq9vvoMUHCL2lcZG1NGi2KfpG9AGFMbV.png&w=200&h=350&t=crop&d=default-produto.png&uptkn=87c518f057c153774ee90f05ae0580bc" />

## Bibliotecas utilizadas

- selenium
- webdriver-manager
- pandas
- openpyxl
- flet

</div>

## Instruções:

<h3> Instalação das bibliotecas:</h3>

- Basta executar o comando:

```python
pip install -r requirements.txt
```

Nome do Projeto: Comparador de Preços Online

## Descrição

O Comparador de Preços Online é uma ferramenta desenvolvida em Python que automatiza a busca e comparação de preços de produtos entre dois dos maiores e-commerces do Brasil: Magazine Luiza e Mercado Livre. O objetivo principal do projeto é ajudar os consumidores a encontrar o melhor preço para um produto específico, economizando tempo e dinheiro.

## Funcionalidades

1. **Busca Automatizada:** O usuário insere o nome do produto desejado, clica em pesquisar e a ferramenta realiza buscas automáticas nos sites do Magazine Luiza e Mercado Livre.
2. **Extração de Dados:** Utilizando técnicas de web scraping, a ferramenta extrai os preços dos produtos listados em ambos os sites.
3. **Comparação de Preços:** Os preços extraídos são comparados, e a ferramenta identifica qual site oferece o produto pelo menor preço.
4. **Exibição de Resultados:** Os dos dois produtos são salvos no excel e apresentado na tela o de menor valor, com o nome do produto, valor e plataforma.

## Documentação das tecnologias Utilizadas

- **Python:** Linguagem de programação principal do projeto. [Documentação Oficial](https://www.python.org/)
- **Selenium:** Biblioteca utilizada para automação de navegação e extração de dados dos sites. [Documentação Oficial](https://www.selenium.dev/documentation/)
- **Pandas:** Biblioteca para manipulação e análise de dados. [Documentação Oficial](https://pandas.pydata.org/getting_started.html)
- **Flet:** Biblioteca para criação de uma interface gráfica amigável para o usuário. [Documentação Oficial](https://flet.dev/docs/)

## Benefícios

- **Economia de Tempo:** Automatiza a busca de preços, eliminando a necessidade de o usuário visitar manualmente cada site.
- **Economia de Dinheiro:** Ajuda os consumidores a encontrar o melhor preço disponível para o produto desejado.
- **Facilidade de Uso:** Interface intuitiva que permite ao usuário realizar buscas e obter resultados com poucos cliques.

## Extra: Transformando o arquivo em .exe

1. Instalar o PyInstaller

```python
pip install pyinstaller
```

2. Verificar o arquivo Python
   Certifique-se de que seu script Python está funcionando corretamente. Por exemplo, suponha que você tenha um arquivo chamado meu_script.py.
3. Converter o arquivo Python em executável(com icone)

```python
pyinstaller --onefile --icon=meu_icone.ico --noconsole meu_script.py

```
