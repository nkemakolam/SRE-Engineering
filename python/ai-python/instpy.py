import instaloader
 
# Creating an instance of the Instaloader class
loader = instaloader.Instaloader()
 
 # Load the profile of the target user
profile = instaloader.Profile.from_username(loader.context, 'benyjewels')

# Print user information
print("Username:", profile.username)
print("Followers:", profile.followers)
print("Following:", profile.followees)
print("Bio:", profile.biography)
 
for post in profile.get_posts():
    loader.download_post(post, target=profile.username)
  
    
   