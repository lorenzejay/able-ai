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
    interpreter.llm.model='llama3-70b-8192'
    interpreter.llm.api_key= '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'
    interpreter.llm.api_base='https://api.groq.com/openai/v1'
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
    interpreter.auto_run=True
    print('interpreter.messages', interpreter.messages)
    result = interpreter.chat(chat.command)
    print('result', result)
    
    return {
      "messages": messages
    }


@app.get("/history")
def history_endpoint():
    return interpreter.messages