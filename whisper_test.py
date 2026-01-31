# whisper_test.py
import whisper

# Load the Whisper model
model = whisper.load_model("base")

# Transcribe audio
result = model.transcribe("data/sample_audio.wav")

# Print the transcription
print("Whisper Transcription:")
print(result["text"])

# Optionally, save the result to a file
with open("results/metrics.txt", "a") as f:
    f.write("Whisper Transcription:\n")
    f.write(result["text"] + "\n\n")
