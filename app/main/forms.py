from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required, Email, Length

class BlogForm(FlaskForm):
    title = StringField('Title', validators = [Required()])
    text = TextAreaField('Blog',validators = [Required()])
    category = SelectField('Category', choices = [('cuisine', 'Cuisine'),('voyage','Voyage'), ('health','Health'),('empower','Empowerment')], validators = [Required()])
    submit = SubmitField('Post')


