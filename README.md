# Flask Webhook to REST API Bridge

This project is a simple Flask-based middleware that transforms incoming webhook requests into REST API calls. It accepts HTTP verb, endpoint, payload, and base URL dynamically via JSON.
## 🙌 Author
 TS : Tapomay Sanyal
## 🔧 Features

- Accepts `httpverb`, `endpoint`, `base_url`, and `content` in a JSON POST request.
- Forwards the request using the appropriate HTTP method.
- Returns the full response (status, headers, and body) from the target API.
- Modular and easily deployable (Replit, Render, BTP, etc).

## 📦 JSON Request Format

Endpoint: POST ,
          https://<the URL of the flask-app whereever you deploy>/webhook_2_any_rest
          Replace `<the URL of the flask-app whereever you deploy>` with the actual URL where your Flask app is deployed (e.g., `https://webhook-2-rest.onrender.com`) when it is deployed on Render!!.

```json
{
  "httpverb": "", 
  "endpoint": "",
  "baseurl": "",
  "content": {
  }
}
