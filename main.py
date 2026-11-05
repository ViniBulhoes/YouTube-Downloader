import customtkinter as ctk
import threading
from downloader import baixar_video

class YouTubeDownloaderApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da Janela
        self.title("YouTube Downloader")
        self.geometry("560x420")
        self.resizable(False, False)
        
        # Tema Escuro Global
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Título Principal
        self.lbl_titulo = ctk.CTkLabel(self, text="YouTube Downloader", font=("Segoe UI", 24, "bold"))
        self.lbl_titulo.pack(pady=(30, 15))

        # "Card" principal que vai agrupar os elementos para criar profundidade
        self.card = ctk.CTkFrame(self, corner_radius=15)
        self.card.pack(padx=40, pady=5, fill="both", expand=True)

        # Entrada de Link (Ocupando toda a largura do card)
        self.entrada = ctk.CTkEntry(
            self.card, 
            placeholder_text="Cole o link do vídeo aqui...", 
            height=45, 
            font=("Segoe UI", 14),
            border_width=1
        )
        self.entrada.pack(padx=25, pady=(25, 15), fill="x")

        # Frame interno para colocar os ComboBoxes alinhados e proporcionais
        self.frame_opcoes = ctk.CTkFrame(self.card, fg_color="transparent")
        self.frame_opcoes.pack(padx=25, pady=5, fill="x")
        
        self.frame_opcoes.columnconfigure(0, weight=1)
        self.frame_opcoes.columnconfigure(1, weight=1)

        self.combo_tipo = ctk.CTkComboBox(
            self.frame_opcoes, 
            values=["Vídeo com Áudio", "Apenas Áudio", "Apenas Vídeo"],
            height=35,
            font=("Segoe UI", 13)
        )
        self.combo_tipo.grid(row=0, column=0, padx=(0, 10), sticky="ew")
        self.combo_tipo.set("Vídeo com Áudio")

        self.combo_resolucao = ctk.CTkComboBox(
            self.frame_opcoes, 
            values=["2160", "1080", "720", "480", "360"],
            height=35,
            font=("Segoe UI", 13)
        )
        self.combo_resolucao.grid(row=0, column=1, padx=(10, 0), sticky="ew")
        self.combo_resolucao.set("1080")

        # Botão Baixar (Mais largo e destacado)
        self.botao = ctk.CTkButton(
            self.card, 
            text="Iniciar Download", 
            command=self.iniciar_download, 
            height=45, 
            font=("Segoe UI", 15, "bold"),
            corner_radius=8
        )
        self.botao.pack(padx=25, pady=(20, 15), fill="x")

        # Rodapé do Card (Status e Porcentagem lado a lado)
        self.frame_status = ctk.CTkFrame(self.card, fg_color="transparent")
        self.frame_status.pack(padx=25, pady=(0, 20), fill="x")

        self.status = ctk.CTkLabel(self.frame_status, text="Aguardando link...", text_color="gray", font=("Segoe UI", 12))
        self.status.pack(side="left")

        self.lbl_porcentagem = ctk.CTkLabel(self.frame_status, text="0%", text_color="gray", font=("Segoe UI", 13, "bold"))
        self.lbl_porcentagem.pack(side="right")

        # Barra de Progresso (Fora do card principal, na parte inferior da tela)
        self.barra = ctk.CTkProgressBar(self, height=8, corner_radius=5)
        self.barra.pack(padx=40, pady=(15, 30), fill="x")
        self.barra.set(0)

    def atualizar_status(self, texto, cor):
        self.after(0, lambda: self.status.configure(text=texto, text_color=cor))

    def atualizar_barra(self, valor):
        self.after(0, lambda: self.barra.set(valor / 100))
        # Muda a cor da porcentagem para branco durante o download para dar destaque
        self.after(0, lambda: self.lbl_porcentagem.configure(text=f"{valor}%", text_color="white"))

    def iniciar_download(self):
        link = self.entrada.get()
        if not link:
            self.atualizar_status("Cole um link primeiro!", "#ff6b6b") # Vermelho mais suave
            return

        mapa_tipos = {
            "Vídeo com Áudio": "video_com_audio",
            "Apenas Áudio": "apenas_audio",
            "Apenas Vídeo": "apenas_video"
        }
        tipo_escolhido = mapa_tipos[self.combo_tipo.get()]
        resolucao_escolhida = self.combo_resolucao.get()

        # Prepara a interface para o início
        self.botao.configure(state="disabled", text="Baixando...")
        self.atualizar_status("Iniciando conexão...", "#feca57") # Amarelo mais suave
        self.barra.set(0)
        self.lbl_porcentagem.configure(text="0%", text_color="gray")

        threading.Thread(
            target=self.processo_thread, 
            args=(link, tipo_escolhido, resolucao_escolhida),
            daemon=True
        ).start()

    def processo_thread(self, link, tipo, resolucao):
        baixar_video(
            link=link,
            callback_status=self.atualizar_status,
            callback_progresso=self.atualizar_barra,
            tipo=tipo,
            resolucao=resolucao
        )
        self.after(0, lambda: self.botao.configure(state="normal", text="Iniciar Download"))

if __name__ == "__main__":
    app = YouTubeDownloaderApp()
    app.mainloop()