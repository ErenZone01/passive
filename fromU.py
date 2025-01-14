from socialscan.util import Platforms, sync_execute_queries
import Displaye
import requests
def search_profile(username):
    username = username.lstrip("@")  # Supprimer le @ au début
    youtube = f"http://www.youtube.com/{username}"
    queries = [username]
    platforms = [Platforms.TUMBLR , Platforms.INSTAGRAM, Platforms.TWITTER, Platforms.REDDIT]
    results = sync_execute_queries(queries, platforms)
    text = ""
    c = 0
    for result in results:
        #print(f"{result.query} on {result.platform}: {result.message} (Success: {result.success}, Valid: {result.valid}, Available: {result.available})")
        platform = result.platform
        if (result.success == True and result.valid == True and result.available == False):
            text += f"{platform}: Yes\n"
            print(f"{platform}: Yes")
        else :
            text+= f"{platform}: No\n"
            print(f"{platform}: No")
    request = requests.get(youtube)
    if request.status_code == 200 :
        text += "Youtube: Yes\n"
        print(f"Youtube: Yes")
    else:
        text += "Youtube: No\n"
        print(f"Youtube: No")
    Displaye.Display(text)
