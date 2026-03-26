import flet as ft
import flet_fastapi
import fastapi

# 1. Creamos la app de FastAPI
app = fastapi.FastAPI()

async def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Icon(name=ft.icons.ROCKET_LAUNCH, color="orange", size=50),
                ft.Text("OFICINA ESTRELLA", size=32, weight="bold"),
                ft.Text("CONEXIÓN ESTABLECIDA", color="green"),
                ft.Divider(),
                ft.Text("Si ves esto, el gris murió.", italic=True)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=30,
            bgcolor="#1a1a22",
            border_radius=15
        )
    )
    page.update()

# 2. MONTAMOS CON CONFIGURACIÓN ANTIBLOQUEO
# Usamos 'web_renderer' en html para que sea más liviano
app.mount("/", flet_fastapi.app(main, web_renderer=ft.WebRenderer.HTML))
