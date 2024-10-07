

response_comment=requests.request("GET",url_comment)
response_post=requests.request("GET",url_post)
#recupération des posts sous forme de json
data_posts=json.loads(response_post.text)
#recupération de la partie data qui est un tableau
tab_posts=data_posts['data'];

for post in tab_posts:
    #each has id,message,created_time
    print(post)
    print(post['created_time'])








#print(response_post.text)
#print(response_comment.text.encode('utf8'))
data=json.loads(response_comment.text)
#Fac@if1==1@
# create object with only name,time,message
def get_comment(comment):
    return{
        'name':comment['from']['name'],
        'time':comment['created_time'],
        'message':comment['message']
    }


excel_data=list(map(get_comment,data['data']))
df=pd.DataFrame(excel_data)
df.to_csv('endpoints.csv', index=False)

#df.to_excel('comments.csv',index=False)



