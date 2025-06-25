class MCPBase:
    """
    Base class for Model Context Protocol (MCP) connections.
    Apps can inherit from this class to implement MCP-based communication.
    """

    def __init__(self, host: str, port: int, **kwargs):
        self.host = host
        self.port = port
        self.connected = False
        self.connection = None
        self.options = kwargs

    def connect(self):
        """
        Establish a connection to the MCP server.
        Override this method with actual connection logic.
        """
        raise NotImplementedError("connect() must be implemented by subclasses.")

    def disconnect(self):
        """
        Close the connection to the MCP server.
        Override this method with actual disconnection logic.
        """
        raise NotImplementedError("disconnect() must be implemented by subclasses.")

    def send(self, message: str):
        """
        Send a message to the MCP server.
        Override this method with actual send logic.
        """
        raise NotImplementedError("send() must be implemented by subclasses.")

    def receive(self) -> str:
        """
        Receive a message from the MCP server.
        Override this method with actual receive logic.
        """
        raise NotImplementedError("receive() must be implemented by subclasses.")

    def handle_message(self, message: str):
        """
        Handle an incoming message.
        Apps should override this to implement custom message handling.
        """
        raise NotImplementedError("handle_message() must be implemented by subclasses.")

    def run(self):
        """
        Main loop for receiving and handling messages.
        """
        self.connect()
        self.connected = True
        try:
            while self.connected:
                message = self.receive()
                if message:
                    self.handle_message(message)
        finally:
            self.disconnect()
            self.connected = False