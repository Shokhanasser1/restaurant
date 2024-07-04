from users.models import Profile

profile = Profile.objects.first()
print(profile.bio)

print("Hello world")