import logging

from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

from core.config import setup_logging, templates
from schemas.message import MessageResponse, MessageSchema

setup_logging()

app = FastAPI()

message_counter = 0


@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    global message_counter
    await websocket.accept()
    logging.info("Новое WebSocket соединение установлено")
    try:
        while True:
            data = await websocket.receive_json()
            message = MessageSchema(**data)

            message_counter += 1

            response = MessageResponse(number=message_counter, text=message.text)

            await websocket.send_json(response.model_dump())
            logging.info(f"Отправлен ответ №{message_counter}")

    except WebSocketDisconnect:
        logging.info("Клиент отключился")
    except Exception as e:
        logging.error(f"Ошибка: {e}")
