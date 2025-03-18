from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# In-memory data storage
feedback_list = []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        username = request.form.get("username")
        comments = request.form.get("comments")
        
        # Store feedback in memory
        feedback_list.append({
            "username": username,
            "comments": comments
        })
        
        return render_template("form_result.html", 
                             username=username, 
                             comments=comments)
    return render_template("feedback.html")

@app.route("/all-feedback")
def show_feedback():
    return render_template("all_feedback.html", feedback=feedback_list)

@app.route("/api/feedback")
def feedback_api():
    return jsonify(feedback_list)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)