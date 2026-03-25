import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.add(
        ft.Icon(name=ft.icons.STAR, color="yellow", size=50),
        ft.Text("OFICINA ESTRELLA", size=30, weight="bold"),
        ft.Text("¡Conexión establecida con éxito!", color="green")
    )

app = ft.app(target=main, export_asgi=True)
