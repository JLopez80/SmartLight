# SmartLight
This Arduino project uses Whisper for voice recognition to control an LED by using simple voice commands. The provided code recognizes commands like "turn on" and "lights on" to turn on the LED, while commands such as "turn off" and "lights out" will turn it off. An LCD screen will also display a message of the current state of the LED, such as "Light is on!" or "Light is off!"

## Hardware Requirements 
- **Arduino board** 
- **LED**
- **Resistor** (typically 220Ω or 330Ω)
- **16x2 LCD display** (for displaying the light status)
- **Potentiometer** (for adjusting the constrast of the LCD screen)
- **Microphone** (for capturing voice commands)
- **Jumper wires** 
- **Breadboard** 

## Software Requirements 
- **Python 3.x** (for running the speech recognition and controlling the Arduino)
  - Install Python from: [python.org](https://www.python.org/downloads/)
    
- **Arduino IDE** (for programming the Arduino)
  - Download from: [Arduino IDE](https://www.arduino.cc/en/software)
    
- **Arduino Libraries**:
  - **LiquidCrystal**: For controlling the LCD display connected to the Arduino.
- **Python Libraries**:
  - **Whisper**: For speech recognition (to transcribe voice commands).
     ```bash
       pip install openai-whisper
  - **PyAudio**: For recording audio.
     ```bash
       pip install pyaudio
  - **PySerial**: For serial communication between Python and Arduino.
     ```bash
       python3 -m pip install pyserial
- **FFmpeg** (required for audio processing in Whisper)
  - Windows: Download form [FFmpeg.org](https://ffmpeg.org/download.html) and follow installing instructions.
  - Linux (Ubuntu/Debian):
      ```bash
       sudo apt update
       sudo apt install ffmpeg
  - macOS (using Homebrew):
     ```bash
       brew install ffmpeg

    


     




