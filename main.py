from website import create_app


app = create_app()

def run_flask():
    app.run(debug=True)


if __name__ == '__main__':

    run_flask()
