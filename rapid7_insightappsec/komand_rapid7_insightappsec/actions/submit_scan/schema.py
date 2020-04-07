# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Submit a new scan"


class Input:
    SCAN_CONFIG_ID = "scan_config_id"
    

class Output:
    STATUS = "status"
    

class SubmitScanInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "scan_config_id": {
      "type": "string",
      "title": "Scan Config ID",
      "description": "UUID of the scan config to use",
      "order": 1
    }
  },
  "required": [
    "scan_config_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SubmitScanOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "status": {
      "type": "integer",
      "title": "Status",
      "description": "Status code of the request",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
