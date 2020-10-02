from flask import Flask, render_template

app = Flask(__name__)

all_posts =[
    {
        'title':'Post1',
        'content':'thi is content of post1',
        'author': 'Fanta'
    },
    {
        'title':'Post2',
        'content':'thi is content of post2'
    }
]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/posts')
def posts():
    return render_template('posts.html', posts=all_posts)

@app.route('/home/users/<string:name>/posts/<int:id>')
def hello(name,id):
    return "Hello, " + name + ", your id is:"  + str(id)

@app.route('/onlyget', methods=['GET'])
def get_only():
    return "You can only get this webpage"


if __name__ == "__main__":
    app.run(debug=True)