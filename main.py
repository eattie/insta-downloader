import instaloader
from instaloader import Profile

def download_instagram_videos(profile_name, download_folder, max_count):
    """Downloads a limited number of the most recent videos from an Instagram profile.
    """

    L = instaloader.Instaloader()

    L.login("alanetai2332","alanetai!")

    profile = Profile.from_username(L.context, profile_name)

    count = 0
    for post in profile.get_posts():
        if count > max_count:
            break
        print(post.caption)
        count+=1
        # L.download_post(post, target=profile.username)

if __name__ == "__main__":
    profile_to_download = "vozzey"
    download_path = "insta-videos" 
    max_posts = 1

    download_instagram_videos(profile_to_download, download_path, max_posts)
