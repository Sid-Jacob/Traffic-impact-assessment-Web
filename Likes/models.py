from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User


#likes number model
class Likes(models.Model):
    #content type
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(ct_field="content_type",
                                       fk_field="object_id")

    #likes number
    likes_num = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s:%s(%s)' % (self.content_type, self.object_id,
                               self.likes_num)


#likes detail recode
class LikesDetail(models.Model):
    likes = models.ForeignKey(Likes, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_like = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pub_date']
