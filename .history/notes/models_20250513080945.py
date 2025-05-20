from django.db import models

class Note(models.Model):
  text = models.TextField()


  def __str__(self):
    return self.text[:10] + "...."
  

  Black Formatter
  ES7 React/Redux
  ESLint
  HTML CSS Support
  Path Intellisense
  Prettier - Code formatter
  Pylance
  Python
  
