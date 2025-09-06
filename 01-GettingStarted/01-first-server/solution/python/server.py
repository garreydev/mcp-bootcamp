# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server instance
mcp = FastMCP("First MCP Server")

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    greetings = f"Hello, {name}!"
    return greetings.replace("%20", " ")

# Add a prompt for translating text to Japanese
@mcp.prompt()
def translation_ja(txt: str) -> str:
    """Translating to Japanese"""
    return f"Please translate this sentence into Japanese:\n\n{txt}"

# Main execution block - this is required to run the server
if __name__ == "__main__":
    mcp.run()
