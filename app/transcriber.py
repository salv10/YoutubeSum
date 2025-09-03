#utilizzo di whisper per trascrivere il testo di un video scaricato
import whisper

def transcribe_audio(audio_file):
    model = whisper.load_model("base")  # "tiny", "base", "small", ecc.
    result = model.transcribe(audio_file)
    return result["text"]
