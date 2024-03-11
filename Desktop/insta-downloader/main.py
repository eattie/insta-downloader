import instaloader
import os

def download_instagram_videos(profile_name, download_folder, max_count):
    """Downloads a limited number of the most recent videos from an Instagram profile.
    """

    L = instaloader.Instaloader()

    L.login(vozzey2,Laugh123!)

    posts = L.get_profile(profile_name).get_posts()

    count = 0
    for post in posts:
        if count >= max_count:
            break

        # Download if it's a video
        if post.is_video:
            L.download_post(post, target=download_folder)
            count += 1

if __name__ == "__main__":
    profile_to_download = "natgeo"
    download_path = "insta-videos" 
    max_posts = 5  # Download the 5 most recent videos 

    download_instagram_videos(profile_to_download, download_path, max_posts)
