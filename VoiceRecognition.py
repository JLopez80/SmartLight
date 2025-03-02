import serial
import time
import whisper
import pyaudio
import wave

# Set up the serial port for communication with Arduino
ser = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)  # Wait for the serial connection to establish

# Initialize the Whisper model
model = whisper.load_model("base")

def record_audio():
    # Set up audio recording parameters
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 1
    rate = 16000
    frames_per_buffer = chunk
    
    p = pyaudio.PyAudio()

    print("Recording...")
    stream = p.open(format=sample_format, channels=channels, rate=rate,
                    input=True, frames_per_buffer=frames_per_buffer)
    
    frames = []
    
    # Record for 4 seconds (adjust as needed)
    for _ in range(0, int(rate / chunk * 4)):  
        data = stream.read(chunk)
        frames.append(data)
    
    print("Recording finished.")
    
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save the recording as a WAV file
    wf = wave.open("temp.wav", 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

def recognize_speech():
    # Record audio first
    record_audio()

    # Use the Whisper model to transcribe the audio
    result = model.transcribe("temp.wav")
    print("Transcription: ", result['text'])

    # Send the recognized command to Arduino. Write as many as you would like
    if "lights on" in result['text'].lower():
        ser.write(b'O')  # Send 'O' command to turn on the LED
        print("Command: Lights on")
    elif "lights out" in result['text'].lower():
        ser.write(b'F')  # Send 'F' command to turn off the LED
        print("Command: Lights out")
    elif "turn on" in result['text'].lower():
        ser.write(b'O')  # Send 'O' command to turn on the LED
        print("Command: Turn on")
    elif "turn off" in result['text'].lower():
        ser.write(b'F')  # Send 'F' command to turn off the LED
        print("Command: Turn off")    

    else:
        print("No recognizable command detected.")

def wait_for_command():
    while True:
        recognize_speech()  # Continuously listen for voice commands
        time.sleep(1)  # Wait before processing the next command

# Start listening for voice commands
wait_for_command()
