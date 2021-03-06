from flask import Flask, render_template

app = Flask(
    __name__,
    instance_relative_config=False,
    template_folder="templates",
    static_folder="static"
)


@app.route('/')
def hello():  
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
