import flet as ft
import flet_fastapi
import fastapi

app = fastapi.FastAPI()

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.add(
        ft.Icon(name=ft.icons.TELEVISION_OFF_OUTLINED, color="red", size=50),
        ft.Text("PRUEBA DE CONEXIÓN", size=30, weight="bold"),
        ft.Text("Si ves esto, matamos al 500 y al Gris.", color="white70")
    )
    page.update()

# Esta es la forma más estable de montar Flet en Vercel
app.mount("/", flet_fastapi.app(main))
