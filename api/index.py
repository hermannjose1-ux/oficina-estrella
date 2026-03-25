import flet as ft
import flet_fastapi
from supabase import create_client
import fastapi

# --- CONFIGURACIÓN ---
URL = "https://elikcpilcoujjcoftzmw.supabase.co"
KEY = "sb_publishable_cJD5fnogfagfdQ5NI-yzTQ_hv61swRw" 
# Agregamos una configuración para desactivar el 'realtime' que causa el error 500
supabase = create_client(URL, KEY)

def main(page: ft.Page):
    page.title = "Oficina Estrella"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.START
    
    chat_view = ft.Column(expand=True, scroll=ft.ScrollMode.ALWAYS)
    campo_texto = ft.TextField(hint_text="Escribí tu mensaje...", expand=True, on_submit=lambda e: enviar(e))

    def cargar_mensajes(e=None):
        try:
            # Pedimos los datos de forma simple, sin canales abiertos
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
            print(f"Error: {ex}")

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

    # Interfaz limpia
    page.add(
        ft.Text("⭐ OFICINA ESTRELLA", size=24, weight="bold"),
        ft.Container(
            content=chat_view, 
            expand=True, 
            border=ft.border.all(1, "white24"), 
            border_radius=10, 
            padding=10
        ),
        ft.Row([
            campo_texto, 
            ft.IconButton(icon=ft.icons.SEND, on_click=enviar),
            ft.IconButton(icon=ft.icons.REFRESH, on_click=cargar_mensajes, tooltip="Actualizar chat")
        ])
    )
    
    cargar_mensajes()

# --- LANZADOR FASTAPI ---
app = fastapi.FastAPI()
app.mount("/", flet_fastapi.app(main))
