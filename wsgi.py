from app import app

print("hello from wsgi.py")

if __name__ == "__main__":
    app.run(debug=True)
