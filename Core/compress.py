import gzip
import json
class Compress:
    def __init__(self):
        self.data = []

    def compress(self, jsonData):
        json_str = json.dumps(jsonData) + "\n"  # 2. string (i.e. JSON)
        json_bytes = json_str.encode('utf-8')  # 3. bytes (i.e. UTF-8)
        with gzip.open("jsonfilename.json", 'w') as fout:  # 4. fewer bytes (i.e. gzip)
            fout.write(json_bytes)

