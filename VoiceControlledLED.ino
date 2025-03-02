#include <LiquidCrystal.h>  // Include the LiquidCrystal library

// Pins used for the LCD
LiquidCrystal lcd(12, 11, 5, 4, 3, 2); // RS, E, D4, D5, D6, D7

int ledPin = 13;  // Pin connected to the LED

void setup() {
  // Initialize the LCD and set the number of columns and rows:
  lcd.begin(16, 2);
  
  // Print a message to the LCD.
  lcd.print("LED Control");

  // Set the LED pin as an output
  pinMode(ledPin, OUTPUT);
  
  // Initialize serial communication:
  Serial.begin(9600);
}

void loop() {
  // Check if there's a message from Python (via Serial)
  if (Serial.available() > 0) {
    char command = Serial.read();  // Read the command from Python
    
    if (command == 'O') {  // If the command is 'O' (for "turn on")
      digitalWrite(ledPin, HIGH);  // Turn the LED on
      lcd.clear();
      lcd.print("Light is on!");
    } 
    else if (command == 'F') {  // If the command is 'F' (for "turn off")
      digitalWrite(ledPin, LOW);  // Turn the LED off
      lcd.clear();
      lcd.print("Light is off!");
    }
  }
}
