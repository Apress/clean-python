class Protocol:
    def __init__(self, host, port):
        self.host, self.port = host, port

    def __enter__(self):
        self._client = socket()
        self._client.connect((self.host, self.port))
        return self

    def __exit__(self, exception, value, traceback):
        self._client.close()

    def send(self, payload):
        <code for sending data>

    def receive(self):
        <code for receiving data>


with Protocol(host, port) as protocol:
     protocol.send(['get', signal])
     result = protocol.receive()
