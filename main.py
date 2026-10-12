from js import Response

async def on_fetch(request, env, ctx):
    html_content = """
    <!DOCTYPE html>
    <html lang="fa" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>سایت پایتونی من</title>
        <style>
            body { 
                font-family: Tahoma, sans-serif; 
                text-align: center; 
                padding-top: 50px; 
                background: #f4f4f9; 
                color: #333; 
            }
            h1 { color: #f38020; }
        </style>
    </head>
    <body>
        <h1>سلام دنیا! 🚀</h1>
        <p>این سایت ساده با پایتون روی کلودفلر ورکر با موفقیت اجرا شد.</p>
    </body>
    </html>
    """
    
    # هدرها به صورت لیست دوال (Sequence) ارسال می‌شوند تا خطای نوع داده رفع شود
    return Response.new(
        html_content,
        headers=[("content-type", "text/html;charset=UTF-8")]
    )
