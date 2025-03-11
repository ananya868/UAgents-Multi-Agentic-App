### **Intermediate Concepts**

**Communication between Agents**

Local: Two agents can communicate locally without needing to register in Almanac contract. To run two agents, use Bureau( ) method to run multiple agents in the same script. 

Remote: Two or more agents can communicate remotely. Agents need to be registered in Almanac contract and have addresses. Using this address, agent can be communicated  

**Agent Protocols**

Holds the message type and handlers for the agent. 

Let's suppose an agent 'a' is an agent for a restaurant, whose job is to handle table booking requests. We can define a booking protocol and also define the desired logic to determine if the booking is successful or not. 

After creation of this protocol, you can include this protocol into your agent.

**Agent Handlers**

These are functions which are used along with decoraters, to be only triggered on a condition. 

1. Interval Tasks:  .on_interval( )
   
   - Can be used to do tasks periodically 

2. Handle Messages:  .on_message( )
   
   - 

3. Answer Queries:  .on_query( )
   
   - 

4. Triggered by Event:  .on_event( )
   
   - 
