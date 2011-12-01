#!/usr/bin/env python
import queues


def produce(conn):
    """
    'Produce' the pages of a book, one at a time.
    """
    pages = [
        "There was once a man.",
        "The man lived on an island, many nautical miles from any port.",
        "The life of the man was a simple one: he went fishing, he went swimming.",
        "Slowly the sun set that evening and the man smiled, just like he always did.",
        "'Tomorrow will be a good day for adventures!', he said softly to the dog that wasn't there."
    ]
    queue = conn.SimpleQueue(queues.page_queue)
    for page_number, page in enumerate(pages, 1):
        document = {
            'page_number': page_number,
            'page': page,
        }
        queue.put(document)

if __name__ == '__main__':
    from kombu import BrokerConnection
    with BrokerConnection('localhost') as conn:
        produce(conn)
