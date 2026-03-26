import flet as ft
import flet_fastapi

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(
        ft.Icon(name=ft.icons.CHIP, color="cyan", size=50),
        ft.Text("OFICINA ACTIVA", size=30, weight="bold"),
        ft.Text("El servidor está procesando el código.", color="green")
    )

app = flet_fastapi.app(main)
