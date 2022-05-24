from django.conf import settings


def export_settings(request):
    return {
        "PRIMARY_COLOR": settings.PRIMARY_COLOR,
        "SECONDARY_COLOR": settings.SECONDARY_COLOR,
        "FAVICON_URL": settings.FAVICON_URL,
        "ADMIN_TITLE_PREFIX": settings.ADMIN_TITLE_PREFIX,
    }
