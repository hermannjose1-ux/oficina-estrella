import flet as ft
import flet_fastapi
import fastapi

app = fastapi.FastAPI()

async def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.add(
        ft.Icon(name=ft.icons.CHECK_CIRCLE_OUTLINE, color="green", size=60),
        ft.Text("OFICINA ESTRELLA", size=30, weight="bold"),
        ft.Text("SERVIDOR ACTIVO", color="white70")
    )
    page.update()

# Usamos la montura estándar, sin parámetros extra que causen el 500
app.mount("/", flet_fastapi.app(main))
