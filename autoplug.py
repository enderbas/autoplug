import broadlink
import time
import psutil
from datetime import datetime
import logging

broadlink.setup('wifi-ssid','wifi-password',3) #comment this line after first run
logging.basicConfig(filename='pc-plug.log', encoding='utf-8', level=logging.DEBUG)

devices = broadlink.discover()
logging.info(devices)

pc_charger_device = devices[0]
logging.info("Selected device is: " + str(pc_charger_device))
pc_charger_device.auth()

while 1:
    now = datetime.now()
    try:
        battery = psutil.sensors_battery()
        logging.info("Battery percent: " + str(battery.percent))
        state = pc_charger_device.check_power()
        if battery.percent <= 21 and state is False:
            logging.debug("Device power on. " + str(now))
            pc_charger_device.set_power(True)
        if battery.percent >= 85 and state is True:
            logging.debug("Device power off. " + str(now))
            pc_charger_device.set_power(False)
        state = pc_charger_device.check_power()
    except:
        logging.error("CRASH " + str(now))
        logging.error(broadlink.e)
    devState = "NO CHARGE"
    if state is True:
        devState = "CHARGE"
       
    logging.info("Device state is " + devState + " at " + str(now))
    
    time.sleep(60)