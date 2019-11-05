# Advanced Regex

## About

Perform regex operations on a string using Python regex.

## Actions

### Data Extraction

This action is used to extract data via regex from a string.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ascii|boolean|False|False|Make \w \W \b \B follow ASCII rules|None|
|dotall|boolean|False|False|Make . match newline|None|
|ignorecase|boolean|False|False|Make regex non-case sensitive|None|
|in_regex|string|None|True|Regex to use for data extraction|None|
|in_string|string|None|True|Input string|None|
|multiline|boolean|False|False|Make begin/end consider each line|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|matches|[][]string|True|An array of string arrays matching the output of Python re.findall()|

Example output:

```
{
  "matches": [
    "Lorem",
    "lorem"
  ]
}
```

### Search and Replace

This action is used to regex search and replace string.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ascii|boolean|False|False|Make \w \W \b \B follow ASCII rules|None|
|dotall|boolean|False|False|Make . match newline|None|
|ignorecase|boolean|False|False|Make regex non-case sensitive|None|
|in_regex|string|None|True|Regex to match|None|
|in_string|string|None|True|Input string|None|
|max_replace|integer|0|False|Max occurences to replace - if zero all will be replaced|None|
|multiline|boolean|False|False|Make begin/end consider each line|None|
|replace_string|string|None|True|The string to replace matches with|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|string|True|The result of the replace operation|

Example output:

```
{
  "result": "REPLACED ipsum dolor sit amet, consectetur \nadipiscing elit. Aliquam sapien ex, REPLACEDs odales sed luctus ac, dapibus quis augue. Vivamus in cursus libero. Donec vehicula turpis eu ante viverra, lacinia."
}
```

### Split by Regex

This action is used to split a string into array using regex.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ascii|boolean|False|False|Make \w \W \b \B follow ASCII rules|None|
|dotall|boolean|False|False|Make . match newline|None|
|ignorecase|boolean|False|False|Make regex non-case sensitive|None|
|in_regex|string|None|True|Regex to split string on matches|None|
|in_string|string|None|True|Input string|None|
|max_split|integer|0|False|Max splits - if non-zero last element is remainder of string|None|
|multiline|boolean|False|False|Make begin/end consider each line|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|[]string|True|An array of the strings returned by the split operation|

Example output:

```
{
  "result": [
    "",
    " ipsum dolor sit amet, consectetur \nadipiscing elit. Aliquam sapien ex, ",
    "s odales sed luctus ac, dapibus quis augue. Vivamus in cursus libero. Donec vehicula turpis eu ante viverra, lacinia."
  ]
}
```

## Triggers

_This plugin does not contain any triggers._

## Connection

_This plugin does not contain a connection._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

## Workflows

Examples:

This is a utility plugin used to manipulate string data using regex

## Versions

* 1.0.0 - Initial plugin

## References

* [Python Regex](https://docs.python.org/library/re.html)

## Custom Output Types

_This plugin does not contain any custom output types._