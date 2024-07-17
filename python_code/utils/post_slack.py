import requests




def post_to_slack(webhook_url, message):
    response = requests.post(webhook_url, json={"text": message})
    if response.status_code != 200:
        raise ValueError(f"Request to Slack returned an error {response.status_code}, the response is:\n{response.text}")
