import json
from pathlib import Path

WEB_DIR = Path(__file__).resolve().parent
DATA_JSON = WEB_DIR / "data.json"
DATA_JS = WEB_DIR / "data.js"


def sync():
    data = json.loads(DATA_JSON.read_text(encoding="utf-8"))
    js_content = (
        "// Auto-generated from data.json. Do not edit manually.\n"
        "window.JOBS_DATA = "
        + json.dumps(data, ensure_ascii=False, indent=2)
        + ";\n"
    )
    DATA_JS.write_text(js_content, encoding="utf-8")
    print(f"Synced {len(data.get('companies', []))} companies to {DATA_JS}")


if __name__ == "__main__":
    sync()
