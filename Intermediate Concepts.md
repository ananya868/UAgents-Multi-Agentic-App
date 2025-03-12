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
   
   - Used to handle message requests and response

3. Answer Queries:  .on_query( )
   
   - Used to handle messages requests and responses with a pre-defined response logic

4. Triggered by Event:  .on_event( )
   
   - 


**Types of Agents**

1. **Hosted Agents**: State changes after each call, easy to handle, low flexibility in configurations 
2. **Local Agents**: State doesn't change after each call, highly configurable, extensibility with other frameworks, little complex. Local Agents are perfect for high-performance, real-time applications requiring deep customization, resource management, and direct integration with local functions.
3. **MailBox Agents**: To manage such scenarios, the Mailbox feature in Agentverse allows Agents to receive messages while they are offline with ease. Once the Agent comes back online, it can retrieve these messages from its mailbox.
4. **Proxy Agents**: A Proxy serves as a bridge between your Agent and the Agentverse, allowing the Agent to publish interaction data without needing a Mailbox. 


