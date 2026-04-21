You are a senior test engineer.

Please generate standard-format test cases based on the following OpenAPI interface definition (do not generate code).

## Interface Information
- Path: {path}
- Method: {method}
- Description: {description}
- Request Parameters: {parameters}
- Request Body Structure: {request_body}
- Response Definition: {responses}

## Output Requirements
Please output test cases in the following format. Each test case must include:
1. **Test Case ID**: TC_{Interface Name}_{Sequence Number}
2. **Test Title**: Brief description of the test scenario
3. **Preconditions**: Data or state that needs to be prepared
4. **Test Steps**: Operation steps
5. **Test Data**: Specific parameter values to be used
6. **Expected Result**: HTTP status code + response key field validation

## Scenarios to Cover (at minimum)
- Normal scenario: All required parameters are correct, expected success
- Missing parameter: Missing a required parameter
- Parameter type error: Parameter type mismatch
- Boundary value: Parameter takes minimum/maximum values
- Exception ID / Resource not found: Accessing a non-existent resource

Please output the test cases directly, do not generate code.