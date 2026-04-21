import json
import yaml

import requests

from typing import Dict,Optional

class SwaggerReader:

    def __init__(self,source:str):
        self.source = source
        self.content = self._read_content()
        self.spec=""

    def _read_content(self):
        try:
            if self.source.startswith(('http://','https://')):
                response = requests.get(self.source)
                response.raise_for_status()
                return response.text
            else:
                with open(self.source,'r',encoding='utf-8') as f:
                    return f.read()
        except Exception as e:
            raise Exception(f"Read Swagger doc failed:{str(e)}")


    def _parse_content(self):
        try:
            return json.loads(self.content)
        except json.JSONDecodeError:
            return yaml.safe_load(self.content)

    def get_raw_content(self):
        return self.content