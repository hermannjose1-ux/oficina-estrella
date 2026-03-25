import flet as ft
from supabase import create_client

# Usamos una variable global para el cliente
URL = "https://elikcpilcoujjcoftzmw.supabase.co"
KEY = "TU_CLAVE_ANON_ACA"
supabase = create_client(URL, KEY)

def main(page: ft.Page):
    page.add(ft.Text("⭐ OFICINA ESTRELLA - PRUEBA DE CONEXIÓN"))
    try:
        # Prueba simple sin bucles ni cosas raras
        res = supabase.table("mensajes").select("*").limit(1).execute()
        page.add(ft.Text("✅ Conexión con Supabase: EXITOSA"))
    except Exception as e:
        page.add(ft.Text(f"❌ Error de conexión: {e}"))

# Esto es lo que Vercel busca por defecto
app = ft.app(target=main, export_asgi=True)
