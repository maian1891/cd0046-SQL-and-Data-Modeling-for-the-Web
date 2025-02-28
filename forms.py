from datetime import datetime
from flask_wtf import FlaskForm as Form
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, BooleanField, IntegerField
from wtforms.validators import DataRequired, URL, ValidationError, Regexp
from enums import States, Genres

def is_facebook_url(form, field):
    if "facebook.com" not in field.data:
        raise ValidationError("URL must be a Facebook link.")

phone_regex = r'^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$'

class ShowForm(Form):
    artist_id = StringField(
        'artist_id'
    )
    venue_id = StringField(
        'venue_id'
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default= datetime.today()
    )

class VenueForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=States.items()
    )
    address = StringField(
        'address', validators=[DataRequired()]
    )
    phone = StringField(
        'phone', validators=[Regexp(phone_regex, 0, message="Invalid phone number format.")]
    )
    image_link = StringField(
        'image_link'
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired()],
        choices=Genres.items()
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL(), is_facebook_url]
    )
    website_link = StringField(
        'website_link'
    )

    seeking_talent = BooleanField( 'seeking_talent' )

    seeking_description = StringField(
        'seeking_description'
    )

class ArtistForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=States.items()
    )
    phone = StringField(
        'phone', validators=[Regexp(phone_regex, 0, message="Invalid phone number format.")]
    )
    image_link = StringField(
        'image_link'
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired()],
        choices=Genres.items()
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL(), is_facebook_url]
     )

    website_link = StringField(
        'website_link'
     )

    seeking_venue = BooleanField( 'seeking_venue' )

    seeking_description = StringField(
            'seeking_description'
     )

class ShowForm(Form):
    start_time = DateTimeField(
        'start_time', validators=[DataRequired()], default=datetime.today()
    )
    artist_id = IntegerField(
        'artist_id'
    )
    venue_id = IntegerField(
        'venue_id'
    )