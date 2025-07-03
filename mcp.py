# mcp.py
import uuid

class MCPMessage:
    def __init__(self, sender, receiver, msg_type, payload):
        self.sender = sender
        self.receiver = receiver
        self.type = msg_type
        self.trace_id = str(uuid.uuid4())
        self.payload = payload

    def to_dict(self):
        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "type": self.type,
            "trace_id": self.trace_id,
            "payload": self.payload
        }