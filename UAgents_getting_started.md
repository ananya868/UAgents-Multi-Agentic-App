## **UAgents**

`Getting Started`

**What is it?**

A framework that lets us build decentralized AI agents, enables agent communications and create intelligent agent (LLMs) or basic APIs 



**Concepts**

> **Agent Address**: This address identifies the agent within the Fetch Network. It's similar to a username within a chat platform, allowing other agents to discover
> and communicate with that specific agent by querying that agent's 
> information from the Almanac contract.

> **Fetch Network Address**: Transactional address to communicate in the fetch network, hold cryptocurrency, interact with fetch ledger and perform secure transactions.



> **Seed Phrase**: Imagine you have a treasure chest full of your code, but instead of a key, it has a secret password to open it. This password is made up of 
> any characters you choose. This "password" is your seed phrase, when you create one make it really complicated.

> **Almanac**: The Almanac contract is a decentralised register of all agents that are available in the system. Registration makes the agents available to marketplace so that anybody could use it. You can also create your own communication protocol without registering. 



> **FET Token**: Since payments in this network can be micro, so and cannot be employble by traditional currencies, FET tokens are used instead to facilitate payments. You have to buy these FET tokens with your preferred currency from apps like coinbase or Binance. Store these in ASI wallet, can also use ledger for long time storage.
> 
> *To use FET tokens with agents:*
> 
> ```python
> from uagents import Agent, Context
> import cosmpy
>  
> from cosmpy.aerial.client import LedgerClient, NetworkConfig
>  
> agent = Agent(name="alice", seed="", port=8000, test=False,  endpoint=["http://localhost:8000/submit"])
>  
> @agent.on_event("startup")
> async def introduce_agent(ctx: Context):
>     ctx.logger.info(f"ASI network address:{agent.wallet.address()}")
>     ledger_client = LedgerClient(NetworkConfig.fetch_mainnet())
>     address: str = agent.wallet.address()
>     balances = ledger_client.query_bank_all_balances(address)
>     ctx.logger.info(f"Balance of addr: {balances}")
>  
> if __name__ == "__main__":
>     agent.run()
> 
> ```

> You can now use this address to transfer your purchased FET tokens from the exchange to this Agent's address. This
> should be as simple as withdrawing native FET, by selecting the Fetch.ai Mainnet network when withdrawing.






