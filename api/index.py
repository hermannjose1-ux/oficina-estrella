import flet as ft
import flet_fastapi

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.add(
        ft.Icon(name=ft.icons.BOLT, color="yellow", size=50),
        ft.Text("¡OFICINA ONLINE!", size=32, weight="bold"),
        ft.Text("Seguridad configurada correctamente.", color="green")
    )

app = flet_fastapi.app(main)
