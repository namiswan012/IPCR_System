from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group == 'Admin_Dean' or group == 'Admin_Director':
                return redirect('admin_home')
            elif group == 'Superadmin':
                return redirect('superadmin_home')
            else:
                return redirect ('member_home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


