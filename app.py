from flask import Flask, request, render_template

app = Flask('SoundCloud Recommender')

@app.route('/')
def index():
  return "Hello world"

if __name__ == '__main__':
  app.run(debug=True)
