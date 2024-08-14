from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField(blank=True, null=True)
    text_input = models.TextField(blank=True, null=True)
    file_name = models.CharField(max_length=100, blank=True, null=True)
    summary_result = models.TextField(blank=True, null=True) # 번역 전 결과 (기본 결과)
    translation_result = models.TextField(blank=True, null=True) # 번역 후 결과
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.created_at}"