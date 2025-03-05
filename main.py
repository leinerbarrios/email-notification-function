import functions_framework
import resend
import os

from flask import jsonify

resend.api_key = os.environ["RESEND_API_KEY"]

@functions_framework.http
def send_email(request):
    body = request.get_json()
    email = body["email"]
    message = body["message"]
    
    try:
        params: resend.Emails.SendParams = {
            "from": "sancochoft@devsco.tech",
            "to": [email, "lj.barrios@uniandes.edu.co"],
            "subject": "Email Notification",
            "text": message,
        }

        r = resend.Emails.send(params)
        return jsonify(r)

    except Exception as e:
        return jsonify({"error": str(e)})