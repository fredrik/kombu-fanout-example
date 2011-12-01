#!/usr/bin/env python
import queues


def read_page(page, page_number):
    if not page or not page_number:
        print 'whoa, something is funny with this page. not reading it. no way.'
        print page, page_number
        return
    print "hoopla, I read page %d. it was quite long, but good." % page_number


def consume(queue):
    print 'just another consumer getting ready.'
    try:
        while True:
            message = queue.get()
            document = message.payload
            read_page(document.get('page'), document.get('page_number'))
            message.ack()
    except KeyboardInterrupt:
        print "\ncaught CTRL-C."


def argv_or_bust():
    """
    Read the first argument on the command line,
    or complain if there isn't one.
    """
    import sys
    if len(sys.argv) < 2:
        print "usage: %s <direction>" % sys.argv[0]
        print "where direction is one of 'left' and 'right'."
        sys.exit(1)
    return sys.argv[1]


if __name__ == '__main__':
    from kombu import BrokerConnection
    with BrokerConnection('localhost') as conn:
        consumer_choice = argv_or_bust()
        queue = conn.SimpleQueue(queues.page_queues.get(consumer_choice))
        consume(queue)
