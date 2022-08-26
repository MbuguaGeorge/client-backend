from rest_framework import serializers
from orders.models import Academic_Writing

class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Academic_Writing
        fields = '__all__'

    def save(self):
        details = Academic_Writing(
            order_type = self.validated_data['order_type'],
            academic_year = self.validated_data['academic_year'],
            deadline = self.validated_data['deadline'],
            paper_level = self.validated_data['paper_level'],
            title = self.validated_data['title'],
            upgrade = self.validated_data['upgrade'],
            paper_type = self.validated_data['paper_type'],
            subject = self.validated_data['subject'],
            pages = self.validated_data['pages'],
            charts = self.validated_data['charts'],
            slides = self.validated_data['slides'],
            instructions = self.validated_data['instructions'],
            # instruction_file = self.validated_data['instruction_file'],
            paper_format = self.validated_data['paper_format'],
            references = self.validated_data['references'],
        )

        details.save()
        return details