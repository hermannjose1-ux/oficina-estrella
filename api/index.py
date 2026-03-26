import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.add(
        ft.Icon(name=ft.icons.STARS_ROUNDED, color="amber", size=60),
        ft.Text("OFICINA ESTRELLA", size=30, weight="bold"),
        ft.Text("SISTEMA DE SEGURIDAD ACTIVO", color="white70")
    )

# No usamos flet_fastapi aquí, dejamos que flet maneje el inicio
if __name__ == "__main__":
    ft.app(target=main)
