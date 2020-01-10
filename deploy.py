# Author: Zaher Abdul Azeez 
# Tagline: I come to my sel

# Date: "2020-01-10"

"""
Tars App
"""

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket
import json
import os
import datetime, time
from loggert import logger

class HealthCheck(tornado.web.RequestHandler):
	"""
	Handler for HealthCheck
	"""
	def get(self):
		"""
		Get Handler
		"""
		logger.info("je suis en bonne sante")
		self.write({
				"status": 42,
				"message": "towards infinity and beyond"
			})


class ChatPageHandler(tornado.web.RequestHandler):
	"""
	Home Chat Page Handler
	"""
	def get(self):
		"""
		Get handler
		"""
		self.render("./templates/index.html", curr_time=curr_time)

class WebSocketHandler(tornado.web.WebSocketHandler):
	"""
	Class that handles Web Socket Connections
	"""
	def open(self):
		"""
		ws on open handler
		"""
		logger.info("WS open handler")

	def on_message(self, message):
		"""
		what to do when a message is received
		"""
		logger.info("received message {}".format(message))
		self.write_message(u"Happy to hear from you")

	def on_close(self):
		"""
		What to do when a socket is closed
		"""
		logger.info("WebSocket closed")


settings = {
	"static_path" : os.path.join(os.path.dirname(__file__), "static"),
	"debug": False if env == "prod" else True
}

application = tornado.web.Application([
		()
	])



