import flet as ft
import flet_fastapi

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.add(
        ft.Icon(name=ft.icons.CHECK_CIRCLE, color="green", size=50),
        ft.Text("SISTEMA ONLINE", size=30, weight="bold"),
        ft.Text("Flet y Vercel están hablando el mismo idioma.", color="white70")
    )

# ESTO ES LO QUE REEMPLAZA AL ERROR:
app = flet_fastapi.app(main)
