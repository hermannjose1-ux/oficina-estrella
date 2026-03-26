import flet as ft
import flet_fastapi

# Definimos la función principal
async def main(page: ft.Page):
    page.title = "Oficina Estrella"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Agregamos el contenido
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Icon(name=ft.icons.WAVEOUT_OUTLINED, color="cyan", size=50),
                ft.Text("OFICINA ESTRELLA", size=32, weight="bold"),
                ft.Text("CONEXIÓN EXITOSA", color="green", size=20),
                ft.Divider(),
                ft.Text("Esperando órdenes del operador...", italic=True, color="white70")
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            border_radius=15,
            bgcolor=ft.colors.SURFACE_VARIANT
        )
    )
    page.update()

# Esta es la forma exacta que Vercel necesita para no quedarse "cargando"
app = flet_fastapi.app(main)
