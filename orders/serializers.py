from rest_framework import serializers
from orders.models import Academic_Writing, Academic_Writing_Detail, Academic_Writing_Requirement

class DetailSerializer(serializers.ModelSerializer):
    fields_to_be_removed = ['paper_type', 'subject', 'charts', 'slides']

    class Meta:
        model = Academic_Writing_Detail
        fields = ('paper_type', 'subject', 'pages', 'charts', 'slides', 'order_type')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        for field in self.fields_to_be_removed:
            try:
                if rep[field] is None:
                    rep.pop(field)
            except KeyError:
                pass
        return rep

    def save(self):
        detail = Academic_Writing_Detail (
            paper_type = self.validated_data['paper_type'],
            subject = self.validated_data['subject'],
            pages = self.validated_data['pages'],
            charts = self.validated_data['charts'],
            slides = self.validated_data['slides'],
        )

        detail.save()
        return detail

class RequirementSerializer(serializers.ModelSerializer):
    fields_to_be_removed = ['instructions', 'instruction_file', 'paper_format', 'references']

    class Meta:
        model = Academic_Writing_Requirement
        fields = ('instructions', 'instruction_file', 'paper_format', 'references', 'order_type')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        for field in self.fields_to_be_removed:
            try:
                if rep[field] is None:
                    rep.pop(field)
            except KeyError:
                pass
        return rep

    def save(self):
        requirement = Academic_Writing_Requirement (
            instructions = self.validated_data['instructions'],
            instruction_file = self.validated_data['instruction_file'],
            paper_format = self.validated_data['paper_format'],
            references = self.validated_data['references'],
        )

        requirement.save()
        return requirement

class SummarySerializer(serializers.ModelSerializer):
    fields_to_be_removed = ['order_type', 'academic_year', 'deadline', 'paper_level', 'title', 'upgrade']

    details = DetailSerializer(many=True)
    requirements = RequirementSerializer(many=True)

    class Meta:
        model = Academic_Writing
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['details'] = {detail['id']: detail for detail in rep['details']}
        rep['requirements'] = {requirement['id']: requirement for requirement in rep['requirements']}
        for field in self.fields_to_be_removed:
            try:
                if rep[field] is None:
                    rep.pop(field)
            except KeyError:
                pass
        return rep

    def save(self):
        details_data = self.validated_data.pop('details')
        requirements_data = self.validated_data.pop('requirements')
        summ = Academic_Writing.objects.create(**self.validated_data)
        for detail in details_data:
            Academic_Writing_Detail.objects.create(order_type=summ, **detail)

        for requirement in requirements_data:
            Academic_Writing_Requirement.objects.create(order_type=summ, **requirement)

        summ.save()
        return summ