import flet as ft
from supabase import create_client
import os

# --- CONFIGURACIÓN ---
URL = "https://elikcpilcoujjcoftzmw.supabase.co"
KEY = "sb_publishable_cJD5fnogfagfdQ5NI-yzTQ_hv61swRw" 
supabase = create_client(URL, KEY)

def main(page: ft.Page):
    page.title = "Oficina Estrella"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    
    # Referencias de UI
    chat_view = ft.Column(expand=True, scroll=ft.ScrollMode.ALWAYS)
    campo_texto = ft.TextField(hint_text="Escribí tu respuesta...", expand=True)
    
    def cargar_mensajes(e=None):
        try:
            res = supabase.table("mensajes").select("*").order("created_at", desc=True).limit(20).execute()
            chat_view.controls.clear()
            for m in reversed(res.data):
                es_op = "Op:" in m['remitente']
                chat_view.controls.append(
                    ft.Row([
                        ft.Container(
                            content=ft.Text(f"{m['remitente']}: {m['texto']}", color="white"),
                            bgcolor="#27ae60" if es_op else "#34495e",
                            padding=10, border_radius=10,
                        )
                    ], alignment=ft.MainAxisAlignment.END if es_op else ft.MainAxisAlignment.START)
                )
            page.update()
        except Exception as ex:
            print(f"Error cargando: {ex}")

    def enviar(e):
        if campo_texto.value:
            try:
                supabase.table("mensajes").insert({
                    "texto": campo_texto.value,
                    "remitente": "Op: Central"
                }).execute()
                campo_texto.value = ""
                cargar_mensajes()
            except: pass

    # Botón de refresco manual (más estable para web)
    btn_refresh = ft.IconButton(icon=ft.icons.REFRESH, on_click=cargar_mensajes)

    page.add(
        ft.Text("⭐ OFICINA ESTRELLA ONLINE", size=20, weight="bold"),
        ft.Container(content=chat_view, expand=True, border=ft.border.all(1, "white24"), border_radius=10, padding=10),
        ft.Row([campo_texto, ft.ElevatedButton("ENVIAR", on_click=enviar), btn_refresh])
    )
    
    cargar_mensajes()

# LA CLAVE PARA VERCEL
app = ft.app(target=main, export_asgi=True)
