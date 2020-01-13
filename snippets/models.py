from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# we'd also need to make sure that when the model is saved, that we populate the highlighted field, using the pygments
# code highlighting library.

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0])for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    # let's add a couple of fields. One of those fields wil be used to represent the user who created the code snippet.
    # The other field will be used to store the highlighted HTML representation of the code.
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()

    # also add a .save() custom method to ur model class

    def save(self, *args, **kwargs):
        """
        use the 'pymgents' library to crate a highlighted HTML
        representation of the code snippet.

        :param args:
        :param kwargs:
        :return:
        """

        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else{}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)

        super(Snippet, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created']

