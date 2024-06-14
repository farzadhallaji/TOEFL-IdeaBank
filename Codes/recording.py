import sounddevice as sd
import numpy as np
import threading
import wave

# Settings
sample_rate = 16000  # Sample rate
channels = 1  # Mono
duration = 10  # Duration of recording in seconds (set long duration, we will stop via keyboard)

# Buffer to store the recorded data
recorded_frames = []

# Function to handle recording
def record_audio():
    global recorded_frames
    try:
        with sd.InputStream(samplerate=sample_rate, channels=channels, callback=callback):
            sd.sleep(duration * 1000)
    except Exception as e:
        print(f"An error occurred: {e}")

# Callback function to collect audio data
def callback(indata, frames, time, status):
    if status:
        print(status, flush=True)
    recorded_frames.append(indata.copy())

# Function to save the recorded audio to a WAV file
def save_wav_file(filename):
    global recorded_frames
    recorded_data = np.concatenate(recorded_frames, axis=0)
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(2)  # 2 bytes (16 bits) per sample
        wf.setframerate(sample_rate)
        wf.writeframes(recorded_data.tobytes())

# Thread function to wait for user input to stop recording
def stop_recording():
    input("Press Enter to stop recording...\n")
    sd.stop()

# Main function to start recording
def main():
    global recorded_frames
    recorded_frames = []  # Clear any previous recordings

    # Start recording in a separate thread
    recording_thread = threading.Thread(target=record_audio)
    recording_thread.start()

    # Start the stop_recording thread
    stop_thread = threading.Thread(target=stop_recording)
    stop_thread.start()

    # Wait for both threads to complete
    recording_thread.join()
    stop_thread.join()

    # Save the recorded audio
    save_wav_file("output.wav")
    print("Recording saved as output.wav")

if __name__ == "__main__":
    main()
 
