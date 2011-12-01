from kombu import Exchange
from kombu import Queue

word_exchange = Exchange('words', type='fanout')
producer_queue = Queue('pages', word_exchange)

page_queues = {
    'left':  Queue('pages_to_the_left_of_me', word_exchange),
    'right': Queue('pages_to_the_right', word_exchange),
}
