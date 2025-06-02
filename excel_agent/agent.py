from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import os
from dotenv import load_dotenv
from excel_agent.tools import read_excel
from pydantic import BaseModel, Field
from google.adk.tools.mcp_tool.mcp_toolset import (
    MCPToolset,
    StdioServerParameters,
    SseServerParams,
)

load_dotenv()

model = LiteLlm(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_base=os.getenv("AZURE_OPENAI_API_ENDPOINT"),
)


# --- Define Output Schema ---
class ResponseContent(BaseModel):
    response: str = Field(description="處理Excel的回應")


root_agent = Agent(
    name="excel_agent",
    model=model,
    description="你是個Excel專家，可以幫助使用者處理Excel文件",
    instruction="""
        1. 你是一個Excel專家，可以幫助使用者處理Excel文件。
        2. 你可以讀取Excel檔案名稱，並且讀取Excel檔案的內容。
        3. 你可以讀取工作表名稱。
        4. 如果沒有提供路徑檔名，則使用環境變數FILE_PATH的值為路徑。
        5. 如果沒有提供工作表名稱，則讀取工作表1。
    """,
    tools=[
        read_excel,
        # MCPToolset(
        #     connection_params=SseServerParams(
        #         url="http://localhost:3001/sse",
        #     )
        # ),
    ],
    # output_schema=ResponseContent,  # if output_schema is set, tools must be empty
    # output_key="response",
    # tools=[  # haris-musa/excel-mcp-server
    #     MCPToolset(
    #         connection_params=StdioServerParameters(
    #             command="uvx",
    #             args=["excel-mcp-server", "stdio"],
    #         )
    #     ),
    # ],
    # tools=[ # negokaz/excel-mcp-server
    #     MCPToolset(
    #         connection_params=StdioServerParameters(
    #             command="npx",
    #             args=["--yes", "@negokaz/excel-mcp-server"],
    #         )
    #     ),
    # ],
)
