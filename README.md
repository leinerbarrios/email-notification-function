# Email Notification

This is a simple example of a function that sends an email using the [Resend API](https://resend.com/docs/introduction).

## Prerequisites

- Install [Cloud SDK](https://cloud.google.com/sdk/docs/install)
- Install [Python 3.9](https://www.python.org/downloads/)
- Generate a Resend API key [here](https://resend.com/api-keys).

## Running locally

### 1. Create a virtual environment

```bash
python3 -m venv env
```

### 2. Activate the virtual environment

```bash
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Deploying function to Google Cloud Run

```bash
gcloud run beta deploy email-notification --source . --function send_email --region us-central1 --allow-unauthenticated --memory 256M --timeout 60 --min-instances 0 --max-instances 1 --set-env-vars RESEND_API_KEY=your_resend_api_key
```

Using Cloud Functions

```bash
gcloud functions deploy email-notification --entry-point send_email --runtime python39 --trigger-http --allow-unauthenticated --memory 256MB --region us-central1 --timeout 60 --min-instances 0 --max-instances 1 --cpu 1 --set-env-vars RESEND_API_KEY=your_resend_api_key
```

## Use

To send an email, make a POST request to the `/email-notification` endpoint with the following JSON body:

```json
{
  "email": "your_email@example.com",
  "message": "Hello, world!"
}
```