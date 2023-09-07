from flask import Flask, render_template, redirect, url_for
from forms import AddressForm  # Impor the form class from forms.py
import googlemaps 

app = Flask(__name__)
app.config['AIzaSyDxc4FcGZNlTYYy92HlO7QjFHkHW6-8TyQ'] = 'AIzaSyDxc4FcGZNlTYYy92HlO7QjFHkHW6-8TyQ'  # Replacing with a secret key for form security
gmaps = googlemaps.Client(key = 'AIzaSyDxc4FcGZNlTYYy92HlO7QjFHkHW6-8TyQ')
@app.route('/address', methods=['GET', 'POST'])
def address():
    form = AddressForm()
    if form.validate_on_submit():
        # Handling form submission (save data to the database, etc.)
        street_number = form.street_number.data
        area = form.area.data

        # code here to process and store the address data
        # we'll just print it to the console until update
        print(f'Street Number: {street_number}, Area: {area}')
        address = f'{street_number}, {area}'
        geocode_result = gmaps.geocode(address)

        if geocode_result:
            # Address is valid; process it in the database
        
            print(f'Validated Address: {geocode_result[0]["formatted_address"]}')
            return 'Address submitted successfully!'
        else:
            # Address is not valid
            return 'Address validation failed. Please check your address.'


    return render_template('address_form.html', form=form)
@app.route("/")
def index():
    return "<h1>This is the Welcome page</h1>"
    
@app.route('/submit_address', methods=['POST'])
def submit_address():
    form = AddressForm()

    if form.validate_on_submit():
        street_number = form.street_number.data
        area = form.area.data

        # Use Google Maps Geocoding API to validate the address
        address = f'{street_number}, {area}'
        geocode_result = gmaps.geocode(address)

        if geocode_result:
            # Address is valid; you can proce it in the database
        
            print(f'Validated Address: {geocode_result[0]["formatted_address"]}')
            return 'Address submitted successfully!'

        else:
            # Address is not valid
            return 'Address validation failed. Please check your address.'

    return render_template('address_form.html', form=form)
if __name__ == '__main__':
    app.run()
