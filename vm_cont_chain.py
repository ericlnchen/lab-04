

import paho.mqtt.client as mqtt
import time


def on_connect(client, userdata, flags, rc):

    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("echen606/ping") # subscribe to ping
    
    #Add the custom callbacks by indicating the topic and the name of the callback handle
    client.message_callback_add("echen606/ping", on_message_from_ping)
    
def on_message(client, userdata, msg):
    print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))


#Custom message callback.
def on_message_from_ping(client, userdata, message): # message for ping
   ping_val = message.payload.decode()
   print("Custom callback  - PING: "+ ping_val)
   tine.sleep(1) # adding a delay so that numbers don't show up so fast
   
   client.publish("echen606/pong", f"{int(ping_val)+1}") # after receiving ping, increment it and publish it back
   print(f"Sent PONG")
   

if __name__ == '__main__':
    
    #create a client object
    client = mqtt.Client()
    #attach a default callback which we defined above for incoming mqtt messages
    client.on_message = on_message
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect
    
    # connects to the rpi broker
    client.connect(host="172.20.10.12", port=1883, keepalive=60)

    client.loop_forever()
    
    
    
    
    
