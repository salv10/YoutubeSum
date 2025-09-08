#utilizzo di whisper per trascrivere il testo di un video scaricato
import whisper, os

def transcribe_audio(audio_file):
    if not audio_file.endswith('.mp3'):
        audio_file += '.mp3'
    model = whisper.load_model("large")  # "tiny", "base", "small", ecc.
    result = model.transcribe(audio_file, language='it')  # specifica la lingua se necessario
    return result["text"]


# metodo per la creazione del file partendo dal testo trascritto
def create_txt_file(testo, path, nomeFile):
    nomeFile += '.txt'
    completePath = os.path.join(path, nomeFile)
    with open(completePath, 'w', encoding='utf-8') as f:
        f.write(testo)
    
    
    
