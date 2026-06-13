from rest_framework import serializers
from testapp.models.models import Category



class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    def create(self, validated_data):
        name = validated_data.get("name")

        if Category.objects.filter(name=name).exista():
            raise serializers.ValidationError(
                {"name": "Категория с таким названием уже существует."}
            )

        return super().create(validated_data)


    def update(self, instance, validated_data):
        name = validated_data.get("name", instance.name)

        if Category.objects.filter(name=name).exclude(pk=instance.pk).exists():
            raise serializers.ValidationError(
                {"name": "Категория с таким названием уже существует."}
            )

        return super().update(instance, validated_data)
