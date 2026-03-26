import flet as ft
import flet_fastapi
import fastapi

app = fastapi.FastAPI()

def main(page: ft.Page):
    page.title = "Oficina Estrella"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.add(
        ft.Icon(name=ft.icons.DASHBOARD_CUSTOMIZE_ROUNDED, color="cyan", size=60),
        ft.Text("SISTEMA OPERATIVO", size=30, weight="bold"),
        ft.Text("Conexión segura vía HTTP", color="green"),
        ft.Divider(),
        ft.ElevatedButton("INICIAR SESIÓN", on_click=lambda _: print("Acceso"))
    )
    page.update()

# ESTA ES LA LÍNEA QUE MATA EL ERROR DE WEBSOCKET:
# 'web_socket_path=None' obliga a usar Long Polling
app.mount("/", flet_fastapi.app(main, web_socket_path=None))
