from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers


class BaseSerializer(FlexFieldsModelSerializer):
    role_based_fields = None
    pass


class BaseListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        objs = [self.context["view"].model(**i) for i in validated_data]
        return self.context["view"].model.objects.bulk_create(objs)


from app_auth.models import User


class BaseModelSerializer(FlexFieldsModelSerializer):
    def __init__(self, *args, **kwargs):
        # read_only_fields = kwargs.pop("read_only_fields", None)
        excluded_fields = kwargs.pop("excluded_fields", None)
        kwargs.pop("roles", None)

        super(BaseModelSerializer, self).__init__(*args, **kwargs)

    class Meta:
        list_serializer_class = BaseListSerializer


class FilterParamSerializer(serializers.Serializer):
    field_name = serializers.CharField(max_length=256, required=True)
    operator = serializers.CharField(max_length=256, default="exact")
    value = serializers.CharField(max_length=5000, required=True)

    def validate(self, data, *args, **kwargs):
        self.available_fields = [
            i.name for i in self.context["model"]._meta.get_fields()
        ]
        if data["operator"] not in self.context["model"].valid_operators:
            raise serializers.ValidationError(
                f"{data['operator']} is not in valid operators of {self.context['model'].__name__}. "
                f"Valid operators: {self.context['model'].valid_operators}"
            )
        # if data["field_name"] not in self.available_fields:
        #     raise serializers.ValidationError(
        #         f"Cannot resolve field name \"{data['field_name']}\". Choices are {self.available_fields}"
        #     )
        return data
