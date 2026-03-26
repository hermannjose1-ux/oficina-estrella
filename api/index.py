import flet as ft
import flet_fastapi

def main(page: ft.Page):
    page.title = "Oficina Estrella"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Limpiamos todo rastro de error anterior
    page.clean()
    
    page.add(
        ft.Icon(name=ft.icons.VERIFIED_USER_ROUNDED, color="blue", size=60),
        ft.Text("CONEXIÓN ESTABLE", size=30, weight="bold"),
        ft.Text("Modo de compatibilidad Vercel activado", color="white70")
    )
    page.update()

# ESTA CONFIGURACIÓN MATA EL ERROR DE WEBSOCKETS
app = flet_fastapi.app(
    main,
    web_renderer=ft.WebRenderer.HTML,
    use_color_emoji=True
)
