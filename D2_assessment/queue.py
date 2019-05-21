class Queue(object):
    '''
    Queue object
    '''
    def __init__(self):
        '''
        Creates a queue object
        '''
        self.queue = []

    def enqueue(self, dict_input):
        '''
        adds item to the queue
        '''
        for element in dict_input.values():
            self.queue.insert(0, element)
        return self.queue

    def alt_enqueue(self, dict_input):
        '''
        I found out that the enqueue() and dequeue() can be merged to this
        '''
        for element in dict_input.values():
            if element not in self.queue:
                self.queue.insert(0, element)
        return self.queue

    def dequeue(self, dict_input):
        '''
        compares the values in the queue and the input
        deletes the values in the input if already present in the queue
        '''
        dict_copy = dict_input.copy()

        for key, value in dict_input.items():
            if value in self.queue:
                del dict_copy[key]

        self.enqueue(dict_copy)
        return self.queue

dict1 = {'fruits':'apples', 'location':'namibia', 'age':'3 months', 'price':200}
dict2 = {'fruits':'apples', 'location':'rwanda', 'age':'4 months', 'price':200,\
          'specie': 'african special'}
queue1 = Queue()
queue2 = queue1.enqueue(dict1)
print(queue2)
queue3 = queue1.dequeue(dict2)
print(queue3)
print('*'*40)
print('alternate method')
print('*'*40)
queue_with_alt_enqueue = Queue()
queue_with_alt_enqueue1 = queue_with_alt_enqueue.alt_enqueue(dict1)
print(queue_with_alt_enqueue1)
queue_with_alt_enqueue2 = queue_with_alt_enqueue.alt_enqueue(dict2)
print(queue_with_alt_enqueue2)

