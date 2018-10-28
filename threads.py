import threading


class Messenger(threading.Thread):
    def run(self):
        for _ in range(100):
            print(threading.current_thread().getName())


a = Messenger(name="Sending msg")
b = Messenger(name="Receiving msg")
a.start()
b.start()
