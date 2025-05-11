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

Endpoint: `POST /webhook_2_any_rest`

```json
{
  "httpverb": "GET/POST/PUT/DELETE", 
  "endpoint": "THE RESOURCE YOU WANT TO ADDRESS",
  "base_url": "BASE URL OF YOUR REST API",
  "content": {
    JSON with The Usual BODY that you would have used to carry out the respective REST activity!
  }
}
