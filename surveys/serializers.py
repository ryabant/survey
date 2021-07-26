from rest_framework import serializers

from .models import Question, Survey, Choice, Answer


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ("text", "question")


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ("id", "text", "type_of_answer", "survey", "choices")

    def validate(self, data):
        if data["type_of_answer"] == "Text" and self.initial_data["choices"]:
            raise serializers.ValidationError(
                "Wrong type of answer for choices. Try one or many"
            )
        return data

    def create(self, validated_data):
        choices = validated_data.pop("choices")
        question = Question.objects.create(**validated_data)
        if (
            self.data["type_of_answer"] == "One"
            or self.data["type_of_answer"] == "Many"
        ):
            if choices:
                for choice in choices:
                    Choice.objects.create(question=question, **choice)
            else:
                Choice.objects.create(question=question, text="Example 1")
        return question


class SurveySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Survey
        fields = ("id", "title", "description", "create_at", "questions")


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ("question", "text", "choices")

    def validate(self, data):
        type_of_answer = Question.objects.get(id=data["question"].id).type_of_answer
        if type_of_answer == "One" or type_of_answer == "Many":
            if "choices" not in self.initial_data or len(data["choices"]) == 0:
                raise serializers.ValidationError("choices field is required")
        else:
            if "text" not in data:
                raise serializers.ValidationError("text field is required")
        return data
