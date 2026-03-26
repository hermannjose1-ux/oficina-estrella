import flet as ft

def main(page: ft.Page):
    page.title = "Oficina Estrella"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Icon(name=ft.icons.CELL_TOWER, color="blue", size=50),
                ft.Text("OFICINA CONECTADA", size=30, weight="bold"),
                ft.Text("La señal está llegando correctamente", color="white70")
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20
        )
    )
    page.update()

# FORZAMOS EL MODO WEB PURO
if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
