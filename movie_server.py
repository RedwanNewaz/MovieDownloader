from app import app, IP_ADDRESS

if __name__ == "__main__":
    app.run(debug=True, host=IP_ADDRESS)