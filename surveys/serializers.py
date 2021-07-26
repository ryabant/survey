from rest_framework import serializers

from .models import Question, Survey, Choice, Answer


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ("text",)


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, required=False)

    class Meta:
        model = Question
        fields = ("id", "text", "type_of_answer", "survey", "choices")

    def validate(self, data):
        if data["type_of_answer"] == "Text" and "choices" in self.initial_data:
            raise serializers.ValidationError(
                "Wrong type of answer for choices. Try 'One' or 'Many'."
            )
        return data

    def create(self, validated_data):

        if self.data["type_of_answer"] == "Text":
            question = Question.objects.create(**validated_data)
            return question
        try:
            choices = validated_data.pop("choices")
        except KeyError:
            question = Question.objects.create(**validated_data)
            Choice.objects.create(question=question, text="Example 1")
        else:
            question = Question.objects.create(**validated_data)
            if len(choices) == 0:
                Choice.objects.create(question=question, text="Example 1")
            else:
                for choice in choices:
                    Choice.objects.get_or_create(question=question, **choice)
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
            if "text" in data:
                raise serializers.ValidationError("text field is not required")
            if "choices" not in self.initial_data or len(data["choices"]) == 0:
                raise serializers.ValidationError("choices field is required")
        else:
            if "choices" in self.initial_data:
                raise serializers.ValidationError("choices is not required")
            if "text" not in data:
                raise serializers.ValidationError("text field is required")
        return data

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
