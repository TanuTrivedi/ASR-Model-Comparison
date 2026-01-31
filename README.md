ASR Benchmarking for Noisy Customer Support Environments
📌 Project Overview
This project involves a comparative study of State-of-the-Art (SOTA) Speech-to-Text models to identify the best candidate for a customer support AI assistant. The primary focus is evaluating model performance in noisy environments and across multiple accents.

🎯 Objectives
Research recent ASR models, including open-source and API-based options.

Select and benchmark 3 specific models.

Evaluate performance on a small dataset (e.g., LibriSpeech or Common Voice).

Analyze architecture, training approach, and deployment feasibility.

Provide a data-driven production recommendation.

🛠️ Research & Candidate Models
As per the research requirements, the following models were considered for benchmarking:


OpenAI Whisper (base/small): A robust multitask model.


Faster-Whisper: An optimized version for improved inference speed.


Distil-Whisper: A compressed version for lower resource usage.


Wav2Vec2: A self-supervised learning framework.


NeMo ASR: NVIDIA’s toolkit for conversational AI.

📊 Evaluation Criteria
Each model is evaluated against the following technical metrics:


Accuracy: Measured via Word Error Rate (WER).


Latency: Measured by total inference time.


Resource Usage: Approximate memory (VRAM/RAM) consumption.


Operational Effort: Setup complexity and ease of deployment.


Robustness: Suitability for noisy real-world audio.

Selected Model: Based on the benchmark results.


Fine-tuning: A strategy to improve performance on domain-specific terminology.


Optimization: Ideas for high-speed production environments.


Architecture: A suggested production-grade deployment layout.
