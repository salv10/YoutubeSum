Youtube Summarize

An application in Python that automatically extracts text from a YouTube video and generates a concise summary using AI models.

- 📌 Planned features
- 📥 Automatic extraction of subtitles from a YouTube video
- 📝 Cleaning and formatting of the text
- 🤖 Summary generation via AI APIs (e.g., OpenAI, HuggingFace)
- 💾 Option to save the summary as .txt or .pdf
- 🌐 Simple web interface (planned for a future release)

-- Librerie/Pacchetti -- 
Per utilizzare la versione 'free' di whisper bisogna aggiungere il pacchetto eseguendo questo comando: pip install git+https://github.com/openai/whisper.git
Installare pytorch utilizzando questo comando pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

Verrà installato anche NumPy, la versione installata va in conflitto con PyTorch.
Dunque bisogna disinstallare con il comando pip uninstall numpy 
e installarla utilizzando il comando pip install "numpy<2" che installerà la versione 1.x.x 
compatibile con PyTorch

Inoltre è importante al fine di far funzionare il programma installare i pacchetti 
contenuti nel file requirements.txt
basta dare il comando pip install -r requirements.txt


