# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Convert Markdown to HTML"


class Input:
    MARKDOWN = "markdown"
    MARKDOWN_STRING = "markdown_string"
    

class Output:
    HTML = "html"
    HTML_STRING = "html_string"
    

class MarkdownToHtmlInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "markdown": {
      "type": "string",
      "title": "Markdown Bytes",
      "displayType": "bytes",
      "description": "Markdown content represented in base64",
      "format": "bytes",
      "order": 1
    },
    "markdown_string": {
      "type": "string",
      "title": "Markdown String",
      "description": "Markdown content as a string",
      "order": 2
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class MarkdownToHtmlOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "html": {
      "type": "string",
      "title": "HTML",
      "displayType": "bytes",
      "description": "HTML data as bytes",
      "format": "bytes",
      "order": 1
    },
    "html_string": {
      "type": "string",
      "title": "HTML",
      "description": "HTML data",
      "order": 2
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)