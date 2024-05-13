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
    interpreter.llm.model='gpt-4'
    interpreter.auto_run=True
    interpreter.os=True
    messages = interpreter.chat(chat.command)
    return {
      'messages': messages
    }

    
@app.get("/api/history")
def history_endpoint():
    return interpreter.messages