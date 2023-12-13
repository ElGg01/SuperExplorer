import flet as ft
import functions as f

logo = "./LogoSuperExplorer.jpeg"

def main(page: ft.Page):
    #CONFIGURACIÓN DE LA PAGINA
    page.title = "SUPER EXPLORER"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 50
    page.bgcolor = "#010044"
    page.window_width = 500
    page.window_height = 600
    # page.window_min_width = 500
    # page.window_min_height = 600
    # page.window_max_width = 500
    # page.window_max_height = 600
    page.window_resizable = False

    #FUNCIONES
    def checar(e):
        indice = e.control.selected_index
        if indice == 0:
            try:
                page.remove(ft_order_button)
                page.add(ft_remove_button)
            except:
                print("No se puede remover lo que no existe")
        if indice == 1:
            try:
                page.remove(ft_remove_button)
                page.add(ft_order_button)
            except:
                print("No se puede remover lo que no existe")
    def seleccionarCarpeta(e: ft.FilePickerResultEvent):
        ft_textfield.value = e.path
        ft_textfield.update()
    def eliminar(e):
        ft_remove_button.disabled = True
        ft_order_button.disabled = True

        finalizo, mensaje = f.eliminarCarpetasVacias(ft_textfield.value)
        page.snack_bar = ft.SnackBar(ft.Text(mensaje))

        if finalizo:
            ft_remove_button.disabled = False
            ft_order_button.disabled = False

            ft_textfield.value = ""
            page.snack_bar.open = True
            page.update()
    def organizar(e):
        ft_remove_button.disabled = True
        ft_order_button.disabled = True

        finalizo, mensaje = f.organizarCarpetas(ft_textfield.value)
        page.snack_bar = ft.SnackBar(ft.Text(mensaje))

        if finalizo:
            ft_remove_button.disabled = False
            ft_order_button.disabled = False

            ft_textfield.value = ""
            page.snack_bar.open = True
            page.update()


    #COMPONENTES
    pick_path_dialog = ft.FilePicker(on_result=seleccionarCarpeta)

    ft_navigation_bar = ft.NavigationBar(
                destinations=[
                    ft.NavigationDestination(icon=ft.icons.DELETE, label="Borrar"),
                    ft.NavigationDestination(icon=ft.icons.REORDER, label="Ordenar")
                ], on_change=checar, bgcolor="#202429"
            )
    ft_logo = ft.Image(logo, width=200, height=200)
    ft_title = ft.Text(spans=[ft.TextSpan("SUPER EXPLORER", ft.TextStyle(size=40, weight=ft.FontWeight.BOLD))])
    ft_textfield = ft.TextField(label="Ruta:", border_color="WHITE", read_only=True)
    ft_remove_button = ft.FilledTonalButton("Eliminar las carpetas vacías", on_click=eliminar)
    ft_order_button = ft.FilledTonalButton("Organizar archivos", on_click=organizar)

    page.overlay.append(pick_path_dialog)

    page.add(
        ft_logo,
        ft_title,
        ft.Row([ft_textfield, ft.FilledTonalButton("Buscar", icon=ft.icons.FOLDER_OPEN, on_click=lambda _: pick_path_dialog.get_directory_path("Escoge una ruta:"))], alignment=ft.MainAxisAlignment.CENTER),
        ft_remove_button,
        ft_navigation_bar
    )

ft.app(target=main)