import flet as ft
import flet_fastapi
import fastapi

# Creamos el motor
app = fastapi.FastAPI()

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.add(
        ft.Icon(name=ft.icons.STARS_SHARP, color="blue", size=60),
        ft.Text("OFICINA ESTRELLA", size=32, weight="bold"),
        ft.Text("CONEXIÓN ESTABLECIDA", color="green"),
        ft.Text("Si ves esto, ganamos la guerra.", size=16)
    )
    page.update()

# Esta es la forma oficial. Sin trucos, sin configuraciones raras.
app.mount("/", flet_fastapi.app(main))
