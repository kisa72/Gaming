from sungrowinverter import SungrowInverter
import asyncio
import time


def get_inverter_values(inverter_ip):
    client = SungrowInverter(inverter_ip)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        result = loop.run_until_complete(client.async_update())
    except:
        print("Failed to read")
        return "fail"
    #Get a list data returned from the inverter.
    return client.data


if __name__ == '__main__':
    inverter_ip = "192.168.0.135" # THIS CAN CHANGE

    while True:
        state = "good"
        try:
            inverter_values = get_inverter_values(inverter_ip)
            #print(inverter_values)
        except:
            print("failed")
            state = "bad"
        #print(inverter_values)

        # check read was successful
        if inverter_values != "fail" and state == "good":
            # filter to what I need
            export_power = inverter_values["export_power"] # Power going into the grid, 2176 = 2.176kW
            battery_level = inverter_values["battery_level"] 
            battery_power = inverter_values["battery_power"] # Power going into battery, 286.6 = 2.866kW
            #load_power = inverter_values["load_power"] 

            print("export_power: {0}".format(export_power))
            print("battery_level: {0}".format(battery_level))
            print("battery_power: {0}".format(battery_power))
            #print("load_power: {0}".format(load_power))

        time.sleep(300)
          
    
    
