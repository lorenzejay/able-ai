# Bringing Open Interpreter to your Apple Ecosystem w/ Apple Shortcuts

<blockquote class="twitter-tweet">
  <p lang="en" dir="ltr">@vkash16
 and I showed our AI assistant to 
@bcristei
 
@altryne
 in the 
@SHACK15sf
 hackathon today. We used 
@OpenInterpreter
, 
@GroqInc
, 
@ollama
 with llama3 to have an AI agent control our computer without typing. We aim to shift the paradigm of voice assistants to handle agentic workflows automating tasks like an actual personal assistant. Here’s our demo examples:
</p>&mdash; Lorenze Jay (@lorenzejayTech) <a href="https://x.com/lorenzejayTech/status/1789819432254234755">View our twitter post here</a>
</blockquote>

## Hackathon Project:

Most people have a smartphone, and instead of an additional device, would prefer connecting with their AI agents through the device they already own.

Our focus is on agentic accessibility through the users current mobile device to help reshape the paradigm of how we interact with our mobile command interfaces.

Our first example is leveraging open interpreter (and future local AI agents) triggered by your phone for a hands/typing free user experience.

# Local Server

## run local server

`uvicorn server:app --host 0.0.0.0 --port 8000`

## Local Tunnel for Iphone Shortcuts

`ngrok http --domain=<your-domain-set> 8000`

## Tools:

1. ngrok
2. open interpreter
3. fastapi

## Shortcut

https://www.icloud.com/shortcuts/f0618b8008654d6d93a4422cb1564dd6
