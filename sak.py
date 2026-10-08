from flask import Flask, render_template_string

app = Flask(__name__)

# HTML template embedded directly into the Python file for simplicity
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>College Notice Board</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background-color: #f4f4f9; color: #333; }
        header { background-color: #003366; color: white; padding: 20px; text-align: center; border-radius: 5px; }
        .container { max-width: 800px; margin: 20px auto; background: white; padding: 20px; border-radius: 5px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        .notice { border-left: 5px solid #003366; background: #eef4fa; padding: 15px; margin-bottom: 15px; border-radius: 0 5px 5px 0; }
        .date { font-size: 0.85em; color: #666; font-weight: bold; }
        footer { margin-top: 30px; text-align: center; font-size: 0.9em; color: #555; border-top: 1px solid #ccc; padding-top: 10px; }
    </style>
</head>
<body>
    <header>
        <h1>Apex Institute of Technology</h1>
        <h2>Department of Computer Science & Engineering</h2>
    </header>
    <div class="container">
        <h3>Current Notices</h3>
        <div class="notice">
            <div class="date">October 8, 2026</div>
            <p><strong>End Semester Examinations:</strong> The final theory examinations will commence from November 16, 2026. Hall tickets can be downloaded next week.</p>
        </div>
        <div class="notice">
            <div class="date">October 6, 2026</div>
            <p><strong>Hackathon Registration:</strong> Registrations for the Annual Inter-College Hackathon close on October 15. Submit your team details on the student portal.</p>
        </div>
        <div class="notice">
            <div class="date">October 1, 2026</div>
            <p><strong>Placement Drive:</strong> TechCorp will conduct a virtual campus recruitment drive for final-year students on October 12, 2026.</p>
        </div>
    </div>
    <footer>
        <p>Contact Information: support@apexinstitute.edu | Ph: +1 (555) 019-2834</p>
    </footer>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    # Bind to 0.0.0.0 so it can accept external requests inside the container
    app.run(host='0.0.0.0', port=5000)
