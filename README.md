# Math Canvas Backend API

A high-performance FastAPI backend service that processes mathematical expressions and drawings using Google's Gemini API.

## 🚀 Features

- **Image Processing**: Analyzes hand-drawn mathematical expressions
- **Mathematical Computation**: Solves equations, expressions, and word problems
- **Variable Management**: Supports variable assignments and usage
- **RESTful API**: Clean, well-documented endpoints
- **Production Ready**: Optimized for deployment with proper error handling

## 📋 Prerequisites

- Python 3.11 or higher
- Google Gemini API key ([Get one here](https://aistudio.google.com/app/apikey))
- pip (Python package manager)

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd mathnotes-server
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
PORT=8000
ENV=dev
```

**Environment Variables:**
- `GEMINI_API_KEY`: Your Google Gemini API key (required)
- `PORT`: Server port (default: 8000)
- `ENV`: Environment mode (`dev` or `prod`)

## 🏃 Running the Server

### Development Mode

```bash
python main.py
```

The server will start at `http://localhost:8000` with auto-reload enabled.

### Production Mode

```bash
# Set environment to production
ENV=prod python main.py

# Or with Gunicorn (recommended)
pip install gunicorn
gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

## 📡 API Endpoints

### Health Check

```http
GET /
```

**Response:**
```json
{
  "message": "Math Canvas API is running",
  "status": "success"
}
```

### Health Status

```http
GET /health
```

**Response:**
```json
{
  "status": "healthy"
}
```

### Calculate Math Expression

```http
POST /calculate
```

**Request Body:**
```json
{
  "image": "data:image/png;base64,iVBORw0KGg...",
  "dict_of_vars": {
    "x": 5,
    "y": 10
  }
}
```

**Response:**
```json
{
  "message": "Image processed",
  "status": "success",
  "data": [
    {
      "expr": "2 + 2",
      "result": "4",
      "assign": false
    }
  ]
}
```

## 📦 Project Structure

```
mathnotes-server/
├── apps/
│   └── calculator/
│       ├── route.py          # API routes
│       └── utils.py          # Core logic
├── constants.py              # Configuration
├── main.py                   # Application entry point
├── schema.py                 # Pydantic models
├── requirements.txt          # Dependencies
├── .env.example              # Environment template
└── README.md                 # This file
```

## 🔧 Dependencies

- **FastAPI**: Modern web framework
- **Uvicorn**: ASGI server
- **Pillow**: Image processing
- **Pydantic**: Data validation
- **google-genai**: Gemini API client
- **python-dotenv**: Environment management

## 🐳 Docker Deployment

### Build Image

```bash
docker build -t math-canvas-backend .
```

### Run Container

```bash
docker run -d \
  -p 8000:8000 \
  -e GEMINI_API_KEY=your_key_here \
  -e ENV=prod \
  --name math-canvas-api \
  math-canvas-backend
```

### Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]
```

## 🌐 Deployment Options

### Render

1. Connect your GitHub repository
2. Select "Web Service"
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `python main.py`
5. Add environment variables
6. Deploy

### Railway

1. Connect GitHub repository
2. Add environment variables
3. Railway auto-detects Python and deploys

### AWS/GCP/Azure

Deploy using standard Python ASGI deployment methods with Uvicorn or Gunicorn.

## 🔒 Security Best Practices

- Keep your `.env` file secure and never commit it
- Use environment variables for all sensitive data
- Enable HTTPS in production
- Update `allowed_origins` in `main.py` for production domains
- Regularly update dependencies: `pip install --upgrade -r requirements.txt`

## 🐛 Troubleshooting

### API Key Issues

```bash
# Check if API key is set
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('API Key:', bool(os.getenv('GEMINI_API_KEY')))"
```

### Port Already in Use

```bash
# Change port in .env file
PORT=8001
```

### Import Errors

```bash
# Reinstall dependencies
pip install --force-reinstall -r requirements.txt
```

## 📊 Performance

- Handles concurrent requests efficiently
- Async/await for non-blocking operations
- Production-ready with Gunicorn workers
- Optimized image processing

## 🧪 Testing

```bash
# Test health endpoint
curl http://localhost:8000/health

# Test calculate endpoint
curl -X POST http://localhost:8000/calculate \
  -H "Content-Type: application/json" \
  -d '{"image":"data:image/png;base64,...","dict_of_vars":{}}'
```

## 📄 License

MIT License - feel free to use this project for personal or commercial purposes.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For issues and questions:
- Open an issue on GitHub
- Check existing documentation
- Review API responses for detailed error messages

## 🔄 Updates

To update dependencies:

```bash
pip install --upgrade -r requirements.txt
```

## ⚡ Quick Start Commands

```bash
# Setup
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
cp .env.example .env  # Add your API key

# Run
python main.py

# Test
curl http://localhost:8000/health
```

---

**Built with FastAPI and Gemini API** | **Production Ready** | **High Performance**
