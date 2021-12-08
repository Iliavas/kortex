def create_profile(sender, **kwargs):
    if kwargs["created"]:
        instance = kwargs["instance"]
        Profile.objects.create(name=kwargs["instance"], user=kwargs["instance"])
