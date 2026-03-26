import flet as ft
import flet_fastapi

async def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Icon(name=ft.icons.AUTO_AWESOME, color="yellow", size=60),
                ft.Text("OFICINA ESTRELLA", size=35, weight="bold"),
                ft.Text("CONEXIÓN POR HTTP (SINFÍN)", color="green"),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=40,
            bgcolor="#1e1e26",
            border_radius=20,
        )
    )
    page.update()

# CONFIGURACIÓN CRÍTICA PARA VERCEL:
# web_renderer=ft.WebRenderer.HTML evita el uso de CanvasKit/WebSockets
app = flet_fastapi.app(main, web_renderer=ft.WebRenderer.HTML)
