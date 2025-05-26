import asyncio
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mcp_adapters.client import MultiServerMCPClient

load_dotenv()


async def list_tools():
    client = MultiServerMCPClient(
        {
            "mcp-yahoo-finance": {
                "command": "uvx",
                "args": ["mcp-yahoo-finance"],
                "transport": "stdio",
            },
        }
    )
    return await client.get_tools()


async def main():
    tools = await list_tools()
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )
    llm_with_tools = llm.bind_tools(tools)

    messages = [{"role": "user", "content": "What is current price of Tesla?"}]
    result = await llm_with_tools.ainvoke(messages)
    if result.tool_calls:
        messages.append({
            "role": "assistant", "content": "", "tool_calls": result.tool_calls
        })
        price = await tools[0].ainvoke(result.tool_calls[0]["args"])
        messages.append({
            "role": "tool",
            "tool_call_id": result.tool_calls[0]["id"],
            "content": price
        })
        result = await llm_with_tools.ainvoke(messages)

    messages.append({"role": "assistant", "content": result.content})
    print(messages[-1])

asyncio.run(main())
