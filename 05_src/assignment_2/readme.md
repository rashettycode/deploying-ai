# 💹 Finance Support Chatbot (Assignment 2)

This project is a conversational AI system built for the **UofT DSI Deploying AI** micro credential course.  
It is designed to answer finance-related questions, show stock information, and explain simple investment ideas — while keeping the chat safe using guardrails and short-term memory.

---

## 🎯 Project Overview

The goal of this assignment was to design a small multi-service AI system with a conversational interface.  
My chatbot, **Finance Support**, helps users ask about stock prices, understand financial terms, and explore simulated market data.

It uses:
- One service that calls a real API (Alpha Vantage)  
- One service that performs a small semantic search  
- One custom service that gives plain-language financial explanations  
- A simple memory system and guardrails for safety  
- A chat interface built with **Gradio**

---

## 🧩 Services Implemented

### **Service 1 – API Calls (Alpha Vantage)**
- Uses the Alpha Vantage API to get live stock prices (e.g., AAPL, MSFT).
- The API key is stored safely in the `.secrets_f` file.
- Example response:  
  > “MSFT is currently trading at \$496.82, with a daily change of -0.0563 %.”

### **Service 2 – Semantic Search**
- Stores small text snippets about basic finance topics.
- Uses **FAISS** + **OpenAI Embeddings** (`text-embedding-3-small`) to find the most relevant answer.
- Example:  
  > “Diversification reduces portfolio risk.”

### **Service 3 – Custom Tool (Explain Simple + Simulated MCP)**
- Explains user questions in simple language.
- Can simulate an MCP connection to Yahoo Finance for extra realism.  
  (Example: *‘Simulated MCP result for Tesla and Nvidia data…’*)

---

## 💬 Chat Interface

The chatbot runs in **Gradio** with the title:

> 💹 Finance Support (Guardio 🛡️ Enabled)

Features:
- Chat window for user questions  
- 🧠 Short-term memory (last 5 exchanges)  
- 🧹 Clear Memory button to reset the context  
- 🛡️ Guardrails that block restricted topics (cats, dogs, horoscopes, Taylor Swift, etc.)


## 🧠 MCP Management


In this project, the MCP (Model Context Protocol) service is simulated rather than fully connected.
MCP is a protocol that allows AI systems to connect and communicate securely with external tools or servers in a standardized way — for example, to fetch real-time market data or interact with APIs through an agent-like process.

Since the mcp-client library currently requires Python 3.13+ and my environment uses Python 3.12, I implemented a mock MCP simulation instead.

The simulation mimics an asynchronous workflow using Python’s asyncio style functions, giving the impression of remote data retrieval.

Here’s a simplified example of how this behavior can be structured:


## Simulated MCP Call using asyncio

Example functions:
```python

import asyncio

async def simulate_mcp_request(query: str):
    """Fake async function to mimic MCP data retrieval."""
    await asyncio.sleep(1)  # simulate network delay
    return f"📡 Simulated MCP result for '{query}': Market trends mixed — tech leads gains."

# Example usage
async def main():
    result = await simulate_mcp_request("Tesla and Nvidia")
    print(result)

# asyncio.run(main())


In the live chatbot, this concept is represented in the custom tool (tools_custom.py) where user queries such as

“Use MCP to get Tesla data”

return a simulated response like:

“📡 Simulated MCP result for Tesla data: Tech stocks are leading gains today.”

This setup demonstrates understanding of asynchronous programming patterns and how MCP connections can be integrated in future versions, once the package supports the current Python environment.


## 🧠 Memory Management

File: `memory.py`

The memory keeps only the last 5 conversation pairs using a Python list.  
If the list grows too long, old messages are trimmed automatically.  
This simulates a limited context window.

Example functions:

```python
add_to_memory(user_message, bot_response)
get_recent_memory()
clear_memory()

## 🛡️ Guardrails

Certain topics are automatically filtered:

cats, dogs, horoscope, zodiac, Taylor Swift


When triggered, the bot replies:

🚫 Sorry, I can’t help you about that topic.

The emoji 🛡️ Guardio appears to show that filtering is active.

## 🧰 Folder Structure

05_src/
 └── assignment_chat/
      ├── main.ipynb          ← main logic + Gradio interface
      ├── tools_api.py        ← Alpha Vantage API service
      ├── tools_semantic.py   ← Semantic search service
      ├── tools_custom.py     ← Simple explanation / MCP simulation
      ├── memory.py           ← short-term memory manager
      ├── prompts.py          ← optional system prompts
      └── readme.md           ← Background about the logic

⚙️ How to Run

Activate your environment:

source deploying-ai-env/Scripts/activate


Load your keys:

%load_ext dotenv
%dotenv ../05_src/.secrets_f


Start the chat:

python 05_src/assignment_chat/main.py


or open main.ipynb and run all cells.

The chat launches at local
http://127.0.0.1:7860

Please note that the Public link expires after 7 days


🧩 Example Interactions

User: What is diversification?
Bot: Diversification reduces portfolio risk by spreading investments across different assets.

User: Get stock price of MSFT
Bot: MSFT is currently trading at $496.82 with a daily change of -0.0563 %.

User: Do you like cats or dogs?
Bot: 🚫 Sorry, I can’t help you about that topic.

