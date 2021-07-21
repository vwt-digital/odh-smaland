import json

with open("config.json") as config_file:
    config = json.load(config_file)


def kvstore(request):
    key = request.path[4:]  # remove the /kv/

    request_json = request.get_json(silent=True)

    if request_json and "key" in request_json:
        key = request_json["key"]

    keys = key.split("/")

    try:
        conf = config
        for key in keys:
            conf = conf[key]
    except Exception:
        return "Not Found", 404

    return json.dumps(conf).strip('"'), 200, {"Content-Type": "application/json"}
