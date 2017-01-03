#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

import argparse
import paho.mqtt.publish
import grovepi

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('hostname', help=u'MQTT broker hostname')
    parser.add_argument('--topic', default='enviroment')
    return parser.parse_args()

def sensing():
    (temperature, humidity) = grovepi.dht(8, 0)
    return (temperature, humidity)

def publish(hostname, data):
    print data
    paho.mqtt.publish.multiple([data], hostname=hostname)

if __name__ == '__main__':
    args = parse_args()
    (temperature, humidity) = sensing()
    data = {
        'topic': args.topic,
        'payload':str({'temperature':temperature, 'humidity':humidity})
    }
    publish(args.hostname, data)
