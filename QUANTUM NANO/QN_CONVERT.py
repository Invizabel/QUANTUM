import base64
import gzip
import lzma

with open("QN_SOURCE.py", "rb") as file:
    content = file.read()

if len(base64.b64encode(gzip.compress(content))) <=  len(base64.b64encode(lzma.compress(content))):
    print(f"GZIP | {len(base64.b64encode(gzip.compress(content)))}")
    print(base64.b64encode(gzip.compress(content)))

else:
    print(f"LZMA | {len(base64.b64encode(lzma.compress(content)))}")
    print(base64.b64encode(lzma.compress(content)))
