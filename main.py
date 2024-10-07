import requests
import os

import pandas as pd
import json
import functions_framework
from datetime import datetime, timedelta

page_id='61565547791830'
post_id='122103804986518259'
access_token='EABkQ1QbrK6wBOxH2Oyb4zaM7urgRlCBv4eHrOrQMLGSEdDwW68lL2IEAYZAe6FXWqQXP3bF1dNo2gYCpVm33VS7I70qnZCIWZAwpQ63xmPSV3bvJCdkpnLSpgjUeuKxY9ZCSIZAl8if2d2c9JIZBlSwKQmKSJCbmZAl7UwluxtXH3U7Fgze63UP8cy43l4y11OB'
#url_comment= f'https://graph.facebook.com/v20.0/{page_id}_{post_id}/comments?access_token={access_token}'

436658636193491_122103804986518259
url_post=f'https://graph.facebook.com/v17.0/me/posts'


params = {
    'access_token': access_token,
}

all_posts = []
while url_post:
    response = requests.get(url_post, params=params)
    data = response.json()
    all_posts.extend(data.get('data', []))
    url_post = data.get('paging', {}).get('next')


# Number of days to subtract
n = 7
# Subtract n days from the current date and time
start_date = datetime.now() - timedelta(days=n)
end_date=datetime.now() 


# Filter posts by created_time
filtered_posts = [
    post for post in all_posts
    if start_date <= datetime.strptime(post['created_time'], '%Y-%m-%dT%H:%M:%S+0000') <= end_date
]

# Print filtered posts
all_comments=[]
for post in filtered_posts:
    post_id=post['id']
    #Pour chaque commentaire
    url_comment= f'https://graph.facebook.com/v20.0/{post_id}/comments'
    while url_comment:
        response=requests.get(url_comment,params=params)
        data = response.json()
        all_comments.extend(data.get('data', []))
        url_comment = data.get('paging', {}).get('next')

    #post attachment
    url_attachment=f'https://graph.facebook.com/v20.0/{post['id']}/attachments'
    response=requests.get(url_attachment,params=params)
    data=response.json()
    for attachment in data.get('data'):
        url=attachment['url']
        print(attachment['media']['image']['src'])


#print(all_comments)
df=pd.DataFrame(all_comments)
df.to_csv('comments.csv', index=False)


























