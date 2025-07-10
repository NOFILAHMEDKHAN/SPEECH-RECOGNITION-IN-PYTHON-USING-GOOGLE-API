# 🎧 Speech Recognition & Audio Signal Visualization using Google API

## 📌 Course: CT-361 - Artificial Intelligence and Expert System  
**Lab No:** 06  
**Student:** Nofil Ahmed Khan  
**Roll No:** CT-22301  

---

## 🎯 Objective:
To understand how to use Python for **speech recognition** and **audio signal visualization** using the **Google Web Speech API** and **Scipy** tools.

---

## 📁 Lab Breakdown

### 🔹 Task 1: Visualize Waterfall Audio Signal
- Load `.wav` file (Audio_waterfall.wav)
- Plot amplitude vs time using Matplotlib
- Extract metadata (shape, data type, duration)

### 🔹 Task 2: Compare Other Audio Signals
- Repeat Task 1 for:
  - Audio_car.wav
  - Audio_carengine.wav
  - Audio_dog.wav
  - harvard.wav

### 🔹 Task 3: Recognize Spoken Word
- Use `speech_recognition` library with Google API
- Capture microphone input and transcribe speech

### 🔹 Task 4: Analyze Background Noise
- Adjust for ambient noise
- Display noise levels before and after
- Analyze recognition impact

---

## 🛠️ Technologies Used
- Python 3.x
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/)
- Matplotlib
- Scipy

---

## 🚀 How to Run

### Step 1: Install dependencies
```bash
pip install matplotlib scipy SpeechRecognition pyaudio
```

### Step 2: Run scripts
```bash
python task1_visualize_waterfall.py
python task2_compare_signals.py
python task3_microphone_recognition.py
python task4_background_noise_analysis.py
```

---

## 📷 Outputs
Each script will:
- Plot the waveform of audio files
- Print signal properties
- Transcribe audio (for Task 3 & 4)

---


## 📂 Repository Structure

```
📁 speech-recognition-lab06/
│
├── README.md
├── task1_visualize_waterfall.py
├── task2_compare_signals.py
├── task3_microphone_recognition.py
├── task4_background_noise_analysis.py
├── OUTPUTS
```

---

## 🤝 Contributions
Feel free to fork and enhance this lab with:
- Real-time visualization
- Spectrograms
- Language detection
