from langchain_core.callbacks import CallbackManagerForToolRun
from langchain_core.tools import BaseTool, BaseToolkit
from pydantic import BaseModel, Field

try:
    from swcpy import SWCClient, SWCConfig
    from swcpy.swc_client import League, Team
except ImportError:
    raise ImportError("swcpy is not installed. Please install it.")

config = SWCConfig(backoff=False)
local_swc_client = SWCClient(config)


class HealthCheckInput(BaseModel):
    pass


class HealthCheckTool(BaseTool):
    name: str = "HealthCheck"
    description: str = "useful to check if the API is running before you make other calls"
    args_schema: type[HealthCheckInput] = HealthCheckInput
    return_direct: bool = False

    def _run(self, run_manager: CallbackManagerForToolRun | None = None) -> str:
        """Use the tool to check if the API is running."""
        health_check_response = local_swc_client.get_health_check()
        return health_check_response.text


class LeaguesInput(BaseModel):
    league_name: str | None = Field(default=None, description="league name. Leave blank or None to get all leagues.")


class ListLeaguesTool(BaseTool):
    name: str = "ListLeagues"
    description: str = "get a list of leagues from SportsWorldCentral. " "Leagues contain teams if they are present."
    args_schema: type[LeaguesInput] = LeaguesInput
    return_direct: bool = False

    def _run(self, league_name: str | None = None, run_manager: CallbackManagerForToolRun | None = None) -> list[League]:
        """Use the tool to get a list of leagues from SportsWorldCentral."""
        # Call the API with league_name, which could be None
        list_leagues_response = local_swc_client.list_leagues(league_name=league_name)
        return list_leagues_response


class TeamsInput(BaseModel):
    team_name: str | None = Field(
        default=None, description="Name of the team to search for. Leave blank or None to get all teams."
    )
    league_id: int | None = Field(
        default=None,
        description=(
            "League ID from a league. You must provide a numerical League ID. "
            "Leave blank or None to get teams from all leagues."
        ),
    )


class ListTeamsTool(BaseTool):
    name: str = "ListTeams"
    description: str = (
        "Get a list of teams from SportsWorldCentral. Teams contain players if they are "
        "present. Optionally provide a numerical League ID to filter teams "
        "from a specific league."
    )
    args_schema: type[TeamsInput] = TeamsInput
    return_direct: bool = False

    def _run(
        self, team_name: str | None = None, league_id: int | None = None, run_manager: CallbackManagerForToolRun | None = None
    ) -> list[Team]:
        """Use the tool to get a list of teams from SportsWorldCentral."""
        list_teams_response = local_swc_client.list_teams(team_name=team_name, league_id=league_id)
        return list_teams_response


class SportsWorldCentralToolkit(BaseToolkit):
    def get_tools(self) -> list[BaseTool]:
        """Return the list of tools in the toolkit."""
        return [HealthCheckTool(), ListLeaguesTool(), ListTeamsTool()]
