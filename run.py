import aita

if __name__ == "__main__":
    # Development, Testing, Production
    app = aita.create_app('Development') 
    app.run()
