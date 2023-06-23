from django.urls import path
from .views import (
    ApplicationFormCreate,
    ApplicationFormRetrieve,
    ApplicationFormUpdate,
    AdmissionFormCreate,
    AdmissionFormRetrieve,
    AdmissionFormUpdate,
)

urlpatterns = [
    path(
        "application-form-create/",
        ApplicationFormCreate.as_view(),
        name="application-create",
    ),
    path(
        "admission-form-create/",
        AdmissionFormCreate.as_view(),
        name="admission-create",
    ),
    path(
        "application-form-update/<pk>",
        ApplicationFormUpdate.as_view(),
        name="application-update",
    ),
    path(
        "admission-form-update/<pk>",
        AdmissionFormUpdate.as_view(),
        name="admission-update",
    ),
    path(
        "application-form-retrive/<pk>",
        ApplicationFormRetrieve.as_view(),
        name="application-retrive",
    ),
    path(
        "admission-form-retrive/<pk>",
        AdmissionFormRetrieve.as_view(),
        name="admission-retrive",
    ),
]
