

import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    
    client.subscribe("echen606/pong") # subscribe to pong
    
    #Add the custom callbacks by indicating the topic and the name of the callback handle
    client.message_callback_add("echen606/pong", on_message_from_pong)
    
def on_message(client, userdata, msg):
    print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))

#Custom message callback.
def on_message_from_pong(client, userdata, message): # message for pong
   pong_val = message.payload.decode()
   print("Custom callback  - PONG: "+ pong_val)
   tine.sleep(1) # adding a delay so that numbers don't show up so fast
   
   client.publish("echen606/ping", f"{int(message.payload.decode())+1}") # after receiving pong, increment it and publish again
   print(f"Sent PING")


if __name__ == '__main__':
    
    #create a client object
    client = mqtt.Client()
    
    client.on_message = on_message
    
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect

    # connects to the rpi broker
    client.connect(host="172.20.10.12", port=1883, keepalive=60)
    
    # makes the first publish to start the sequence
    client.publish("echen606/ping", f"{ping}")
    print(f"Sent ping")
    time.sleep(1)
    
    client.loop_forever()

        
        
