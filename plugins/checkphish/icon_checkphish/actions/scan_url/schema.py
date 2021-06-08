# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Scan a URL and retrieve scan results"


class Input:
    URL = "url"
    

class Output:
    SCAN_RESULTS = "scan_results"
    

class ScanUrlInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "url": {
      "type": "string",
      "title": "URL",
      "description": "URL you wish to scan and get results for",
      "order": 1
    }
  },
  "required": [
    "url"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ScanUrlOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "scan_results": {
      "$ref": "#/definitions/scan_url",
      "title": "Scan Results",
      "description": "Scan results",
      "order": 1
    }
  },
  "required": [
    "scan_results"
  ],
  "definitions": {
    "scan_url": {
      "type": "object",
      "title": "scan_url",
      "properties": {
        "brand": {
          "type": "string",
          "title": "Brand",
          "description": "Brand",
          "order": 6
        },
        "disposition": {
          "type": "string",
          "title": "Disposition",
          "description": "Disposition",
          "order": 5
        },
        "error": {
          "type": "boolean",
          "title": "Error",
          "description": "Error",
          "order": 10
        },
        "insights": {
          "type": "string",
          "title": "Insights",
          "description": "Insights URL",
          "order": 7
        },
        "job_id": {
          "type": "string",
          "title": "Job ID",
          "description": "Job ID",
          "order": 1
        },
        "resolved": {
          "type": "boolean",
          "title": "Resolved",
          "description": "Resolved",
          "order": 8
        },
        "screenshot_path": {
          "type": "string",
          "title": "Screenshot Path",
          "description": "Screenshot Path",
          "order": 9
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Status",
          "order": 2
        },
        "url": {
          "type": "string",
          "title": "URL",
          "description": "URL",
          "order": 3
        },
        "url_sha256": {
          "type": "string",
          "title": "URL SHA256",
          "description": "URL SHA256",
          "order": 4
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)