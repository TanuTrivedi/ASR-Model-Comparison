# wav2vec2_test.py
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torch
import librosa

# Load processor and model
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

# Load audio
audio, sr = librosa.load("data/sample_audio.wav", sr=16000)

# Process audio
inputs = processor(audio, return_tensors="pt", sampling_rate=sr)

# Get logits
with torch.no_grad():
    logits = model(inputs.input_values).logits

# Decode predicted ids
predicted_ids = torch.argmax(logits, dim=-1)
transcription = processor.decode(predicted_ids[0])

# Print transcription
print("Wav2Vec2 Transcription:")
print(transcription)

# Save transcription to results
with open("results/metrics.txt", "a") as f:
    f.write("Wav2Vec2 Transcription:\n")
    f.write(transcription + "\n\n")
