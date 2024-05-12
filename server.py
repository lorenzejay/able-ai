from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from interpreter import OpenInterpreter
interpreter = OpenInterpreter(import_computer_api=True)

app = FastAPI()

class ChatMessage(BaseModel):
    command: str

@app.post("/api/chat")
async def chat_endpoint(chat: ChatMessage):
    print('data',chat)
    interpreter.auto_run = True
    interpreter.llm.model='gpt-4-turbo'
    # interpreter.llm.model='llama3-70b-8192'
    # interpreter.llm.api_key= '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'
    # interpreter.llm.api_base='https://api.groq.com/openai/v1'
    interpreter.custom_instructions='My work apps are: ["Arc", "Google Chrome", "Obsidian", "Xcode"], sometimes you need to open or close them.'
    interpreter.auto_run=True
    interpreter.verbose=True

    messages = interpreter.chat(chat.command)
    return {
      'messages': messages
    }

@app.post("/api/follow-up")
async def chat_endpoint_2(chat: ChatMessage):
    interpreter.auto_run = True
    interpreter.llm.model='llama3-70b-8192'
    interpreter.llm.api_key= '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'
    interpreter.llm.api_base='https://api.groq.com/openai/v1'
    interpreter.custom_instructions='My work apps are: ["Arc", "Google Chrome", "Obsidian", "Xcode"], sometimes you need to open or close them.'
    interpreter.auto_run=True
    print('interpreter.messages', interpreter.messages)
    result = interpreter.chat(chat.command)
    print('result', result)
    
@app.get("/history")
def history_endpoint():
    return interpreter.messages