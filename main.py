import device, website

if __name__ == '__main__':
    app = website.create_app()
    app.run(host='0.0.0.0', debug=True)