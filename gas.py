import RPi.GPIO as GPIO
import requests
from gpiozero import Servo, MCP3008, Buzzer
from time import sleep


#Setup
servo_pin = 17
buzzer_pin = 18
adc_channel = 3
exhaust_fan_pin = 23  # GPIO pin connected to the relay module controlling the exhaust fan

GPIO.setmode(GPIO.BCM)
servo = Servo(servo_pin)
buzzer = Buzzer(buzzer_pin)
adc = MCP3008(channel=adc_channel)
#GPIO.setup(exhaust_fan_pin, GPIO.OUT)  # Setup exhaust fan pin as output

def send_telegram_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=data)
    return response.json()  
bot_token = '7173020181:AAHS7_Q5t-xHYU1hGVA7HFMXbnHZ52U0elI'
chat_id = '1660814242'
message = 'GAS LEAKAGE DETECTED!'
def detect_gas_leakage():
    gas_level = adc.value
    print(adc.value)
    if gas_level > 0.004:  # Threshold for gas detection, adjust as necessary
        print("Gas leakage detected!")
        result = send_telegram_message(bot_token, chat_id, message)
        print(result)
        buzzer.on()
        #GPIO.output(exhaust_fan_pin, GPIO.HIGH) 
        sleep(1)  # Buzzer sounds for 1 second
        buzzer.off()
        servo.max()  # Simulate opening a door
        #sleep(5)  # Keep the door open for 5 seconds
        #servo.mid()  # Reset servo position (door closed)
        #GPIO.output(exhaust_fan_pin, GPIO.LOW)  # Turn off exhaust fan
if _name_ == "_main_":
    try:
        while True:
            detect_gas_leakage()
            sleep(1)  # Check every 10 seconds
    except KeyboardInterrupt:
        print("Program terminated")
        GPIO.cleanup()