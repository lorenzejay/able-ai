from interpreter import interpreter

interpreter.llm.model='llama3-70b-8192'
interpreter.llm.api_key= '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'
interpreter.llm.api_base='https://api.groq.com/openai/v1'
interpreter.auto_run=True
interpreter.verbose=True

interpreter.chat('open youtube on safari')