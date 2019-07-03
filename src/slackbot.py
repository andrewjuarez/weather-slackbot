import requests
import slack

def query_weather():
    WEATHER_API_KEY = '5e3d647341040856d9ae2d68fe430d42'
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Irvine&units=imperial&APPID=" + WEATHER_API_KEY)
    response = response.json()
    return str(response['main']['temp']) + "F"


@slack.RTMClient.run_on(event='message')
def say_hello(**payload):
    print("payload:", payload)
    data = payload['data']
    web_client = payload['web_client']
    rtm_client = payload['rtm_client']
    try:
        if 'hello' in data['text']:
            channel_id = data['channel']
            thread_ts = data['ts']
            user = data['user']

            web_client.chat_postMessage(
                channel=channel_id,
                text=f"Good morning San Diago!",
                thread_ts=thread_ts
            )
        elif "temp" in data['text']:
            channel_id = data['channel']
            thread_ts = data['ts']
            user = data['user']

            web_client.chat_postMessage(
                channel=channel_id,
                text=f"It is currently " + query_weather() + " in Irvine.",
                thread_ts=thread_ts
            )
        else:
            channel_id = data['channel']
            thread_ts = data['ts']
            user = data['user']

            web_client.chat_postMessage(
                channel=channel_id,
                text=f"What are you trying to say?",
                thread_ts=thread_ts
            )
    except KeyError:
        pass

slack_token = 'xoxb-620885944051-641418642384-lDgQqEc48j4z5JuHfndrQo1U'
rtm_client = slack.RTMClient(token=slack_token)
print("Starting client")
rtm_client.start()

