from django.db import models
from django.contrib.auth.models import User

class UploadedFile(models.Model):
	MEDIA_TYPES = (
		('Image', 'Image'),
		('Video', 'Video'),
		('Audio', 'Audio'),
		('ChatLog','ChatLog'),
	)

	user = models.ForeignKey(User, editable = False)
	file_path = models.FileField(upload_to = "sharedfiles")
	file_name = models.CharField(u"File Name", max_length = 500)
	pub_date = models.DateTimeField(u"Date Published", auto_now_add = True)
	file_type = models.CharField(u"File Type", blank = True, max_length = 20, choices = MEDIA_TYPES)
	is_public = models.BooleanField()
	share_to = models.ForeignKey(User, related_name = "share_to")
