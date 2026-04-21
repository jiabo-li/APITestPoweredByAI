from langchain_deepseek import ChatDeepSeek
from langchain.messages import HumanMessage,SystemMessage
from typing import Dict,List,Any
import json
from pathlib import Path
from config import Config

class TestCaseGenerator:
    def __init__(self,output_dir:str="generated_cases"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        print(Config.DEEPSEEK_MODEL)
        self.llm = ChatDeepSeek(
            api_key = Config.DEEPSEEK_API_KEY,
            model= Config.DEEPSEEK_MODEL,
            temperature = 0.1,
            max_tokens = 8000
        )
        self.prompts = []
        testcase_prompt = self._load_prompts()
        self.prompts.append(testcase_prompt)

    def _load_prompts(self):
        prompts_dir = Path(__file__).parent/"prompts"
        prompts_file=prompts_dir/"test_case_prompt.md"

        if prompts_file.exists():
            with open(prompts_file,'r',encoding='utf-8') as f:
                return {"type":"text",'text': f.read()}

        return {"type":"text","test_case_prompt":self._get_default_prompt()}

    def generate_test_cases(self,swagger_content):
        swagger_prompt = {"type":"text","text":swagger_content}
        self.prompts.append(swagger_prompt)

        messages =[
            SystemMessage(content="You are an API testing engineer and good at generating API test cases accoring to the swagger content"),
            HumanMessage(content=self.prompts)
        ]
        print(messages)
        response = self.llm.invoke(messages)
        test_case = response.content

        #test_case = "mock test case"

        test_case_file = self.output_dir/"API_testcase.md"

        with open(test_case_file,'w',encoding="utf-8") as f:
            f.write(test_case)

        return test_case
    def _get_default_prompt(self):
        return """generate API test cases according OpenAPI/Swagger document"""

