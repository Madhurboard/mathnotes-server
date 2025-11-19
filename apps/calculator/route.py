from fastapi import APIRouter, HTTPException
import base64
from io import BytesIO
from apps.calculator.utils import analyze_image
from schema import ImageData
from PIL import Image

router = APIRouter()

@router.post("")
async def run(data: ImageData):
    try:
        if not data.image or "," not in data.image:
            raise HTTPException(status_code=400, detail="Invalid image data URL")

        try:
            image_b64 = data.image.split(",", 1)[1]
            image_data = base64.b64decode(image_b64)
        except Exception:
            raise HTTPException(status_code=400, detail="Failed to decode base64 image")

        try:
            image_bytes = BytesIO(image_data)
            image = Image.open(image_bytes)
            image.load()
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid image format")

        responses = analyze_image(image, dict_of_vars=data.dict_of_vars or {})
        out = []
        for r in responses or []:
            out.append(r)

        return {"message": "Image processed", "data": out, "status": "success"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {e}")

