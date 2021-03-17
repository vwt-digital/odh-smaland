import os
import subprocess
import time

import requests
from requests.packages.urllib3.util.retry import Retry


def test_args():
    port = os.getenv(
        "PORT", 8080
    )  # Each functions framework instance needs a unique port

    process = subprocess.Popen(
        [
            "functions-framework",
            "--target",
            "kvstore",
            "--source",
            "../main.py",
            "--port",
            str(port),
        ],
        cwd=os.path.dirname(__file__),
        stdout=subprocess.PIPE,
    )

    time.sleep(0.5)

    # Send HTTP request simulating Pub/Sub message
    # (GCF translates Pub/Sub messages to HTTP requests internally)
    BASE_URL = f"http://localhost:{port}"

    retry_policy = Retry(total=6, backoff_factor=2)
    retry_adapter = requests.adapters.HTTPAdapter(max_retries=retry_policy)

    session = requests.Session()
    session.mount(BASE_URL, retry_adapter)

    url = "{}/kv/item1".format(BASE_URL)

    res = requests.get(url)
    assert res.text == '{"key1": "value1", "key2": "value2"}'

    # Stop the functions framework process
    process.kill()
    process.wait()
