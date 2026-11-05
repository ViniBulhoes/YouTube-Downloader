# 🎬 YouTube Downloader

## 📖 Sobre

Um aplicativo desktop moderno e minimalista para download de vídeos do YouTube. O projeto evoluiu de um teste acadêmico inicial em Análise e Desenvolvimento de Sistemas (ADS) para uma ferramenta robusta, com interface gráfica focada na experiência do usuário e suporte a downloads em alta resolução.

## 🚀 Novas Funcionalidades (Atualizado)

- **Múltiplas Resoluções:** Suporte nativo para baixar vídeos na qualidade máxima disponível (incluindo 1080p e 4K), superando o limite antigo de 720p.
- **Opções de Formato:** Permite escolher entre baixar o vídeo completo (Vídeo + Áudio), apenas a trilha sonora (Áudio em MP3) ou apenas a imagem.
- **Interface Moderna:** Totalmente reescrita utilizando `CustomTkinter` com layout em "Card", tema escuro (Dark Mode) e barra de progresso em tempo real.
- **Independente e Portátil:** Integração com `imageio-ffmpeg`, embutindo os binários necessários para conversão sem exigir que o usuário instale o FFmpeg manualmente no Windows.
- **Bypass de Restrições:** Atualizado com as versões mais recentes do `yt-dlp` para mitigar bloqueios de servidor (Erro 403).

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **[yt-dlp](https://github.com/yt-dlp/yt-dlp):** Motor principal de extração e download.
- **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter):** Construção da interface gráfica moderna e responsiva.
- **[imageio-ffmpeg](https://github.com/imageio/imageio-ffmpeg):** Processamento e junção de áudio/vídeo em segundo plano.

## 💻 Como Executar na Sua Máquina

1. Clone este repositório:
   ```bash
   git clone [https://github.com/ViniBulhoes/YouTube-Downloader.git](https://github.com/ViniBulhoes/YouTube-Downloader.git)

## ⚠️ Aviso Legal

Este projeto foi desenvolvido estritamente para fins de estudo e aprimoramento em programação orientada a objetos. Use com responsabilidade.