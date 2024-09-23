from bot_price_now import scrape_product_info
import flet as ft
from go_product import go_product

def main(page: ft.Page):
    try:
        #Config página
        page.title = "Price Now"
        ft.Page.padding = 200
        page.prevent_scroll = True
        page.window_width = 500
        page.window_height = 470
        page.window_resizable = False
        
        # Ícone de carregamento
        loading_gif = ft.Image(src="https://cdn.pixabay.com/animation/2023/05/02/04/29/04-29-06-428_512.gif",width=150, height=150, visible=False,opacity=.7)
        
        # Função que será chamada ao clicar no botão
        def pesquisar(e):
            global link 
            try:
                if resultado.value != "":
                    resultado.value = ""
                    page.update()
                product = campo_input.value
                if product != "":
                    resultado.value = f"Pesquisando Por: {campo_input.value} \n"
                    resultado.color = "GREEN"
                    loading_gif.visible = True
                    label_resultado.visible = False
                    campo_input.value = ""
                    campo_input.label = ""
                    label_resultado.content.value = ""
                    page.update()
                    product_inf,file_path = scrape_product_info(product)
                    link = update_result(product_inf, file_path)
                    return link 
                else:
                    resultado.value = f"   DIGITE UM PRODUTO PARA PESQUISAR!!! 👆"
                    resultado.color = "RED"
                    page.update()
            except Exception as e:
                return f"Erro na busca dos dados: {e}"
        def update_result(product_inf,file_path):
            try:
                loading_gif.visible = False
                label_resultado.visible = True
                botao_navegar.visible = True
                resultado.value = f"Resultado da Pesquisa:"
                page.update()
                novo_texto = f"Arquivo Excel salvo em: \n{file_path}\nProduto: {product_inf[0]}\nValor: {product_inf[1]}\nPlataforma: {product_inf[2]}"
                label_resultado.content.value = novo_texto
                page.update()
                return product_inf[3]
            except Exception as e:
                return f"Erro na busca dos dados: {e}"
    
        # Função para abrir o link
        def open_link(e):
            if link:  # Verifica se o link está definido
                go_product(link)    
        # Cria o campo de input e o botão
        campo_input = ft.TextField(label="Digite o item para pesquisa", width=320,text_size=11)
        botao_pesquisar = ft.ElevatedButton(text="Pesquisar 🌐", on_click=pesquisar)
        botao_navegar = ft.ElevatedButton(text="Ir para o site 🔗", on_click=open_link)
        botao_navegar.visible = False
        page.update()
        # Cria um label para mostrar o resultado da pesquisa, com estilo de texto menor
        resultado = ft.Text(size=12)  # Tamanho menor do texto

        # Cria o label de resposta com a borda lilás clara
        label_resultado = ft.Container(
            content=ft.Text(""),
            border=ft.border.all(1, ft.colors.GREY_700),
            padding=10,
            border_radius=5,
            width=410,
            alignment=ft.alignment.center,
            height=200,
            margin=20
        )
        # Adiciona os componentes à página em uma linha (Row), com alinhamento central
        page.add(
        ft.Column(
            [
                ft.Row([campo_input, botao_pesquisar], alignment=ft.alignment.center),
                resultado,
                ft.Container(
                    content=loading_gif,
                    alignment=ft.alignment.center
                ),
                label_resultado,            
                botao_navegar,
            ],
            alignment=ft.alignment.center,  # Centraliza verticalmente na página
            horizontal_alignment=ft.alignment.center  # Centraliza horizontalmente os elementos
        )
    )
    except Exception as e:
        return f"Erro na busca dos dados: {e}"

ft.app(target=main)
