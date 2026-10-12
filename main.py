from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <!DOCTYPE html>
    <html lang="fa" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>سایت پایتونی من</title>
        <style>
            body { font-family: Tahoma, sans-serif; text-align: center; padding-top: 50px; background: #f4f4f9; color: #333; }
            h1 { color: #f38020; }
        </style>
    </head>
    <body>
        <h1>سلام دنیا! 🚀</h1>
        <p>این سایت با پایتون (FastAPI) روی کلودفلر ورکر اجرا شده است.</p>
    </body>
    </html>
    """