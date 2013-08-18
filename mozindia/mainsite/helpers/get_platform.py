import re


def get_platform(request):
    '''
    Get the best guess at the platform of the user.

    :param request: A Django request object.
    :type request: :class:`django.http.HttpRequest`

    :returns: One value of ('win', 'linux', 'osx')

    '''
    
