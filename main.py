from fastapi import FastAPI
from pydantic import BaseModel

from core.validator import validate_request
from core.dispatcher import dispatch_command

app = FastAPI()


class CommandRequest(BaseModel):
    command: str
    confidence: float


@app.get("/")
def home():
    return {
        "message": "Synapti Mesh Backend Running"
    }


@app.post("/command")
def process_command(data: CommandRequest):

    is_valid, validation_message = validate_request(
        data.command,
        data.confidence
    )

    if not is_valid:
        return {
            "success": False,
            "message": validation_message
        }

    success, execution_message = dispatch_command(
        data.command
    )

    return {
        "success": success,
        "message": execution_message
    }