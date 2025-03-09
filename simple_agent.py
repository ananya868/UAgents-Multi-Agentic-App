from uagents import Agent, Context, Model   

agent = Agent(
    name="Ananya's Agent", 
    seed="hi, i work for Ananya", 
    port=8000, 
    endpoint=["http://localhost:8000/submit"]
)

@agent.on_event("startup")
async def introduce_agent(ctx: Context):
    # await ctx.send("Hello, I am Ananya's agent. I am here to help you with your queries.")
    ctx.logger.info(
        f"""
            Hello, I am{agent.name}t. I am here to help you with your queries.
            my address is {agent.address}
        """
    ) 


if __name__=="__main__": 
    agent.run()