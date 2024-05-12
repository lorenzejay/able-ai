from interpreter import OpenInterpreter
interpreter = OpenInterpreter(import_computer_api=True)

# interpreter.llm.model='llama3-70b-8192'
interpreter.llm.model='gpt-4-turbo'

# interpreter.llm.api_key= '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'
# interpreter.llm.api_base='https://api.groq.com/openai/v1'
interpreter.auto_run=True
interpreter.verbose=True
interpreter.max=True
# interpreter.custom_instructions=''
interpreter.os=True
# interpreter.computer

# interpreter.chat('open slack app and send a message saying "hello world from our automation" to Federico') 
# interpreter.chat('search for ai events on cerebral valley and add all the future events you see to the numbers app save the sheet as upcoming events.') 
interpreter.chat('open the Obsidian app and create a new note with command + n, call it hello world from shack15, and write a blurb about a hackathon and winning it') 
# does not work
# interpreter.chat('open twitter on Google Chrome and type a tweet saying hello from @shack15.') 