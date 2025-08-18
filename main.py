from app import downloader

if __name__ == "__main__":

    url = input("Inserisci il link del video: ")
    # Validazione dell'URL
    try:
        # verifico che il link sia un link di youtube (anche se vuoto non viene accettato)
        if not url.startswith("https://www.youtube.com/watch") and not url.startswith("https://youtu.be/"):
            raise ValueError("L'URL fornito non è valido. Assicurati che sia un link di YouTube.")  
        # imposto il path di output alla cartella dei download
        output_path = "~/Downloads/video.mp4"
        downloader.download_video(url, output_path)
    except Exception as e:
        print(f"Si è verificato un errore durante il download: {e}")