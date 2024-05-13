from interpreter import OpenInterpreter
interpreter = OpenInterpreter(import_computer_api=True)

# for quick tests
interpreter.llm.model='gpt-4-turbo'
interpreter.auto_run=True
interpreter.verbose=True
interpreter.max=True
interpreter.os=True

interpreter.chat('open twitter on safari then add a test tweet')  
