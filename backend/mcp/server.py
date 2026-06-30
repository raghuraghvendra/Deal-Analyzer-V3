from backend.mcp.tools.company_policy import CompanyPolicyTool

class MCPServer:

    def __init__(self):

        self.tools = {}

        self.register_tool(
            "company_policy",
            CompanyPolicyTool()
        )

    def register_tool(
        self,
        name,
        tool
    ):

        self.tools[name] = tool

    def execute(
        self,
        tool_name,
        **kwargs
    ):

        if tool_name not in self.tools:
            raise ValueError(
                f"Tool '{tool_name}' not found."
            )

        tool = self.tools[tool_name]

        return tool.run(**kwargs)