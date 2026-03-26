import flet as ft
import flet_fastapi
import fastapi

app = fastapi.FastAPI()

def main(page: ft.Page):
    page.title = "Oficina Estrella"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Limpieza total de errores previos
    page.clean()
    
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Icon(name=ft.icons.TIPS_AND_UPDATES_ROUNDED, color="yellow", size=60),
                ft.Text("OFICINA ESTRELLA", size=32, weight="bold"),
                ft.Text("SISTEMA ONLINE (MODO HTTP)", color="green"),
                ft.Divider(),
                ft.Text("Conexión estable sin WebSockets", italic=True)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=40,
            bgcolor="#1a1a22",
            border_radius=20
        )
    )
    page.update()

# ESTA CONFIGURACIÓN ES LA QUE MATA EL GRIS:
# web_socket_path=None -> Obliga a usar peticiones normales (Long Polling)
app.mount("/", flet_fastapi.app(
    main, 
    web_socket_path=None, 
    web_renderer=ft.WebRenderer.HTML
))
