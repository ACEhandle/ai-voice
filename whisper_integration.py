import pyttsx3
import os
os.environ["PATH"] = r"C:\ffmpeg\bin;" + os.environ["PATH"]

import whisper
import sounddevice as sd
import numpy as np
import tempfile
import shutil


def record_audio(duration=5, sample_rate=16000):
    """Record audio from the microphone for a given duration (seconds)."""
    print(f"Recording for {duration} seconds...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
    sd.wait()
    return np.squeeze(audio)


def save_wav(audio, sample_rate=16000):
    """Save the recorded audio to a temporary WAV file and return the path."""
    import soundfile as sf
    temp_wav = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
    temp_wav.close()  # Ensure the file is closed before writing
    sf.write(temp_wav.name, audio, sample_rate)
    return temp_wav.name


def transcribe_audio(audio, sample_rate=16000, model_size="base"):
    """Transcribe audio using Whisper."""
    model = whisper.load_model(model_size)
    wav_path = save_wav(audio, sample_rate)
    print("Transcribing...")
    try:
        result = model.transcribe(wav_path, fp16=False, language='en')
    finally:
        os.remove(wav_path)  # Always remove the temp file, even if an error occurs
    return result["text"]


def main():
    duration = 5  # seconds
    sample_rate = 16000
    audio = record_audio(duration, sample_rate)
    text = transcribe_audio(audio, sample_rate)
    print("Transcription:", text)
    # Text-to-speech output
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    print("ffmpeg found at:", shutil.which("ffmpeg"))
    main()
