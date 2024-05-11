from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from interpreter import interpreter
from pydantic import BaseModel

app = FastAPI()

class ChatMessage(BaseModel):
    command: str

@app.post("/api/chat")
async def chat_endpoint(chat: ChatMessage):
    print('data',chat)
    interpreter.auto_run = True
    messages = interpreter.chat(chat.command)
    return {
      'messages': messages
    }
@app.post("/api/follow-up")
async def chat_endpoint_2(chat: ChatMessage):
    interpreter.auto_run = True
    print('interpreter.messages', interpreter.messages)
    result = interpreter.chat(chat.command)
    print('result', result)
    
    return {
      "messages": messages
    }


@app.get("/history")
def history_endpoint():
    return interpreter.messages