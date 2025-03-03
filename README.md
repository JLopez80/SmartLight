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
## Setting Up the Arduino

To set up the Arduino and connect the components correctly based on the code, follow these steps:

### 1. Connect the LCD Display:

For the 16x2 **LCD Display**, connect the pins to the following Arduino pins:

- **VSS** → **GND** on Arduino
- **VDD** → **5V** on Arduino
- **V0** → **10kΩ Potentiometer** (Adjust to set LCD contrast)
- **RS** → Pin **12** on Arduino
- **RW** → **GND** on Arduino
- **E** → Pin **11** on Arduino
- **D4** → Pin **5** on Arduino
- **D5** → Pin **4** on Arduino
- **D6** → Pin **3** on Arduino
- **D7** → Pin **2** on Arduino
- **A** → **5V** (Anode for LCD backlight)
- **K** → **GND** (Cathode for LCD backlight)

**Note**: The **potentiometer** is used to adjust the contrast of the LCD display. Connect the middle pin of the potentiometer to the **V0** pin on the LCD and the other two pins to **5V** and **GND**.

### 2. Connect the LED:

For controlling the **LED**, use the following connections:

- **Anode (long leg)** of the LED → Pin **13** on Arduino (Digital Pin 13)
- **Cathode (short leg)** of the LED → **GND** (Ground) on Arduino
- Place a **220Ω or 330Ω resistor** in series with the **anode** (positive leg) to limit the current flowing through the LED and prevent damage.

### 3. Wiring Overview:

- The **LCD** is connected to Arduino via **digital pins 2 to 12**.
- The **LED** is connected to **Pin 13**, with the **resistor** in series to protect the LED.
- The **LCD's VSS and RW** pins are connected to **GND**.
- The **LCD's VDD and V0** pins are connected to **5V** (power supply).

## Usage

Once the requirements are installed and the system is set up, you can control the LED with voice commands:

- "Turn on" / "Lights on"
- "Turn off" / "Lights out"

The status will also be displayed on the LCD screen.

## Potential Issues

- **Issue with PyAudio on Windows**: If you encounter errors installing PyAudio on Windows, you can use the precompiled wheel files from [Gohlke's repository](https://www.lfd.uci.edu/~gohlke/pythonlibs/).
- **Microphone not detected**: Ensure that the microphone is correctly configured and accessible by the Python script. You may need to select the correct input device in your system’s audio settings.
- **No recognizable command detected**: Whisper can be sensitive in terms of transfering audio to text. To avoid this issue, use simple commands if you choose to edit the code.

## Credits / Acknowledgements
- **Whisper** by OpenAI for the speech-to-text model.
- **PyAudio** for handling audio recording.
- **LiquidCrystal Library** for controlling the LCD screen on Arduino.
- **FFmpeg** for audio processing and conversion to a suitable format for Whisper.

## Demonstration of my Arduino  
This [video](https://youtu.be/0AbyosnZ-v8) demonstrates my Arduino and how the code works.


     




