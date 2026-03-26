import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.add(
        ft.Icon(name=ft.icons.CHECK_CIRCLE, color="green", size=50),
        ft.Text("SISTEMA ONLINE", size=30, weight="bold"),
        ft.Text("Vercel y Flet están comunicados.", color="white70")
    )

app = ft.app(target=main, export_asgi=True)
