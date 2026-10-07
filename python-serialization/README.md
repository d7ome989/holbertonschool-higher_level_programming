# Python - Serialization

This project explores **serialization** and **marshaling**: converting Python data structures into a format that can be saved to a file or sent over a network, and then rebuilding them later.

## Learning Objectives

- Explain the difference between marshaling and serialization
- Serialize and deserialize Python data using JSON
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

#### How it works

- `json.dump(data, f)` converts the dictionary to JSON and writes it into the open file.
- `json.load(f)` reads JSON from the open file and returns a Python dictionary.
- The file is opened with mode `"w"` for writing (which replaces an existing file) and `"r"` for reading.

#### Usage

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

#### Output

```
$ ./main_00.py
Data serialized and saved to 'data.json'.
Deserialized Data:
{'name': 'John Doe', 'age': 30, 'city': 'New York'}
$ cat data.json
{"name": "John Doe", "age": 30, "city": "New York"}
```

## Resources

- Real Python: Serialization
- Real Python: Working With JSON Data in Python
- Python `pickle` documentation
- Python `json` documentation
- Python XML ElementTree guide
- Socket programming guide

## Author

Abdulrhman saleh alduqil
