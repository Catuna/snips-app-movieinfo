import logging
import logging.config
import json
import time
import paho.mqtt.client as mqtt

from movie_trivia.app import MovieTriviaApp


LOGGER_CONF = 'logger_conf.json'
APP_LOGGER = 'MovieTriviaApp'

MQTT_IP_ADDR = "raspberrypi.local"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

skill = None


def onMessage(client, userData, message):
    logger = logging.getLogger(APP_LOGGER)
    payload = json.loads(message.payload)

    try:
        skill.handleIntent(payload['sessionId'],
                           message.topic,
                           payload['slots'])
    except Exception:
        logger.exception('Failed to answer query')


def onConnect(client, userData, flags, rc):
    logger = logging.getLogger(APP_LOGGER)
    logger.info('Connected to MQTT broker')

    try:
        pass
    except Exception:
        logger.exception('Failed subscribing to topic')


if __name__ == '__main__':
    logger = None
    try:
        with open(LOGGER_CONF, 'rt') as loggerConfFile:
            loggerConf = json.loads(loggerConfFile.read())
            logging.config.dictConfig(loggerConf)
            logger = logging.getLogger(APP_LOGGER)
    except Exception:
        logging.exception('Failed to load configuration from file')
        exit(-1)

    logger.info('Connecting to MQTT broker')
    try:
        mqttCli = mqtt.Client()
        mqttCli.on_connect = onConnect
        mqttCli.on_message = onMessage
        mqttCli.connect(MQTT_IP_ADDR, MQTT_PORT)

        mqttCli.loop_start()
    except Exception:
        logger.exception('Failed to initialize MQTT connection')
        exit(-1)

    logger.info('Movie Trivia app initializing')
    try:
        app = MovieTriviaApp(mqttCli)
    except Exception:
        logger.exception('Failed to initialize app')
        exit(-1)

    shouldStop = False
    try:
        logger.info('Entering infinite loop on main thread')
        while not shouldStop:
            time.sleep(0.1)
    except KeyboardInterrupt:
        mqttCli.loop_stop()
        mqttCli.disconnect()
        shouldStop = True
