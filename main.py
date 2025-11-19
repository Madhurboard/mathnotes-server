from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
import uvicorn
from apps.calculator.route import router as calculator_router
from constants import SERVER_URL, PORT, ENV

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(
    title="Math Canvas API",
    description="Backend API for Math Canvas drawing and calculation",
    version="1.0.0",
    lifespan=lifespan
)

allowed_origins = ['*'] if ENV == 'dev' else [
    "http://localhost:3000",
    "https://mathnotes.madhurpatil.me"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail, "status": "error"},
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={"message": "Validation error", "status": "error", "details": str(exc)},
    )

@app.get('/', tags=["health"])
async def root():
    return {"message": "Math Canvas API is running", "status": "success"}

@app.get('/health', tags=["health"])
async def health_check():
    return {"status": "healthy"}

app.include_router(calculator_router, prefix="/calculate", tags=["calculate"])

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=SERVER_URL,
        port=int(PORT),
        reload=(ENV == "dev"),
        log_level="info" if ENV == "prod" else "debug"
    )
