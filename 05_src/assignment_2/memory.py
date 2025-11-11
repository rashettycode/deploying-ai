# --- memory.py ---
"""
Simple short-term memory manager for the Finance Assistant.
Stores and trims conversation history to avoid overflowing context.
"""

MAX_MEMORY = 5  # only keep last 5 exchanges

conversation_memory = []


def add_to_memory(user_message: str, bot_response: str):
    """Add a new pair of user and bot messages to memory."""
    global conversation_memory
    conversation_memory.append((user_message, bot_response))
    # Trim memory to avoid exceeding the context limit
    if len(conversation_memory) > MAX_MEMORY:
        conversation_memory = conversation_memory[-MAX_MEMORY:]


def get_recent_memory():
    """Return the last few conversation turns as formatted text."""
    return "\n".join(
        [f"User: {u}\nBot: {b}" for u, b in conversation_memory[-MAX_MEMORY:]]
    )


def clear_memory():
    """Clear all conversation history."""
    global conversation_memory
    conversation_memory = []
