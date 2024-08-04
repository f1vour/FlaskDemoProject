#!C:\Users\ka_ndi\AppData\Roaming\Python\Python310\Scripts\venv\Scripts\python.exe
print("Content-Type: text/html\n")

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
