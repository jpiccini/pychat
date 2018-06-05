import paho.mqtt.client as mqtt
import sys

if len(sys.argv) == 1:
    topic = "PyChat/Default/default"
else:
    topic = sys.argv[1]


def on_connect(client, userdata, flags, rc):
    client.subscribe(topic)
    print "\nNow reading messages from topic <%s>."%(topic)
    print

def on_message(client,userdata,msg):
    message,name,color = str(msg.payload).split('#!?#@@!')
    print 'Name:    ' + name
    print 'Message: ' + message
    print 'Color:   ' + color
    print
    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org",1883,60)

client.loop_forever()
