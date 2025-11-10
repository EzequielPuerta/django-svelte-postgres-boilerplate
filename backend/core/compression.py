import base64
import zlib
from typing import Union

def compress_content(content: Union[str, bytes]) -> str:
    if isinstance(content, str):
        content = content.encode("utf-8")
    compressed = zlib.compress(content)
    return base64.b64encode(compressed).decode("utf-8")


def decompress_content(encoded: str) -> str:
    compressed = base64.b64decode(encoded.encode("utf-8"))
    return zlib.decompress(compressed).decode("utf-8")