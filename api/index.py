import flet as ft
import flet_fastapi
import fastapi
from supabase import create_client

# --- CONFIGURACIÓN ---
URL = "https://elikcpilcoujjcoftzmw.supabase.co"
KEY = "sb_publishable_cJD5fnogfagfdQ5NI-yzTQ_hv61swRw"

def main(page: ft.Page):
    page.title = "Oficina Estrella"
    page.theme_mode = ft.ThemeMode.DARK
    
    # UI Básica para que cargue instantáneo
    chat_view = ft.Column(expand=True, scroll=ft.ScrollMode.ALWAYS)
    
    def cargar_datos(e=None):
        try:
            # Creamos el cliente AQUÍ adentro, no afuera
            sb = create_client(URL, KEY)
            res = sb.table("mensajes").select("*").order("created_at", desc=True).limit(10).execute()
            
            chat_view.controls.clear()
            for m in reversed(res.data):
                chat_view.controls.append(ft.Text(f"{m['remitente']}: {m['texto']}"))
            page.update()
        except Exception as ex:
            chat_view.controls.append(ft.Text(f"Error: {ex}", color="red"))
            page.update()

    page.add(
        ft.Text("⭐ OFICINA ESTRELLA", size=20),
        ft.Container(content=chat_view, expand=True),
        ft.ElevatedButton("CARGAR MENSAJES", on_click=cargar_datos)
    )

# --- LANZADOR FASTAPI ---
app = fastapi.FastAPI()
app.mount("/", flet_fastapi.app(main))
