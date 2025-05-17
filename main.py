from mcp.server.fastmcp import FastMCP

mcp = FastMCP("sample_server")

@mcp.tool()
def question(question: str) -> str:
    """
    Answers any question.
    """

    return "42"

if __name__ == "__main__":
    mcp.run(transport="sse")
