# Python - Serialization

This project explores **serialization** and **marshaling**: converting Python data structures into a format that can be saved to a file or sent over a network, and then rebuilding them later.

## Learning Objectives

- Explain the difference between marshaling and serialization
- Serialize and deserialize Python data using JSON, pickle, CSV and XML
- Understand how serialized data is used in files, web applications and network communication
- Compare serialization formats such as JSON, XML and binary formats

## Requirements

- Python 3.x
- Editor: `vi`, `vim` or `emacs`
- All files end with a new line
- First line of every Python file: `#!/usr/bin/python3`
- Code follows the `pycodestyle` style
- All files are executable

## Tasks

### 0. Basic Serialization

**File:** `task_00_basic_serialization.py`

A module that serializes a Python dictionary to a JSON file and deserializes it back.

| Function | Parameters | Description |
|----------|------------|-------------|
| `serialize_and_save_to_file(data, filename)` | `data`: a Python dictionary<br>`filename`: output JSON file | Writes `data` to `filename` as JSON. If the file already exists, it is replaced. |
| `load_and_deserialize(filename)` | `filename`: input JSON file | Reads the JSON file and returns the data as a Python dictionary. |

**How it works**

- `json.dump(data, f)` converts the dictionary to JSON and writes it into the open file.
- `json.load(f)` reads JSON from the open file and returns a Python dictionary.
- The file is opened with mode `"w"` for writing (which replaces an existing file) and `"r"` for reading.

**Usage**

```python
#!/usr/bin/env python3
from task_00_basic_serialization import load_and_deserialize, serialize_and_save_to_file

data_to_serialize = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

serialize_and_save_to_file(data_to_serialize, 'data.json')
print("Data serialized and saved to 'data.json'.")

deserialized_data = load_and_deserialize('data.json')
print("Deserialized Data:")
print(deserialized_data)
```

**Output**

```
$ ./main_00.py
Data serialized and saved to 'data.json'.
Deserialized Data:
{'name': 'John Doe', 'age': 30, 'city': 'New York'}
$ cat data.json
{"name": "John Doe", "age": 30, "city": "New York"}
```

### 1. Pickling Custom Classes

**File:** `task_01_pickle.py`

A `CustomObject` class that can save itself to a file and be rebuilt from it using the `pickle` module.

| Member | Description |
|--------|-------------|
| `CustomObject(name, age, is_student)` | Creates an object with a string `name`, an integer `age` and a boolean `is_student`. |
| `display(self)` | Prints the object's attributes (`Name`, `Age`, `Is Student`). |
| `serialize(self, filename)` | Pickles the current instance and saves it to `filename`. Returns `None` on error. |
| `deserialize(cls, filename)` | Class method. Loads and returns the instance stored in `filename`. Returns `None` if the file does not exist or is malformed. |

**How it works**

- `pickle` writes **binary** data, so files are opened with `"wb"` (write) and `"rb"` (read).
- `pickle.dump(self, f)` saves the whole object, and `pickle.load(f)` rebuilds it.
- `deserialize` is a `@classmethod` because it is called on the class (`CustomObject.deserialize(...)`) before any object exists.
- Errors are handled with `try / except`.

**Usage**

```python
#!/usr/bin/env python3
from task_01_pickle import CustomObject

obj = CustomObject("John", 25, True)
obj.serialize("obj.pkl")

new_obj = CustomObject.deserialize("obj.pkl")
new_obj.display()

print(CustomObject.deserialize("nothing.pkl"))
```

**Output**

```
Name: John
Age: 25
Is Student: True
None
```

### 2. Converting CSV Data to JSON Format

**File:** `task_02_csv.py`

| Function | Parameters | Description |
|----------|------------|-------------|
| `convert_csv_to_json(csv_filename)` | `csv_filename`: input CSV file | Reads the CSV with `csv.DictReader`, and writes the rows as a list of dictionaries to `data.json`. Returns `True` on success, `False` on error (for example, file not found). |

**How it works**

- `csv.DictReader` turns each row into a dictionary, using the header row as keys.
- `list(...)` collects all rows into a list of dictionaries.
- `json.dump` writes that list to `data.json`.
- All CSV values are read as strings, so numbers such as `age` are saved as `"28"`.

**Usage**

`data.csv`:

```
name,age,city
John,28,New York
Alice,24,Los Angeles
Bob,22,Chicago
Eve,30,San Francisco
```

```python
#!/usr/bin/env python3
from task_02_csv import convert_csv_to_json

print(convert_csv_to_json("data.csv"))
print(convert_csv_to_json("nothing.csv"))
```

**Output**

```
True
False
```

`data.json`:

```json
[
    {"name": "John", "age": "28", "city": "New York"},
    {"name": "Alice", "age": "24", "city": "Los Angeles"},
    {"name": "Bob", "age": "22", "city": "Chicago"},
    {"name": "Eve", "age": "30", "city": "San Francisco"}
]
```

### 3. Serializing and Deserializing with XML

**File:** `task_03_xml.py`

| Function | Parameters | Description |
|----------|------------|-------------|
| `serialize_to_xml(dictionary, filename)` | `dictionary`: a Python dictionary<br>`filename`: output XML file | Creates a `<data>` root, adds one child element per dictionary item, and writes the tree to `filename`. |
| `deserialize_from_xml(filename)` | `filename`: input XML file | Parses the XML file and returns a Python dictionary. |

**How it works**

- `ET.Element("data")` creates the root, and `ET.SubElement(root, key)` adds a child for each key.
- Each value is stored as text with `str(value)`.
- When reading back, each child's tag becomes the key and its text becomes the value.
- XML does not distinguish numbers from strings, so every value is returned as a **string**.

**Usage**

```python
#!/usr/bin/env python3
from task_03_xml import serialize_to_xml, deserialize_from_xml

sample_dict = {
    'name': 'John',
    'age': '28',
    'city': 'New York'
}

serialize_to_xml(sample_dict, "data.xml")
print("Dictionary serialized to data.xml")

print("\nDeserialized Data:")
print(deserialize_from_xml("data.xml"))
```

**Output**

```
Dictionary serialized to data.xml

Deserialized Data:
{'name': 'John', 'age': '28', 'city': 'New York'}
```

`data.xml`:

```xml
<data><name>John</name><age>28</age><city>New York</city></data>
```

## Format Comparison

| Format | Readable by humans | Keeps Python types | Used for |
|--------|--------------------|--------------------|----------|
| JSON | Yes | Basic types only | Web APIs, config files |
| pickle | No (binary) | Yes, including custom classes | Python-only storage |
| CSV | Yes | No (all strings) | Tables and spreadsheets |
| XML | Yes | No (all strings) | Structured documents, data exchange |

## Resources

- Real Python: Serialization
- Real Python: Working With JSON Data in Python
- Python `pickle` documentation
- Python `json` documentation
- Python XML ElementTree guide
- Socket programming guide

## Author

Abdulrhman saleh alduqil
