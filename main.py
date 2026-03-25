import customtkinter as ctk
import threading
from downloader import baixar_video

def iniciar_download():
    link = entrada.get()
    if not link:
        status.configure(text="Cole um link primeiro!", text_color="red")
        return

    # Mostra a barra e aumenta a janela
    barra.pack(pady=5)
    porcentagem_label.pack()
    app.geometry("500x260")

    botao.configure(state="disabled")
    status.configure(text="Baixando...", text_color="yellow")
    barra.set(0)
    porcentagem_label.configure(text="0%")

    def processo():
        baixar_video(
            link,
            lambda texto, cor: status.configure(text=texto, text_color=cor),
            atualizar_barra
        )
        botao.configure(state="normal")

    threading.Thread(target=processo).start()

def atualizar_barra(valor):
    barra.set(valor / 100)
    porcentagem_label.configure(text=f"{valor}%")

# Janela
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("YouTube Downloader")
app.geometry("500x200")  # tamanho inicial menor
app.resizable(False, False)

ctk.CTkLabel(app, text="YouTube Downloader", font=("Arial", 20, "bold")).pack(pady=15)

entrada = ctk.CTkEntry(app, width=400, placeholder_text="Cole o link do vídeo aqui...")
entrada.pack(pady=5)

botao = ctk.CTkButton(app, text="Baixar", command=iniciar_download, width=200)
botao.pack(pady=10)

status = ctk.CTkLabel(app, text="")
status.pack(pady=5)

# Barra escondida no início
barra = ctk.CTkProgressBar(app, width=400)
barra.set(0)

porcentagem_label = ctk.CTkLabel(app, text="0%", font=("Arial", 14, "bold"))

app.mainloop()