#qui verranno inseriti i metodi per il download dei video da youtube utilizzando la libreria yt_dlp
import yt_dlp

"""
    Scarica un video da YouTube utilizzando yt_dlp.
    
    Args:
        url (str): L'URL del video da scaricare.
        output_path (str): Il percorso dove salvare il video scaricato.
    """
def download_video(url, output_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio', #converte il video in audio usando ffmpeg
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("ok")

def get_video_title(url):
    ydl_opts = {
        'quiet': True,
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        return info_dict.get('title', 'video')
