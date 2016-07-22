from app import create_app, db

app = create_app()

# app.run(host='0.0.0.0')
app.run(port=80)