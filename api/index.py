import flet as ft
import flet_fastapi
import fastapi

# 1. Definimos la app principal
app = fastapi.FastAPI()

def main(page: ft.Page):
    page.title = "Oficina Estrella"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Renderizado sencillo para que no se quede "pensando"
    page.add(
        ft.Column([
            ft.Icon(name=ft.icons.LIGHTBULB_ROUNDED, color="yellow", size=60),
            ft.Text("SISTEMA ONLINE", size=28, weight="bold"),
            ft.Text("Renderizado vía HTML puro", color="white70"),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )
    page.update()

# 2. CONFIGURACIÓN FINAL:
# web_renderer=ft.WebRenderer.HTML es la clave para que Vercel no bloquee la pantalla
app.mount("/", flet_fastapi.app(main, web_renderer=ft.WebRenderer.HTML))
