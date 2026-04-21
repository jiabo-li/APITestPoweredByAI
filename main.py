import argparse
from config import Config
from swagger_parser import SwaggerReader
from pathlib import Path
from test_generator import TestCaseGenerator

from code_generator import CodeGenerator

class APITestGenerator:
    def __init__(self,swagger_source:str):
        self.swagger_source = swagger_source
        self.reader = SwaggerReader(swagger_source)
        self.test_generator = TestCaseGenerator()
        self.code_generator = CodeGenerator(Config.BASE_URL,Config.OUTPUT_DIR)

    def run(self):
        swagger_content = self.reader.get_raw_content()
        test_cases = self.test_generator.generate_test_cases(swagger_content)
        self.code_generator.generate_test_code(swagger_content,test_cases)


def main():
    soursfile = str(Path(__file__).parent/"swagger"/"input.md")

    apigenerator = APITestGenerator(soursfile)

    apigenerator.run()


if __name__ == "__main__":
    main()