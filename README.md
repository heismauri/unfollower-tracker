# Unfollower Tracker for Instagram
Find who is not following you back using this Python script.

# Usage
1. Request your Instagram Data, [here](https://help.instagram.com/181231772500920) is a tutorial on how to do it. IMPORTANT: The requested format should be JSON. Depending on your account this might take some hours.
2. Download your Instagram Data, and find the folder `followers_and_following`. Then copy and paste that folder on the main directory.
3. Run this script by using the "Start" button on your VSCode or typing `python unfollower-tracker.py` on your terminal.

# Whitelisting
You can whitelist some account you would like to keep following (artists, stores, events, etc) and not be shown on your non-followerback list. You will have to create a file called `whitelist.json`. You can see the file `whitelist.example.json` to know how to format it.
