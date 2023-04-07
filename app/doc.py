class Logged:
    pass

class Doc:
    info = '' # show if "info" is acrivate on index page
    index = '' # show on index page (in this page we can see...)
    single = '' # show each single page (this page show a platform...)
    empty = '' # show red if index page is empty in red
    advice = '' # show if index page is empty to advice user (in green)
    stranger = '' # show at user not authenticated
    success = '' # show if a new histance is generated withou errors
    error = '' # show if a new histance is not generated, because there are errors

class Test(Doc):
    index = """Hier you can test your sources c++. After this test you's gonna be know if you code compile on our platform."""
    success = 'Completed! You\'r code compile correctly on our system'
    error = 'Oh no! there are errors in you code. Sorry but we cannot accept this file'

class Platform(Doc):
    info = 'A <b>Platform</b> is a simply device-model that a room rather have connected. '
    index = 'In this page you can see all our platforms that you can found in <b>rooms</b>. '
    empty = 'Sorry. In this moment there arent platforms registered in our system. '
    advice = 'Please, wait our admins...'

class Room(Doc):
    info = 'A <b>Room</b> is a space where there is platforms and you can test you code on this devices. '
    index = 'In this page you can see all our <b>rooms</b>. In each <b>room</b> there are different <b>platforms</b>. '
    empty = 'Sorry. In this moment there arent <b>rooms</b> registered in our system. '
    strnager = 'After you login, can select a room to create a new <b>experiment</b>. '

class Experiment(Doc, Logged):
    index = """In this pase you can see all your <b>experiments</b>. Each experiment can be
        <i style="padding: 4px" class="w3-round w3-theme-l3">unready</i> (There are more thing to do before testing it),
        <i style="padding: 4px" class="w3-round w3-theme">ready</i> when you want, we can add this experiment to our queue, so test it, 
        <i style="padding: 4px" class="w3-round w3-theme-d3">freeze</i>: you cannot apport modified until test is not finished"""
    empty = 'Oh, geez! You haven\'t created anyhing'
    advice = 'You can go on Rooms\'s page and create a new experiment'