# ai-voice

## Project Goals
- Provide a modular, Python-based voice-to-text and text-to-speech (TTS) integration for use in other projects.
- Use OpenAI Whisper for accurate speech-to-text transcription.
- Use pyttsx3 for local, offline text-to-speech output.
- Enable easy integration into other Python projects or as a standalone tool.

## Current Functionality
- **Record audio** from the microphone using `sounddevice`.
- **Transcribe audio** to text using OpenAI Whisper (supports English by default).
- **Output transcription** as both printed text and spoken audio using `pyttsx3`.
- **Handles ffmpeg dependency** for Whisper audio processing.
- Modular code structure for future integration with AI models or other applications.

## Requirements
- Python 3.10 or 3.11 (not 3.12)
- Windows 10 or later
- [ffmpeg](https://ffmpeg.org/download.html) installed and available in your PATH (or set in the script)
- Microphone for audio input

### Python Dependencies (see `requirements.txt`)
- whisper (openai-whisper)
- torch
- sounddevice
- numpy
- soundfile
- pyttsx3

## Deployment / Packaging as Standalone
To package this project as a standalone executable (e.g., for Windows):

1. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

2. **Install PyInstaller:**
   ```powershell
   pip install pyinstaller
   ```

3. **Build the executable:**
   ```powershell
   pyinstaller --onefile --add-data "C:/ffmpeg/bin;ffmpeg/bin" whisper_integration.py
   ```
   - Adjust the `--add-data` path as needed for your ffmpeg location.
   - The output will be in the `dist` folder.

4. **Distribute the `dist/whisper_integration.exe`** file along with instructions for installing ffmpeg if not bundled.

**Note:** For best results, ensure ffmpeg is available on the target system's PATH, or modify the script to set the PATH at runtime as shown in the code.

## Usage
Run the script in your virtual environment:
```powershell
python whisper_integration.py
```
Follow the prompts to record audio, transcribe, and hear the spoken result.

## Extending / Integrating
- Import the functions from `whisper_integration.py` into other Python projects.
- Modify the main function or add new modules to connect to AI models, chatbots, or other systems.

---
For more details or troubleshooting, see comments in the code or ask for help!
# ai-voice
Voice to AI and back. for integration into other utilities.
