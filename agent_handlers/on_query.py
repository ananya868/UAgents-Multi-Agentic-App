import json 
import uvicorn

from fastapi import FastAPI, Request 
from uagents import Model
from uagents.query import query 
from uagents.envelope import Envelope 


AGENT_ADDRESS = "agent1qt6ehs6kqdgtrsduuzslqnrzwkrcn3z0cfvwsdj22s27kvatrxu8sy3vag0"


class TestRequest(Model):
    message: str


async def agent_query(req):
    response = await query(
        destination=AGENT_ADDRESS,
        message=req, 
        timeout=15 
    )
    if isinstance(response, Envelope):
        data = json.loads(response.decode_payload())
        return data["text"]
    else:
        print("Error: ", response)
    return response


# Make an API 
app = FastAPI() 

@app.get("/")
def read_root(): 
    return "Hello from agent controller"


@app.post("/endpoint")
async def endpoint(req: Request): 
    model = TestRequest.parse_obj(await req.json())
    try: 
        res = await agent_query(model)
        return f"Success: agent response- {res}"
    except Exception as e:
        return f"Error: {e}"

