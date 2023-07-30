import apiclient
import httplib2
from oauth2client.service_account import ServiceAccountCredentials

from .store import Store_interaction


class GoogleSheet_interactions(Store_interaction):
    spreadsheetId: str
    service: "apiclient"
    credentials: ServiceAccountCredentials

    def __init__(self, CREDENTIALS_FILE: str, spreadsheetId: str):
        self.spreadsheetId = spreadsheetId

        # Auth
        self.credentials: ServiceAccountCredentials = (
            ServiceAccountCredentials.from_json_keyfile_name(
                CREDENTIALS_FILE,
                [
                    "https://www.googleapis.com/auth/spreadsheets",
                    "https://www.googleapis.com/auth/drive",
                ],
            )
        )
        httpAuth = self.credentials.authorize(httplib2.Http())
        self.service = apiclient.discovery.build("sheets", "v4", http=httpAuth)

    def __grant_permission(self, email: str):
        driveService = apiclient.discovery.build("drive", "v3", http=httpAuth)
        driveService.permissions().create(
            fileId=self.spreadsheetId,
            body={"type": "user", "role": "writer", "emailAddress": email},
            fields="id",
        ).execute()

    def extract(self, List: str, Position: str):
        spreadsheet = (
            self.service.spreadsheets().get(spreadsheetId=self.spreadsheetId).execute()
        )
        sheetsList: list = spreadsheet.get("sheets")
        sheetsList = [sheet["properties"]["title"] for sheet in sheetsList]
        if List not in sheetsList:
            return []

        ranges = [f"{List}!{Position}"]
        results = (
            self.service.spreadsheets()
            .values()
            .batchGet(
                spreadsheetId=self.spreadsheetId,
                ranges=ranges,
                dateTimeRenderOption="FORMATTED_STRING",
            )
            .execute()
        )

        sheet_values = results["valueRanges"][0]["values"]

        return sheet_values

    def put(self, data, position):
        return True

    def get_free_slots(self) -> dict:
        return {}
