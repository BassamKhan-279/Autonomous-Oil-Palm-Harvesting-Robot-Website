# In login_server.py

async def admin_page(request):
    """
    Serves the admin.html page with explicit content type, 
    but only after verifying admin privileges.
    """
    await require_admin(request) # Protect this page

    admin_path = WEB_DIR / "admin.html"
    
    try:
        # 🚨 CRITICAL FIX: Read the file content and set the MIME type manually
        with open(admin_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        return web.Response(
            text=content,
            content_type='text/html' # Force the browser to render as HTML
        )
    except FileNotFoundError:
        return web.Response(text="Admin HTML file not found.", status=500)
    except Exception as e:
        # If the file exists but the content is corrupted (e.g., Unicode error)
        print(f"Error serving admin page: {e}")
        return web.Response(text="Error processing admin page content.", status=500)
