import speech_recognition as sr

def recognize_speech():
    recording = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        
        # Capture noise level before recording speech
        noise_level_before = recording.energy_threshold
        
        recording.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
        
        # Capture noise level after noise reduction
        noise_level_after = recording.energy_threshold
        
        print("Please introduce yourself...")
        audio = recording.listen(source)

    try:
        recognized_text = recording.recognize_google(audio)
        print("\n Recognized Speech:\n" + recognized_text)

        # Analyzing background noise effect
        print("\n Background Noise Analysis:")
        print(f"Noise Level Before: {noise_level_before}")
        print(f"Noise Level After: {noise_level_after}")
        if noise_level_after > noise_level_before:
            print(" High background noise detected. Speech accuracy might be affected.")
        else:
            print(" Noise reduced successfully.")

    except sr.UnknownValueError:
        print("\n Could not understand the audio (high noise or unclear speech).")
    except sr.RequestError as e:
        print(f"\n API request failed: {e}")
    except Exception as e:
        print(f"\n Error: {e}")

# Run the function
recognize_speech()
