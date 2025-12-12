from fastapi import FastAPI
import uvicorn
from src.press_button import press_button

app = FastAPI()

@app.post("/press_button")
def press_button_endpoint():
    """Endpoint to press the button via servo motor."""
    try:
        press_button()
        return {"status": "success", "message": "Button pressed successfully"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9448)
