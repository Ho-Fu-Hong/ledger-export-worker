import json
from pathlib import Path

import requests

CONFIG = json.loads((Path(__file__).resolve().parents[1] / "config" / "worker.json").read_text())


def export_snapshot(rows):
    api = CONFIG["Export"]
    response = requests.post(api["BaseUrl"] + "/snapshots", json={"rows": rows},
                             auth=(api["ClientId"], api["ClientSecret"]), timeout=30)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(export_snapshot([]))
