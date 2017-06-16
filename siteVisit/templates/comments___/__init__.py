def get_model():
    from my_comment_app.models import CommentWithTitle
    return CommentWithTitle

def get_form():
    from my_comment_app.forms import CommentFormWithTitle
    return CommentFormWithTitle