from django.db import models


class ArticlePlugin(models.Model):
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


class Subscription(models.Model):
    subscription_id = models.AutoField(primary_key=True)
    send_emails = models.BooleanField(default=True)


class ArticleSubscription(ArticlePlugin, Subscription):
    def __unicode__(self):
        return u"Subscription!"
