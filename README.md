# Starter Template for Django REST API

A Django REST API starter template with the following features:

- Django DRF (of course)
- JWT authentication with `django-rest-framework-simplejwt`
- S3 file storage with `django-storages` and `boto3`
- CORS headers with `django-cors-headers`
- Swagger documentation with `drf-yasg`
- Custom user model
- Custom user manager
- Postgres database
- Pagination
- Filtering
- Expanding
- Sorting
- Custom exception handler
- Debug toolbar

And, sane defaults configured for the above features.

Pagination, filtering, expanding, and sorting are implemented
with [django-utilitas](https://pypi.org/project/django-utilitas/).
The package is no longer maintained on PyPi, so I have included the source code in the `utilitas` directory.
However, its documentation is still very useful, and I recommend reading
it [here](https://github.com/ninnroot/utilitas?tab=readme-ov-file#django-utilitas).

## Installation

Just clone the repository and install the dependencies.

## Upgrading packages

The packages in `requirements.txt` are pinned to specific versions. To upgrade the packages, run the following command:

```bash
pip install pip-review
pip-review --interactive
```
