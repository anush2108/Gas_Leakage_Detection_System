# Gas_Leakage_Detection_System

To set up a gas leakage detection system using a Raspberry Pi 4 that sends notifications to a mobile device, sounds a buzzer, and automatically opens a door (simulated here by activating a servo motor), follow the steps below. This setup integrates hardware component interfacing with software logic for real-time monitoring and response.

 Hardware Setup:

1. Components Required:
   - Raspberry Pi 4
   - MQ-2 Gas Sensor
   - MCP3008 ADC (for reading the analog sensor with Raspberry Pi’s digital GPIO)
   - Buzzer
   - SG90 Servo Motor (to simulate door opening)
   - Jumper Wires
   - Breadboard

2. Wiring Connections:
   - *MQ-2 Gas Sensor to MCP3008 ADC*:
     - VCC to 5V on Raspberry Pi
     - GND to GND
     - A0 to MCP3008 Channel 0 (CH0)
   - *MCP3008 to Raspberry Pi*:
     - VDD to 3.3V
     - VREF to 3.3V
     - AGND to GND
     - CLK to SCLK (GPIO 11)
     - DOUT to MISO (GPIO 9)
     - DIN to MOSI (GPIO 10)
     - CS/SHDN to CE0 (GPIO 8)
     - DGND to GND
   - *Buzzer*:
     - Positive to GPIO pin (e.g., GPIO 17)
     - Negative to GND
   - *SG90 Servo Motor*:
     - Red wire (VCC) to 5V
     - Brown wire (GND) to GND
     - Orange wire (Signal) to a GPIO pin (e.g., GPIO 18)

 Software Setup:

1. *SPI Interface*:
   - Enable SPI on the Raspberry Pi using raspi-config.

2. *Python Dependencies*:
   - Install necessary Python libraries with pip3 install RPi.GPIO adafruit-mcp3008 python-telegram-bot gpiozero.

3. *Telegram Bot*:
   - Create a Telegram bot via BotFather to get a bot token.
   - Obtain your chat ID by sending a message to your bot and visiting https://api.telegram.org/bot<YourBOTToken>/getUpdates.

