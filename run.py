from aita import create_app

if __name__ == "__main__":
    # Development, Testing, Production
    app = create_app('Development') 
    app.run()
