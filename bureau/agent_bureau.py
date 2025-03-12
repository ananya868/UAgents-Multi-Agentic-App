from uagents import Agent, Context, Model 

class Message(Model): 
    message: str 


agent_a = Agent("agent_a", seed="agent_a recovery phrase")
agent_b = Agent("agent_b", seed="agent_b recovery phrase")


# Tasks | Behavior 

"""Agent A"""
@agent_a.on_interval(period=3.0)
async def send_message(ctx: Context): 
    await ctx.send(agent_b.address, Message(message="Hello from agent_a"))

@agent_a.on_message(model=Message)
async def agent_a_handle_message(ctx: Context, sender: str, msg: Message): 
    ctx.logger.info(f"Received message from {sender}: {msg.message}")


"""Agent B"""
@agent_b.on_message(model=Message)
async def agent_b_handle_message(ctx: Context, sender: str, msg: Message): 
    ctx.logger.info(f"Received message from {sender}: {msg.message}")
    await ctx.send(agent_a.address, Message(message="Reply from agent_b"))


"""Creating the Bureau"""

from uagents import Bureau 

# bureau = Bureau()

# or 
bureau = Bureau(
    port=8000, 
    agents=[agent_a, agent_b], 
    endpoint="http://localhost:8000/submit"
)

# bureau.add(agent_a)
# bureau.add(agent_b)


if __name__ == "__main__": 
    bureau.run()

