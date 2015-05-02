from accounts.models import User, TrainingAssistant, Trainee
from anonymizer import Anonymizer

class UserAnonymizer(Anonymizer):

    model = User

    attributes = [
        ('id', "SKIP"),
        ('email', "email"),
        ('password', "varchar"),
        ('last_login', "SKIP"),
        ('is_superuser', "SKIP"),
        ('firstname', "first_name"),
        ('lastname', "last_name"),
        ('middlename', "last_name"),
        ('nickname', "last_name"),
        ('maidenname', "last_name"),
        ('gender', "SKIP"),
        ('date_of_birth', "similar_date"),
        ('phone', "phonenumber"),
        ('is_active', "SKIP"),
        ('is_admin', "SKIP"),
        ('is_staff', "SKIP"),
    ]


class TrainingAssistantAnonymizer(Anonymizer):

    model = TrainingAssistant

    attributes = [
        ('id', "SKIP"),
        ('account_id', "SKIP"),
        ('active', "SKIP"),
        ('date_created', "SKIP"),
    ]


class TraineeAnonymizer(Anonymizer):

    model = Trainee

    attributes = [
        ('id', "SKIP"),
        ('account_id', "SKIP"),
        ('spouse_id', "SKIP"),
        ('active', "SKIP"),
        ('date_created', "SKIP"),
        ('type', "SKIP"),
        ('date_begin', "SKIP"),
        ('date_end', "SKIP"),
        ('TA_id', "SKIP"),
        ('mentor_id', "SKIP"),
        ('team_id', "SKIP"),
        ('house_id', "SKIP"),
        ('bunk_id', "SKIP"),
        ('married', "SKIP"),
        ('address_id', "SKIP"),
        ('self_attendance', "SKIP"),
    ]
