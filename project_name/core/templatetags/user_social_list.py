from django import template

register = template.Library()


@register.filter
def get_social_list(user): # Only one argument.
    result = []
    if user.is_authenticated():
        for account in user.socialaccount_set.all():
            result.append(account.provider)

    return result