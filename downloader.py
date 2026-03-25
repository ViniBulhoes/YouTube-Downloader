import yt_dlp
import re

def baixar_video(link, callback_status, callback_progresso):
    def hook(d):
        if d['status'] == 'downloading':
            porcentagem = d.get('downloaded_bytes', 0)
            total = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
            if total > 0:
                valor = (porcentagem / total) * 100
                callback_progresso(round(valor, 1))
        elif d['status'] == 'finished':
            callback_progresso(100)

    try:
        opcoes = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s',
            'progress_hooks': [hook],
        }
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            ydl.download([link])
        callback_status("Baixado com sucesso!", "green")
    except Exception as e:
        callback_status(f"Erro: {e}", "red")