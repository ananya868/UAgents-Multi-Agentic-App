from uagents import Agent, Context, Model 


class Message(Model): 
    message: str

RECIPIENT_ADDRESS = (
    "test-agent://agent1qwq878m02vecg946cq6f3c9eyehpldu9gsxkgrzkkk20lza2mxsks7hd2xm"
)

SenderAgent = Agent(
    name="SenderAgent", 
    port=8000,
    seed="SenderAgent Secret Phrase", 
    endpoint=["http://127.0.0.1:8000/submit"],
)

print(SenderAgent.address) # Sender's agent 

# Tasks 
@SenderAgent.on_interval(period=2.0)
async def send_text(ctx: Context): 
    await ctx.send(
        RECIPIENT_ADDRESS,
        Message(
            message="Hello, Lets start our conversation!"
        )
    )

@SenderAgent.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message): 
    ctx.logger.info(f"Received message from {sender}: {msg.message}")


if __name__ == "__main__": 
    SenderAgent.run()