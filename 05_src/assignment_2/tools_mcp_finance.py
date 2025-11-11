# --- tools_mcp_finance.py ---
import asyncio

async def yahoo_finance_search(query: str):
    """
    Simulated MCP connection to Yahoo Finance tool on glama.ai.
    Mimics an asynchronous data call returning external financial info.
    """
    await asyncio.sleep(1)  # pretend to contact a remote MCP server

    # Produce a simple, friendly, simulated reply
    return (
        f"📡 Simulated MCP result for '{query}': "
        f"The market shows mixed trends today for {query.title()}. "
        f"Tech stocks are leading gains, while energy sectors remain flat."
    )
    