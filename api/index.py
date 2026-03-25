import flet as ft
import flet_fastapi # Esta es la clave para Vercel
from supabase import create_client

# --- CONFIGURACIÓN ---
URL = "https://elikcpilcoujjcoftzmw.supabase.co"
KEY = "sb_publishable_cJD5fnogfagfdQ5NI-yzTQ_hv61swRw" 
supabase = create_client(URL, KEY)

def main(page: ft.Page):
    page.title = "Oficina Estrella"
    page.theme_mode = ft.ThemeMode.DARK
    
    chat_view = ft.Column(expand=True, scroll=ft.ScrollMode.ALWAYS)
    campo_texto = ft.TextField(hint_text="Escribí...", expand=True)

    def cargar_mensajes(e=None):
        try:
            res = supabase.table("mensajes").select("*").order("created_at", desc=True).limit(15).execute()
            chat_view.controls.clear()
            for m in reversed(res.data):
                es_op = "Op:" in m['remitente']
                chat_view.controls.append(
                    ft.Row([
                        ft.Container(
                            content=ft.Text(f"{m['remitente']}: {m['texto']}"),
                            bgcolor="#27ae60" if es_op else "#34495e",
                            padding=10, border_radius=10
                        )
                    ], alignment=ft.MainAxisAlignment.END if es_op else ft.MainAxisAlignment.START)
                )
            page.update()
        except: pass

    def enviar(e):
        if campo_texto.value:
            try:
                supabase.table("mensajes").insert({"texto": campo_texto.value, "remitente": "Op: Central"}).execute()
                campo_texto.value = ""
                cargar_mensajes()
            except: pass

    page.add(
        ft.Text("⭐ OFICINA ONLINE", size=20, weight="bold"),
        ft.Container(content=chat_view, expand=True, border=ft.border.all(1, "white24"), border_radius=10, padding=10),
        ft.Row([campo_texto, ft.IconButton(icon=ft.icons.SEND, on_click=enviar), ft.IconButton(icon=ft.icons.REFRESH, on_click=cargar_mensajes)])
    )
    cargar_mensajes()

# --- ESTO ES LO QUE ELIMINA EL ERROR 500 ---
import fastapi
app = fastapi.FastAPI()
app.mount("/", flet_fastapi.app(main))
