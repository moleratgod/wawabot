from requests import get
from bs4 import BeautifulSoup as BS
import time
from json import loads


def getGithub(username):
    link = f"https://api.github.com/users/{username}"
    resp = get(link)

    if resp.status_code == 200:
        begin = time.time()

        soup = BS(resp.text, "html.parser")


        all_data = loads(str(soup))

        end = time.time()

        slice1 = all_data["created_at"].replace("T", " ")
        final_sclice = slice1.replace("Z", " ")

        all_data["resp_time"] = str(round(end - begin, 5)) + "s"
        all_data["created_at"] = final_sclice[0:len(final_sclice)-1]
        

        return all_data

def profileParser(username):
    fd = getGithub(username)
    formatted_profile = f"""Username: {fd["login"]}
Name: {fd["name"]}
Company: {fd["company"]}
Bio: {fd["bio"]}
Account Creation: {fd["created_at"]}
Most Recent Update: {fd["updated_at"]}

{fd["html_url"]}"""
    
    return (formatted_profile, fd["avatar_url"])

if __name__ == "__main__":
    profile = profileParser("moleratgod")
    print(profile[1])