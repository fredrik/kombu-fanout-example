from kombu import Exchange
from kombu import Queue

word_exchange = Exchange('words', type='fanout')
page_queue = Queue('pages', word_exchange)
