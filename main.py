from webserver import keep_alive
import requests

channelID = PUT THE CHANNEL ID
headers = {
    "989512298068594748":
    "OTkxNjA3Njk4OTQyNTk5MjYw.GojeAy.JyMrCDgSwHS8PHbuiNO9PS4A1cAKx8EOW7PQlg"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
