import flet as ft
import flet_fastapi
import fastapi
from fastapi.middleware.cors import CORSMiddleware

# 1. Creamos la base del servidor
app = fastapi.FastAPI()

# 2. Le decimos al servidor que deje pasar los datos (Evita el gris)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def main(page: ft.Page):
    page.title = "Oficina Estrella"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Diseño de la oficina
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Icon(name=ft.icons.LOCK_OPEN_ROUNDED, color="green", size=50),
                ft.Text("OFICINA ESTRELLA", size=32, weight="bold"),
                ft.Text("CONEXIÓN ESTABLE", color="green", size=20),
                ft.Divider(),
                ft.ElevatedButton("ENTRAR AL SISTEMA", on_click=lambda _: print("Click")),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=40,
            bgcolor="#1e1e26",
            border_radius=20,
        )
    )
    page.update()

# 3. Montamos Flet sobre el servidor FastAPI
app.mount("/", flet_fastapi.app(main))
