import instaloader

insta = instaloader.Instaloader()
defaultpicture = input("Enter Instagram Username You Wish To Download : ")

insta.download_profile(defaultpicture, profile_pic_only= True)
