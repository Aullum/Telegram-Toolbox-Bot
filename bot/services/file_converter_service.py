import pandas as pd
import json
import io

def convert_json_to_csv(json_bytes: bytes) -> bytes:
    try:
        data = json.loads(json_bytes.decode("utf-8"))
        if not isinstance(data, list):
            raise ValueError("JSON root must be an array of objects")

        df = pd.DataFrame(data)
        output = io.StringIO()
        df.to_csv(output, index=False)
        return output.getvalue().encode("utf-8")

    except Exception as e:
        raise ValueError(f"Conversion failed: {str(e)}")
