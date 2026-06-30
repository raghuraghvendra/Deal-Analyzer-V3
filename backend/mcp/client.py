from backend.mcp.server import MCPServer


class MCPClient:

    def __init__(self, server: MCPServer):

        self.server = server

    def use_tool(
        self,
        tool_name,
        **kwargs
    ):

        return self.server.execute(
            tool_name,
            **kwargs
        )