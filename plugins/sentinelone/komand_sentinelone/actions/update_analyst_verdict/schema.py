# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Updates an analyst verdict for each incident ID provided"


class Input:
    ANALYSTVERDICT = "analystVerdict"
    INCIDENTIDS = "incidentIds"
    TYPE = "type"


class Output:
    AFFECTED = "affected"


class UpdateAnalystVerdictInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "analystVerdict": {
      "type": "string",
      "title": "Analyst Verdict",
      "description": "Analyst verdict",
      "enum": [
        "true positive",
        "suspicious",
        "false positive",
        "undefined"
      ],
      "order": 2
    },
    "incidentIds": {
      "type": "array",
      "title": "Incident IDs",
      "description": "A list of alert or threat IDs on which we may update the analyst verdict",
      "items": {
        "type": "string"
      },
      "order": 1
    },
    "type": {
      "type": "string",
      "title": "Type",
      "description": "Type of incidents",
      "enum": [
        "threats",
        "alerts"
      ],
      "order": 3
    }
  },
  "required": [
    "analystVerdict",
    "incidentIds",
    "type"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UpdateAnalystVerdictOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "affected": {
      "type": "integer",
      "title": "Affected",
      "description": "Number of entities affected by the requested operation",
      "order": 1
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
