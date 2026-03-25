import flet as ft
from supabase import create_client
import time
import threading

# --- CONFIGURACIÓN ---
URL = "https://elikcpilcoujjcoftzmw.supabase.co"
KEY = "sb_publishable_cJD5fnogfagfdQ5NI-yzTQ_hv61swRw" # <--- PEGA TU CLAVE ACÁ
supabase = create_client(URL, KEY)

# --- TU EMAIL DE ADMINISTRADOR ---
MAIL_ADMIN = "hermannjose1@gmail.com" 

def main(page: ft.Page):
    page.title = "Oficina Estrella - Acceso Seguro"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 1000
    page.window_height = 700
    
    # Variables de sesión
    usuario_actual = None
    es_admin = False

    # Componentes de la interfaz
    chat_view = ft.Column(expand=True, scroll=ft.ScrollMode.ALWAYS)
    lista_pendientes = ft.Column(spacing=10)
    campo_texto = ft.TextField(hint_text="Escribí tu respuesta...", expand=True)

    # --- FUNCIÓN: ENVIAR MENSAJE ---
    def enviar_mensaje(e):
        if campo_texto.value != "":
            remitente = f"Op: {usuario_actual.email}"
            try:
                supabase.table("mensajes").insert({
                    "texto": campo_texto.value, 
                    "remitente": remitente
                }).execute()
                campo_texto.value = ""
                page.update()
            except: pass

    # --- FUNCIÓN: BORRADO (SOLO ADMIN) ---
    def borrar_historial(e):
        if es_admin:
            try:
                # Borra todos los mensajes (Solo Nivel Dios)
                supabase.table("mensajes").delete().neq("id", 0).execute()
            except: pass

    # --- PANTALLA DE CHAT ---
    def mostrar_oficina():
        page.clean()
        
        # --- BUSCÁ ESTA PARTE EN EL CÓDIGO ---
        btn_borrar = ft.ElevatedButton(
            "Limpieza Total (Nivel Dios)", 
            color="white", # Cambiado a blanco para que resalte
            bgcolor="red_700", # Fondo rojo para seguridad
            on_click=borrar_historial,
            visible=es_admin 
        )

        page.add(
            ft.Row([
                ft.Container(
                    content=ft.Column([
                        ft.Text("⭐ OFICINA ESTRELLA", size=20, weight="bold"),
                        ft.Text(f"Admin: {usuario_actual.email}", size=12, color="blue"),
                        ft.Divider(),
                        lista_pendientes,
                        # --- AGREGAMOS UN SEPARADOR AQUÍ ---
                        ft.Container(padding=10),
                        btn_borrar 
                    ]),
                    width=250, bgcolor="#1c1c1c", padding=20,
                ),
                ft.Container(
                    content=ft.Column([
                        chat_view,
                        ft.Row([
                            campo_texto,
                            ft.ElevatedButton("ENVIAR", on_click=enviar_mensaje)
                        ])
                    ]),
                    expand=True, padding=20
                )
            ], expand=True)
        )
        threading.Thread(target=refrescar_datos, daemon=True).start()

    # --- FUNCIÓN: LOGIN ---
    def login_click(e):
        nonlocal usuario_actual, es_admin
        try:
            res = supabase.auth.sign_in_with_password({
                "email": email_input.value, 
                "password": pass_input.value
            })
            usuario_actual = res.user
            es_admin = usuario_actual.email == MAIL_ADMIN
            mostrar_oficina()
        except:
            page.snack_bar = ft.SnackBar(ft.Text("Acceso denegado. Revisá tus datos."))
            page.snack_bar.open = True
            page.update()

    # --- PANTALLA INICIAL (LOGIN) ---
    email_input = ft.TextField(label="Email")
    pass_input = ft.TextField(label="Contraseña", password=True, can_reveal_password=True)
    
    page.add(
        ft.Column([
            ft.Text("INGRESO OPERADORES", size=30, weight="bold"),
            email_input,
            pass_input,
            ft.ElevatedButton("Entrar a la Oficina", on_click=login_click)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

    # --- REFRESCAR DATOS (IGUAL QUE ANTES) ---
    def refrescar_datos():
        while True:
            try:
                res = supabase.table("mensajes").select("*").order("created_at", desc=True).limit(30).execute()
                datos = res.data
                chat_view.controls.clear()
                for m in reversed(datos):
                    mio = "Op:" in m['remitente']
                    chat_view.controls.append(
                        ft.Row([
                            ft.Container(
                                content=ft.Text(f"{m['remitente']}: {m['texto']}"),
                                bgcolor="#34495e" if not mio else "#27ae60",
                                padding=10, border_radius=10, width=400
                            )
                        ], alignment=ft.MainAxisAlignment.END if mio else ft.MainAxisAlignment.START)
                    )
                lista_pendientes.controls.clear()
                if datos and "Op:" not in datos[0]['remitente']:
                    lista_pendientes.controls.append(ft.Container(ft.Text("⚠️ PENDIENTE", color="black"), bgcolor="yellow", padding=10))
                page.update()
            except: pass
            time.sleep(2)

ft.app(target=main)
