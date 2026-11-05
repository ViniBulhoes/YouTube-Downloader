import yt_dlp
import imageio_ffmpeg

def baixar_video(link, callback_status, callback_progresso, tipo='video_com_audio', resolucao='1080'):
    def hook(d):
        if d['status'] == 'downloading':
            porcentagem = d.get('downloaded_bytes', 0)
            total = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
            if total > 0:
                valor = (porcentagem / total) * 100
                callback_progresso(round(valor, 1))
        elif d['status'] == 'finished':
            # Quando o download termina, o FFmpeg pode demorar uns segundos juntando ou convertendo
            callback_status("Processando arquivo...", "orange")

    try:
        # Pega o executável do FFmpeg embutido via pip
        caminho_ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
        
        opcoes = {
            'outtmpl': '%(title)s.%(ext)s',
            'progress_hooks': [hook],
            'ffmpeg_location': caminho_ffmpeg, # Aponta o FFmpeg para o yt-dlp
        }

        # Configura as opções baseadas no que o usuário escolheu
        if tipo == 'apenas_audio':
            opcoes['format'] = 'bestaudio/best'
            opcoes['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192', # Qualidade do MP3
            }]
            
        elif tipo == 'apenas_video':
            # Baixa apenas a imagem, sem trilha de áudio
            opcoes['format'] = f'bv*[height<={resolucao}]/bestvideo'
            
        else: # video_com_audio
            # Baixa o melhor vídeo até o limite escolhido + o melhor áudio e junta os dois
            opcoes['format'] = f'bv*[height<={resolucao}]+ba/b'
            opcoes['merge_output_format'] = 'mp4'

        with yt_dlp.YoutubeDL(opcoes) as ydl:
            ydl.download([link])
            
        callback_progresso(100)
        callback_status("Baixado com sucesso!", "green")
        
    except Exception as e:
        callback_status(f"Erro: {e}", "red")