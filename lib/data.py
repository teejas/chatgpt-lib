import json

def write_msgs_to_file(msgs: list, filepath: str):
    # always overwrite
    json_object = json.dumps(msgs, indent=2)
    if filepath[0] == "/":
        actual_path = "./data/" + filepath[1:]
    else:
        actual_path = "./data/" + filepath
    with open(actual_path, "w") as f:
        f.write(json_object)
    pass

def read_msgs_from_file(filepath: str) -> list:
    if filepath[0] == "/":
        actual_path = "./data/" + filepath[1:]
    else:
        actual_path = "./data/" + filepath
    with open(actual_path, "r") as f:
        msgs = json.load(f)
    return msgs