# faster_whisper_test.py
from faster_whisper import WhisperModel

# Load Faster-Whisper model
model = WhisperModel("base")  # Can also use "small" or "medium"

# Transcribe audio
segments, info = model.transcribe("data/ASR-Model-Comparisondatasample_audio.wav.m4a")

# Print transcription
print("Faster-Whisper Transcription:")
full_text = ""
for segment in segments:
    print(segment.text)
    full_text += segment.text + " "

# Save transcription to results
with open("results/metrics.txt", "a") as f:
    f.write("Faster-Whisper Transcription:\n")
    f.write(full_text + "\n\n")
