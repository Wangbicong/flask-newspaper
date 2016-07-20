from app import create_app, db

app = create_app()


@app.route('/')
def index():
    return 'Hello World!aawa'
app.run()
