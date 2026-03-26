import flet as ft

def main(page: ft.Page):
    page.title = "Oficina Estrella"
    page.theme_mode = ft.ThemeMode.DARK
    page.add(ft.Text("¡OFICINA ONLINE!", size=30, weight="bold"))

# Cambiamos la forma de lanzar la app para que sea más compatible con Vercel
ft.app(target=main, port=8000, view=ft.AppView.WEB_BROWSER)
