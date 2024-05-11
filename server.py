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
    interpreter.chat(chat.command)
    # def event_stream():
    #     for result in interpreter.chat(message, stream=True):
    #         yield f"data: {result}\n\n"

    # return StreamingResponse(event_stream(), media_type="text/event-stream")

@app.get("/history")
def history_endpoint():
    return interpreter.messages