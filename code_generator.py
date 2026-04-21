from langchain_deepseek import ChatDeepSeek
from langchain.messages import HumanMessage,SystemMessage
from typing import Dict,List,Any

from pathlib import Path
import json
from config import Config

class CodeGenerator:
    def __init__(self,base_url,output_dir:str="generated_tests"):
        self.base_url = base_url
        self.outputdir = Path(output_dir)
        self.outputdir.mkdir(exist_ok=True)
        self.prompts = []
        testcode_prompt = self._load_prompts()
        self.prompts.append(testcode_prompt)

        self.llm =ChatDeepSeek(
            api_key = Config.DEEPSEEK_API_KEY,
            model=Config.DEEPSEEK_MODEL,
            temperature = 0.2,
            max_tokens = 8000
        )

    def  _load_prompts(self):
        prompts_dir = Path(__file__).parent/"prompts"
        prompts = {}
        prompts["type"]="text"
        prompt_files = ['test_code_prompt.md','conftest_prompt.md']

        for filename in prompt_files:
            file_path = prompts_dir / filename
            if file_path.exists():
                with open(file_path,'r',encoding='utf-8') as f:
                    prompts["text"] = f.read()

        return prompts

    def generate_test_code(self,swagger_content:str,test_cases:Dict):

        prompts = self._format_test_code_prompt(swagger_content,test_cases)
        message = [
            SystemMessage(content="You are an API test engineer and good at generating pytest test code"),
            HumanMessage(content=self.prompts)
        ]

        print(self.prompts)
        reponse = self.llm.invoke(message)
        test_code = self._clean_code(reponse.content)

        #test_code = "mock python script"

        test_file = self.outputdir/"test_api.py"

        with open(test_file,'w',encoding='utf-8') as f:
            f.write(test_code)

        return test_file
    def _format_test_code_prompt(self,swagger_content:str,test_cases:Dict):
        testcode_prompt ={"type":"text",'text': swagger_content}

        testcase_prompt = {"type":"text",'text': test_cases}

        self.prompts.append(testcode_prompt)
        self.prompts.append(testcase_prompt)

    def _get_default_code_prompt(self):
        return "generate pytest API test code according OpenAPI/Swagger document"

    def _clean_code(self,code):
        if '```python' in code:
            code = code.split("```python")[1].split('```')[0]
        elif '```' in code:
            code = code.split('```')[1].split('```')[0]
        return code.strip()