import tornado.ioloop
import tornado.web
import tornado.websocket
import subprocess
import os


import json
from time import sleep
import time
import argparse
import numpy as np
import cv2

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class SimpleWebSocket(tornado.websocket.WebSocketHandler):
    connections = set()

    def open(self):
        pass

    def check_origin(self, origin):
        pass

    def on_message(self, message):
        pass

    def on_close(self):
        self.connections.remove(self)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/websocket", SimpleWebSocket)
    ])

class Detector:
    def __init__(self):
        print(os.path.dirname(os.path.realpath(__file__)))
        subprocess.Popen(["/usr/local/bin/yarn", "watch"], cwd=os.path.dirname(os.path.realpath(__file__)))
        app = make_app()
        app.listen(7777)
        print("Start Server ...")
        tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    detector = Detector()