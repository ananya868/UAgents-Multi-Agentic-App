from uagents import Model, Context, Message, Protocol 


class BookTableRequest(Model): 
    table_number: int 

class BookTableResponse(Model): 
    success: bool 


# A logic that decides whether the success is True or False for that specific table number 
book_proto = Protocol()

@book_proto.on_message(model=BookTableRequest, replies={BookTableResponse})
async def handle_book_request(
    ctx: Context, sender: str, msg: BookTableRequest
):  
    """
        This function handles the booking request for a table number. 
    """
    if ctx.storage.has(str(msg.table_number)): 
        success=False # Table is already booked 
    else:
        success=True 
        ctx.storage.set(str(msg.table_number), sender)
        # New booking for table number along with sender 

    await ctx.send(sender, BookTableResponse(success=success))



# Do NOT run this script 
# Create agents and use this protocol with the agents 
#  Done 
#  This protocol can be accessed by 
from protocols.book import book_proto 
# Let's suppose your agent is called 'restaurant'
#  You can now use this protocol as follows
restaurant.include(book_proto)


