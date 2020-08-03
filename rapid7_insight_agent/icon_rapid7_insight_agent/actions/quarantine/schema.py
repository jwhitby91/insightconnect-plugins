# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Quarantine or unquarantine on a device"


class Input:
    AGENT_ID = "agent_id"
    INTERVAL = "interval"
    QUARANTINE_STATE = "quarantine_state"
    

class Output:
    SUCCESS = "success"
    

class QuarantineInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agent_id": {
      "type": "string",
      "title": "Agent ID",
      "description": "The ID of the agent on the device to quarantine",
      "order": 1
    },
    "interval": {
      "type": "integer",
      "title": "Interval",
      "description": "Length of time in seconds to try to take action on a device. This is also called Advertisement Period",
      "default": 604800,
      "order": 3
    },
    "quarantine_state": {
      "type": "boolean",
      "title": "Quarantine State",
      "description": "Set to true to quarantine a host, set to false to unquarantine",
      "default": true,
      "order": 2
    }
  },
  "required": [
    "agent_id",
    "interval",
    "quarantine_state"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class QuarantineOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Was operation successful",
      "order": 1
    }
  },
  "required": [
    "success"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)