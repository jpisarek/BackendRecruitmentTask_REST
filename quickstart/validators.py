# from django.core.exceptions import ValidationError
# from django.utils.translation import gettext_lazy as _
# from .models import Grade

# def validate_if_task_is_already_graded(grade):
#     grades = Grade.objects.all()
#     if any (grade.task_id == g.task_id & grade.candidate_id == g.candidate.id in g for g in grades):
#         raise ValidationError(
#             _('Task is already graded!'),
#             params={},
#         )