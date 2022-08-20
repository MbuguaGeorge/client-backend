from rest_framework import serializers
from orders.models import Academic_Writing, Academic_Writing_Detail, Academic_Writing_Requirement

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academic_Writing_Detail
        fields = ('paper_type', 'subject', 'pages')

    def save(self):
        detail = Academic_Writing_Detail (
            paper_type = self.validated_data['paper_type'],
            subject = self.validated_data['subject'],
            pages = self.validated_data['pages'],
        )
        return detail

class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academic_Writing_Requirement
        fields = ('instructions', 'instruction_file', 'paper_format', 'references')

    def save(self):
        requirement = Academic_Writing_Requirement (
            instructions = self.validated_data['instructions'],
            instruction_file = self.validated_data['instruction_file'],
            paper_format = self.validated_data['paper_format'],
            references = self.validated_data['references'],
        )

class SummarySerializer(serializers.ModelSerializer):
    details = DetailSerializer(many=True)
    requirements = RequirementSerializer(many=True)

    class Meta:
        model = Academic_Writing
        fields = '__all__'

    def save(self):
        # summary = Academic_Writing (
        #     order_type = self.validated_data['order_type'],
        #     academic_year = self.validated_data['academic_year'],
        #     deadline = self.validated_data['deadline'],
        #     paper_level = self.validated_data['paper_level'],
        #     upgrade = self.validated_data['upgrade'],
        # )

        details_data = self.validated_data.pop('details')
        requirements_data = self.validated_data.pop('requirements')
        # det = Academic_Writing_Detail.objects.create()
        # req = Academic_Writing_Requirement.objects.create()
        summ = Academic_Writing.objects.create(**self.validated_data)
        for detail in details_data:
            Academic_Writing_Detail.objects.create(order_type=summ, **detail)

        for requirement in requirements_data:
            Academic_Writing_Requirement.objects.create(order_type=summ, **requirement)

        return summ