from fastapi import APIRouter

from app.config import config
from app.service.store.google_sheets import GoogleSheet_interactions

router = APIRouter(
    prefix="/google_sheets",
    tags=["google_sheets"],
)

SHEET_INTERACTION = GoogleSheet_interactions(
    CREDENTIALS_FILE=config.SERVICE_ACCOUNT_CREDENTIALS_PATH,
    spreadsheetId=config.SPREADSHEET_ID,
)


@router.get("/get_data/{List_name}/{Position}")
async def get_data(List_name: str, Position: str):
    return SHEET_INTERACTION.extract(List=List_name, Position=Position)
