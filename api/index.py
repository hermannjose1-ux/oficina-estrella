import flet as ft
import flet_fastapi

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.add(
        ft.Text("🚀 OFICINA ESTRELLA", size=30, weight="bold"),
        ft.Text("Si ves esto, el servidor está VIVO.", color="green")
    )
    page.update()

# Esta línea es la única que Vercel necesita para conectar con el mundo
app = flet_fastapi.app(main)
