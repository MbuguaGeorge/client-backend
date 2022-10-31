from rest_framework import serializers
from orders.models import Academic_Writing

class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Academic_Writing
        fields = ('id', 'order_type', 'academic_year', 'deadline', 'paper_level', 'title', 'upgrade', 'paper_type', 'subject', 'pages', 'charts', 'slides', 'instructions', 'paper_format', 'references', 'programming_category', 'prog_language', 'task_size', 'amount', 'discipline', 'software', 'spacing')

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
            programming_category = self.validated_data['programming_category'],
            prog_language = self.validated_data['prog_language'],
            task_size = self.validated_data['task_size'],
            amount = self.validated_data['amount'],
            discipline = self.validated_data['discipline'],
            software = self.validated_data['software'],
        )

        details.save()
        return details