from main.models import Category

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def account_alert(request):
    try:
        request.user.studentprofile
        return {}
    except:
        if not request.user.is_authenticated:
            return {}
        if request.user.is_staff:
            return {}
        return {
                'account_alert': 'Your account is not complete. Please fill in your details.'
            }
    