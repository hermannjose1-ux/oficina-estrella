import flet as ft
import flet_fastapi
import fastapi

# 1. Iniciamos el motor web
app = fastapi.FastAPI()

def main(page: ft.Page):
    page.title = "Oficina Estrella"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Diseño ultra-limpio para evitar errores de renderizado
    page.add(
        ft.Column([
            ft.Icon(name=ft.icons.TERMINAL_ROUNDED, color="green", size=60),
            ft.Text("SISTEMA OPERATIVO: ONLINE", size=28, weight="bold"),
            ft.Text("Vercel y Flet están sincronizados.", color="white70"),
            ft.Divider(),
            ft.Text("Esperando comandos...", italic=True, size=14)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )
    page.update()

# 2. Montamos la app de forma que Vercel la entienda al 100%
app.mount("/", flet_fastapi.app(main))
