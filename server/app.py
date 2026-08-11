from flask import Flask

existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

app=Flask(__name__) # creates the flask app

@app.route('/')
def home():
    return f'Welcome to Flatiron Cars'

@app.route('/<model>')
def model(model):
    for key in existing_models:
        if model==key:
            return f'Flatiron {model} is in our fleet!'
        else:
            return f'No models called {model} exists in our catalog'
    

if __name__=='__main__':
    app.run(debug=True)