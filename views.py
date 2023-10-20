from random import choice
from django.shortcuts import render

# Create your views here.

def event_list()
    """    
    gets all events, total people associated with event and max for event and  clickable to register
    
    cookie for event (expires in 30 days anyway, or if event not in page list)    
    """

def register(request):
    """
    cookie for event (expires in 30 days anyway, or if event not in page list)

    gets:
    if already registered, doesn't display ability to register, although allows editing of numbers 
    or deleting registration (not coming any more)
    
    creates:
    associated with event
    codename
    (qr code)
    number of adults
    number of kids
    present 
    """

    nerf_names = (
        "N-strike", "Elite", "Vortex", "Rebelle", "Cyberstrike", "Fire", "Ice", "Zombie-Strike"
        "Rival", "Mega", "Accushot"
    )

    blaster_types = (
        "springer", "flywheel", "HAMP", "Airtank"
    )

    people_types = (
        "modder", "nerd", "ninja", "tank", "operator", "trooper", "grass snake", "walker", "grenadier"
    )
    name = f"{choice(nerf_names)}-{choice(blaster_types)}-{choice(people_types)}"
    # check that name isn't already in list
    # if it is, do it again

    context = {}
    return render(response, "register.html", context)

def admin_login(request):
    """
    logins created by me. No excuses. 
    redirects to admin_create
    """
    context = {}
    return render(response, "admin_login.html", context)

def admin_create(request):
    """
    if from a submitted page:
        update and display
    """
    
    """
    event model:
    name
    date
    time
    description
    conditions
    minor_supervision
    max
    
    display all events, clickable (goes to admin_event)

    """
    context = {}
    return render(response, "admin_create.html", context)

def admin_event(request):
    """
    find event with clicked name
    get:
    name
    date
    time
    description
    conditions
    minor_supervision
    max
    
    all of the above are editable instantly

    get: 
    all people associated with event
    display names

    each person can be marked as present or deleted

    whole event can be deleted

    link to scan page
    """    
    context = {}
    return render(response, "admin_login.html", context)

def scan_in(request):
    """
    with QR code:
    search for person by qr code and scan as present
    redirect to event
    """


def simple(request):
    """
    model for people exist.

    people can register, then they continue to see their own name, plus what they've agreed to and the number of people registered
    
    if cookie name matches one in DB, they can edit THAT entry. #

    If cookie exists, they can't even see the rest of the login stuff

    If cookie name no in list which comes from DB, delete cookie
     
    Cookie expires in one month


    I make an event. 
    people are the only thing we need to register
    Others can create. 
    I can delete via admin. 
    Simple. 
    """