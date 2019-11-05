from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__, template_folder = 'templates')

'''
# OUR MOCK ARRAY OF PROJECTS
playlists = [
    {'title': 'Cat Videos', 'description': 'Cats acting weird'},
    {'title': '80\'s Music', 'description': 'Don\'t stop believing!'}
]
'''

# file:///fortune_results?name=Parker&concentration=DS&birthday=1994-12-05&concentration=logs


@app.route('/')
def playlists_index():
    # find() method returns an iterable of all playlists in our database
    return render_template('fortune.html')


@app.route('/fortune_results')
def fortuneTelling():
    name = request.args.get('name')
    concentration = request.args.get('concentration')
    birthday = request.args.get('birthday')
    hobby = request.args.get('hobby')

    if concentration == 'Mobile':
        concentration = 'Visual Wonder'
        pass
    elif concentration == 'BEW':
        concentration = 'Modern Engineering Marvels'
        pass
    elif concentration == 'FEW':
        concentration = 'Public Work Beautification'
        pass
    elif concentration == 'DS':
        concentration = 'Mapping of Modern Meaning'
        pass

    """form element will be accessed via index on the fortuneTell page"""
    fortune = [
        name,
        concentration,
        birthday,
        hobby
    ]

    return render_template('fortuneTell.html', fortune=fortune)
