class Auth:
    class Signup:
        email_exist = 'Email adress already registered in this app'
        password_different = 'Password and condifm of password are not equal'
        account_created = 'Account created correctly'
        

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
    index = 'Hier you can test your sources c++. After this test you\'s gonna be know if you code compile on our platform. '
    success = 'Completed! You\'r code compile correctly on our system'
    error = 'Oh no! there are errors in you code. Sorry but we cannot accept this file'

class Platform(Doc):
    info = 'A <b>Platform</b> is a simply device-model that a room rather have connected. '
    index = 'In this page you can see all our platforms that you can found in <b>rooms</b>. '
    empty = 'Sorry. In this moment there arent platforms registered in our system. '
    advice = 'Please, wait our admins...'
    created = 'New platform created!'
    class Action:
        created = 'New platform created!'
        edited = 'platform edited!'
        deleted = 'platform deleted!'

class Room(Doc):
    info = 'A <b>Room</b> is a space where there is platforms and you can test you code on this devices. '
    index = 'In this page you can see all our <b>rooms</b>. In each <b>room</b> there are different <b>platforms</b>. '
    empty = 'Sorry. In this moment there arent <b>rooms</b> registered in our system. '
    advice = 'Maibe any room are not exists'
    strnager = 'After you login, can select a room to create a new <b>experiment</b>. '
    class Action:
        created = 'New room created!'
        edited = 'Room edited!'
        deleted = 'Room deleted!'
        class Img:
            notValid = 'Sorry but we accept only image .png'

class Mount:
    empty = 'This room have\'t yet platforms'
    advice = 'Maybe insert a new platform in this room'


class ElementQ(Doc):
    index = 'In this page you can see all your experiment and the times to wait'
    empty = 'You haven\'t experiment yet in this queue '
    advice = 'Maibe any room are not exists'
    strnager = 'After you login, can select a room to create a new <b>experiment</b>. '

class Experiment(Doc, Logged):
    index = """In this page you can see all your <b>experiments</b>. Each experiment can be
        <i style="padding: 4px" class="w3-round w3-theme-d4">unready</i> (There are more thing to do before testing it),
        <i style="padding: 4px" class="w3-round w3-theme">ready</i> when you want, we can add this experiment to our queue, so test it, 
        <i style="padding: 4px" class="w3-round w3-theme-l4">freeze</i>: you cannot apport modified until test is not finished"""
    empty = 'Oh, geez! You haven\'t created anyhing'
    advice = 'You can go on Rooms\'s page and create a new experiment'
    single = 'In this page you can see this experiment. You can add some sources (.cpp) so decide where load ( in what platform ). Then you can start test. <b>This experiment will be freeze until it end</b>'
    noDuration = 'You have not select how many minutes is duration of this experiment'
    noDescription = 'Description of this experiment is not setted'
    class Action:
        created = 'New experiment created!'
        edited = 'Experiment edited!'
        deleted = 'Experiment deleted!'

    class Testbed:
        prepare = 'Are you gonna enqueue you experiment.'
        unready = 'Sorry but this experiment is not ready to test'
        notime = 'I don\'t know how many minutes do that'
        ready = 'Compliment! Now we are able to do that experiment'

idNotAdmin = 'Sorry! You have not permission to stay in this page. '

class User():
    account = 'This is you account. All your information are reserved'
    settings = 'In this page you can change you username or the color-theme. Only your account will be changed'

class Test:
    class Form:
        page = 'In this page you can compile a source.cpp and try to compile on our platform. Then know if code compile'
        ok = 'You\re code compile successfull'
        no = 'Sorry byt you\'re shutty code not worki'
    class File:
        page = 'In this page you can upload a zip file and testing it'
        ok = 'You code compile'
        no = 'This shit, sucks'
        nonZip = 'Sorry we accept only .zip files'

    
    