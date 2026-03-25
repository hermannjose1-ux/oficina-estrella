import flet as ft
from supabase import create_client

# --- CONFIGURACIÓN ---
URL = "https://elikcpilcoujjcoftzmw.supabase.co"
KEY = "sb_publishable_cJD5fnogfagfdQ5NI-yzTQ_hv61swRw" 
supabase = create_client(URL, KEY)
MAIL_ADMIN = "hermannjose1@gmail.com"

def main(page: ft.Page):
    page.title = "Oficina Estrella"
    page.theme_mode = ft.ThemeMode.DARK
    
    # Variables de estado
    state = {"user": None, "is_admin": False}

    chat_view = ft.Column(expand=True, scroll=ft.ScrollMode.ALWAYS)
    lista_pendientes = ft.Column(spacing=10)
    campo_texto = ft.TextField(hint_text="Escribí...", expand=True)

    def enviar_mensaje(e):
        if campo_texto.value != "" and state["user"]:
            try:
                supabase.table("mensajes").insert({
                    "texto": campo_texto.value, 
                    "remitente": f"Op: {state['user'].email}"
                }).execute()
                campo_texto.value = ""
                actualizar_ui()
            except: pass

    def actualizar_ui():
        try:
            res = supabase.table("mensajes").select("*").order("created_at", desc=True).limit(20).execute()
            datos = res.data
            
            chat_view.controls.clear()
            for m in reversed(datos):
                es_mio = "Op:" in m['remitente']
                chat_view.controls.append(
                    ft.Row([
                        ft.Container(
                            content=ft.Text(f"{m['remitente']}: {m['texto']}"),
                            bgcolor="#27ae60" if es_mio else "#34495e",
                            padding=10, border_radius=10
                        )
                    ], alignment=ft.MainAxisAlignment.END if es_mio else ft.MainAxisAlignment.START)
                )
            
            lista_pendientes.controls.clear()
            if datos and "Op:" not in datos[0]['remitente']:
                lista_pendientes.controls.append(ft.Container(ft.Text("⚠️ PENDIENTE", color="black"), bgcolor="yellow", padding=10))
            
            page.update()
        except: pass

    def login_click(e):
        try:
            res = supabase.auth.sign_in_with_password({"email": email.value, "password": pwd.value})
            state["user"] = res.user
            state["is_admin"] = res.user.email == MAIL_ADMIN
            
            page.clean()
            page.add(
                ft.Row([
                    ft.Container(content=ft.Column([ft.Text("⭐ OFICINA"), lista_pendientes]), width=200, bgcolor="#1c1c1c"),
                    ft.Container(content=ft.Column([chat_view, ft.Row([campo_texto, ft.ElevatedButton("ENVIAR", on_click=enviar_mensaje)])]), expand=True)
                ], expand=True)
            )
            actualizar_ui()
        except:
            page.snack_bar = ft.SnackBar(ft.Text("Error de login"))
            page.snack_bar.open = True
            page.update()

    email = ft.TextField(label="Email")
    pwd = ft.TextField(label="Password", password=True)
    page.add(ft.Column([ft.Text("LOGIN"), email, pwd, ft.ElevatedButton("Entrar", on_click=login_click)]))

# ESTO ES LO MÁS IMPORTANTE PARA VERCEL:
app = ft.app(target=main, export_asgi=True)
