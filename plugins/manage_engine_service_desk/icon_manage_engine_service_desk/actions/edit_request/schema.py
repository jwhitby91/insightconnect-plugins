# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Update the given request. At least one parameter other than Request ID is required. In every parameter containing `ID` and `Name` fields please provide only one or the other"


class Input:
    ASSETS = "assets"
    CATEGORY = "category"
    DESCRIPTION = "description"
    EMAIL_IDS_TO_NOTIFY = "email_ids_to_notify"
    GROUP = "group"
    IMPACT = "impact"
    IS_FCR = "is_fcr"
    ITEM = "item"
    LEVEL = "level"
    MODE = "mode"
    PRIORITY = "priority"
    REQUEST_ID = "request_id"
    REQUEST_TYPE = "request_type"
    REQUESTER = "requester"
    SERVICE_CATEGORY = "service_category"
    SITE = "site"
    STATUS = "status"
    SUBCATEGORY = "subcategory"
    SUBJECT = "subject"
    TECHNICIAN = "technician"
    URGENCY = "urgency"
    

class Output:
    REQUEST_ID = "request_id"
    STATUS = "status"
    STATUS_CODE = "status_code"
    

class EditRequestInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "assets": {
      "type": "array",
      "title": "Assets",
      "description": "Array of asset objects associated with this request",
      "items": {
        "$ref": "#/definitions/asset"
      },
      "order": 4
    },
    "category": {
      "$ref": "#/definitions/category",
      "title": "Category",
      "description": "Category to which this request belongs",
      "order": 19
    },
    "description": {
      "type": "string",
      "title": "Description",
      "description": "Description of this request",
      "order": 3
    },
    "email_ids_to_notify": {
      "type": "array",
      "title": "Email IDs to Notify",
      "description": "Array of Email ids, which needs to be notified about the happenings of this request",
      "items": {
        "type": "string"
      },
      "order": 5
    },
    "group": {
      "$ref": "#/definitions/group",
      "title": "Group",
      "description": "The group to which the request belongs",
      "order": 17
    },
    "impact": {
      "$ref": "#/definitions/impact",
      "title": "Impact",
      "description": "Impact of this request",
      "order": 9
    },
    "is_fcr": {
      "type": "boolean",
      "title": "Is Fcr",
      "description": "Boolean value indicating if the request has been marked as First Call Resolution",
      "order": 6
    },
    "item": {
      "$ref": "#/definitions/item",
      "title": "Item",
      "description": "Item of this request",
      "order": 21
    },
    "level": {
      "$ref": "#/definitions/level",
      "title": "Level",
      "description": "Level of the request",
      "order": 12
    },
    "mode": {
      "$ref": "#/definitions/mode",
      "title": "Mode",
      "description": "The mode in which this request is created",
      "order": 11
    },
    "priority": {
      "$ref": "#/definitions/priority",
      "title": "Priority",
      "description": "Priority of the request",
      "order": 14
    },
    "request_id": {
      "type": "integer",
      "title": "Request ID",
      "description": "The ID of a request to edit",
      "order": 1
    },
    "request_type": {
      "$ref": "#/definitions/request_type",
      "title": "Request Type",
      "description": "Type of this request",
      "order": 8
    },
    "requester": {
      "$ref": "#/definitions/user_input",
      "title": "Requester",
      "description": "The requester of the request",
      "order": 7
    },
    "service_category": {
      "$ref": "#/definitions/service_category",
      "title": "Service Category",
      "description": "Service category to which this request belongs",
      "order": 15
    },
    "site": {
      "$ref": "#/definitions/site",
      "title": "Site",
      "description": "Denotes the site to which this request belongs",
      "order": 16
    },
    "status": {
      "$ref": "#/definitions/status",
      "title": "Status",
      "description": "Indicates the current status of this request",
      "order": 10
    },
    "subcategory": {
      "$ref": "#/definitions/subcategory",
      "title": "Subcategory",
      "description": "Subcategory to which this request belongs",
      "order": 20
    },
    "subject": {
      "type": "string",
      "title": "Subject",
      "description": "Subject of this request",
      "order": 2
    },
    "technician": {
      "$ref": "#/definitions/technician",
      "title": "Technician",
      "description": "The technician that was assigned to the request",
      "order": 18
    },
    "urgency": {
      "$ref": "#/definitions/urgency",
      "title": "Urgency",
      "description": "Urgency of the request",
      "order": 13
    }
  },
  "required": [
    "request_id"
  ],
  "definitions": {
    "asset": {
      "type": "object",
      "title": "asset",
      "properties": {
        "barcode": {
          "type": "string",
          "title": "Barcode",
          "description": "Barcode of the asset",
          "order": 3
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Id of the asset",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the asset",
          "order": 2
        }
      }
    },
    "category": {
      "type": "object",
      "title": "category",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID of the category",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the category",
          "order": 2
        }
      }
    },
    "group": {
      "type": "object",
      "title": "group",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Group's id",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Group's name",
          "order": 2
        }
      }
    },
    "impact": {
      "type": "object",
      "title": "impact",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID of the impact",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name impact",
          "order": 2
        }
      }
    },
    "item": {
      "type": "object",
      "title": "item",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID of the item",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the item",
          "order": 2
        }
      }
    },
    "level": {
      "type": "object",
      "title": "level",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Id of the level",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the level",
          "order": 2
        }
      }
    },
    "mode": {
      "type": "object",
      "title": "mode",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Id of the mode",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the mode",
          "order": 2
        }
      }
    },
    "priority": {
      "type": "object",
      "title": "priority",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID of the priority",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the priority",
          "order": 2
        }
      }
    },
    "request_type": {
      "type": "object",
      "title": "request_type",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID of the request type",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the request type",
          "order": 2
        }
      }
    },
    "service_category": {
      "type": "object",
      "title": "service_category",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID of the service category",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the service category",
          "order": 2
        }
      }
    },
    "site": {
      "type": "object",
      "title": "site",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Site's id",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Site's name",
          "order": 2
        }
      }
    },
    "status": {
      "type": "object",
      "title": "status",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID of the current status",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the current status",
          "order": 2
        }
      }
    },
    "subcategory": {
      "type": "object",
      "title": "subcategory",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID of the subcategory",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the subcategory",
          "order": 2
        }
      }
    },
    "technician": {
      "type": "object",
      "title": "technician",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Technician ID",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Technician Name",
          "order": 2
        }
      }
    },
    "urgency": {
      "type": "object",
      "title": "urgency",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Id of the urgency",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the urgency",
          "order": 2
        }
      }
    },
    "user_input": {
      "type": "object",
      "title": "user_input",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "User ID",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "User name",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class EditRequestOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "request_id": {
      "type": "integer",
      "title": "Request ID",
      "description": "The id of edited request",
      "order": 1
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "Status of the request",
      "order": 2
    },
    "status_code": {
      "type": "integer",
      "title": "Status Code",
      "description": "Status code of the request",
      "order": 3
    }
  },
  "required": [
    "status"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
