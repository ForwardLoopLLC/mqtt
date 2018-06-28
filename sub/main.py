#!/usr/bin/python

# this is based on an example in the Paho MQTT repository:

# Copyright (c) 2013 Roger Light <roger@atchoo.org>
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Distribution License v1.0
# which accompanies this distribution.
#
# The Eclipse Distribution License is available at
#   http://www.eclipse.org/org/documents/edl-v10.php.
#
# Contributors:
#    Roger Light - initial implementation

import paho.mqtt.client as mqtt

from os import environ

print(environ)

class MQTTClient(mqtt.Client):

    def on_connect(self, mqttc, obj, flags, rc):
        print("rc: "+str(rc))

    def on_message(self, mqttc, obj, msg):
        print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        print("Subscribed: "+str(mid)+" "+str(granted_qos))

    def on_log(self, mqttc, obj, level, string):
        print(string)

    def run(self):
        rc = 0
        while(True):
            self.connect("0.0.0.0", int(environ['MQTT_PORT']), 60)
            self.subscribe("test/test", 0)

            rc = 0
            while rc == 0:
                rc = self.loop()
        return rc

if __name__ == '__main__':
    mqtt_client = MQTTClient()
    mqtt_client.run()
