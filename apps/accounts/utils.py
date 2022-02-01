import random
import string
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.core.exceptions import ImproperlyConfigured
from django.core.validators import ValidationError

MAX_USERNAME_SUFFIX_LENGTH = 7
USERNAME_SUFFIX_CHARS = [string.digits] * 4 + [string.ascii_letters] * (
    MAX_USERNAME_SUFFIX_LENGTH - 4
)


def random_username(size=7, chars=string.ascii_uppercase + string.digits):

    return ''.join(random.choice(chars) for _ in range(size))


def filter_users_by_username(*username):
    ret = get_user_model()._default_manager.filter(
        **{
            'username'
            + "__in": [u.lower() for u in username]
        }
    )
    return ret


def generate_username_candidate(basename, suffix_length):
    max_length = MAX_USERNAME_SUFFIX_LENGTH
    suffix = "".join(
        random.choice(USERNAME_SUFFIX_CHARS[i]) for i in range(suffix_length)
    )
    return basename[0: max_length - len(suffix)] + suffix


def generate_username_candidates(basename):
    USERNAME_MIN_LENGTH = MAX_USERNAME_SUFFIX_LENGTH
    ret = []
    min_suffix_length = max(1, USERNAME_MIN_LENGTH - len(basename))
    max_suffix_length = MAX_USERNAME_SUFFIX_LENGTH
    for suffix_length in range(min_suffix_length, max_suffix_length):
        ret.append(generate_username_candidate(basename, suffix_length))
    return ret


def generate_unique_username(basename):

    candidates = generate_username_candidates(basename)
    existing_usernames = filter_users_by_username(*candidates).values_list(
        'username', flat=True
    )
    existing_usernames = set([n.lower() for n in existing_usernames])
    for candidate in candidates:
        if candidate.lower() not in existing_usernames:
            try:
                return candidate.lower()
            except ValidationError:
                pass

    raise ImproperlyConfigured("Unable to find a unique username")
