import json

with open("config.json") as config_file:
    config = json.load(config_file)


def kvstore(request):
    keys = request.path[4:].split("/")  # remove the /kv/

    try:
        conf = config
        for key in keys:
            conf = conf[key]
    except Exception:
        return "Not Found", 404

    return json.dumps(conf), 200, {"Content-Type": "application/json"}
