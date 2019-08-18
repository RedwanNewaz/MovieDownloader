from app import app, IP_ADDRESS,PORT


if __name__ == "__main__":
    app.run(debug=True, host=IP_ADDRESS, port=PORT)