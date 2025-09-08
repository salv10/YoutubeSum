from app import downloader, transcriber
import os, tempfile
if __name__ == "__main__":

    url = input("Inserisci il link del video: ")
    # Validazione dell'URL
    try:
        #ottengo il temp path del sistema dove andrò a scaricare il file 
        temp_path = tempfile.gettempdir()
        #print(f"Percorso temporaneo del sistema: {temp_path}") # testing

        # verifico che il link sia un link di youtube (anche se vuoto non viene accettato)
        if not url.startswith("https://www.youtube.com/watch") and not url.startswith("https://youtu.be/"):
            raise ValueError("L'URL fornito non è valido. Assicurati che sia un link di YouTube.")  
        
        # imposto il path di output alla cartella dei download
        nomeFile = downloader.get_video_title(url)
        #print(nomeFile) # testing
        if not nomeFile:
            raise ValueError("Impossibile recuperare il titolo del video. Controlla l'URL fornito.")
        
        print(nomeFile) # testing
        
        # imposto il path di output alla cartella dei download e il nome del file e faccio il download
        output_path = os.path.join(tempfile.gettempdir(), nomeFile)
        #print(output_path) # testing
        downloader.download_video(url, output_path)
        print("Download completato!") #testing

        # trascrivo il file scaricato
        testo = transcriber.transcribe_audio(output_path)
        
        # creazione del file dopo averlo trascritto
        transcriber.create_txt_file(testo, temp_path, nomeFile)
         

    except Exception as e:
        print(f"Si è verificato un errore durante il download: {e}")
