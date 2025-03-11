from uagents import Agent, Bureau, Context, Model 

class Message(Model):
    message: str 


sigmar = Agent(
    name="sigmar",
    seed="sigmar recovery phrase",
    port=8000, 
    endpoint=["http://localhost:8000/submit"]
)
slaanesh = Agent(
    name="slaanesh",
    seed="slaanesh recovery phrase",
    port=8001, 
    endpoint=["http://localhost:8001/submit"]
)


# Let's define sigmar's behavior 
# sigmar will send message to slaanesh periodically 
@sigmar.on_interval(period=3.0)
async def send_message(ctx: Context): 
    await ctx.send(slaanesh.address, Message(message="Hello there, slaanesh!"))


# log messages received to sigmar 
@sigmar.on_message(model=Message)
async def sigmar_message_handler(ctx: Context, sender: str, msg: Message): 
    ctx.logger.info(f"Received message from {sender}: {msg.message}")
# the on_message function in this decorator is a coroutine function that will be called when a message is received


# Let's define slaanesh's behavior
@slaanesh.on_message(model=Message)
async def slaanesh_message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")
    await ctx.send(sigmar.address, Message(message="hello there sigmar"))
 

bureau = Bureau()
# Bureau is a class that allows agents to be run in the same script 

bureau.add(sigmar)
bureau.add(slaanesh)


if __name__=="__main__": 
    bureau.run()
