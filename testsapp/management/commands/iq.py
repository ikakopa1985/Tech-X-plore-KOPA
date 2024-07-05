import os
import openai
from django.core.management.base import BaseCommand
import json
from testsapp.models import *


class Command(BaseCommand):
    help = 'Import questions'

    def handle(self, *args, **kwargs):
        openai.api_key = 'sk-proj-cQmH71y3AV0RkDX0G0kWT3BlbkFJlQz4MVgkcLACyylEUHQ2'
        testTypeGenerate = input('''please select test type for generate Test: 
                                    1 - python 
                                    2 - IOS
                                    ''')
        if testTypeGenerate == '1':
            cat1 = 'PROGRAMMING'
            cat2 = 'PYTHON'
            cat3 = 'Intro'
            message_text = ''' write 1  test of programming language python with answers and correct answers and i want to
             receive  response  exectly like this example without 'test_python = '
                                {"testText":"question", 
                                "answers":[{"answer_text":"answer_text1", "is_correct":0}, {"answer_text":"answer_text2","is_correct":0}, 
                                {"answer_text":"answer_text3","is_correct":1}, {"answer_text":"answer_text4","is_correct":0}]}  
                                   '''
        elif testTypeGenerate == '2':
            cat1 = 'PROGRAMMING'
            cat2 = 'IOS'
            cat3 = 'Intro'
            message_text = ''' write 1  test of programming language IOS with answers and correct answers and i want to
             receive  response  exectly like this example without 'test_python = '
                                {"testText":"question", 
                                "answers":[{"answer_text":"answer_text1", "is_correct":0}, {"answer_text":"answer_text2","is_correct":0}, 
                                {"answer_text":"answer_text3","is_correct":1}, {"answer_text":"answer_text4","is_correct":0}]}  
                                   '''
        if not openai.api_key:
            self.stderr.write(self.style.ERROR('OPENAI_API_KEY environment variable not set.'))
            return

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": message_text}
                ],
                max_tokens=150
            )
            resp = f"{response['choices'][0]['message']['content']}"
            self.stdout.write(self.style.SUCCESS(resp))
        except openai.error.OpenAIError as e:
            self.stderr.write(self.style.ERROR(f"OpenAI API error: {str(e)}"))
        try:
            data = json.loads(resp)
            self.stdout.write(self.style.SUCCESS(data))
            test_text = data.get('testText')
            answers = data.get('answers', [])
            category3 = Category3.objects.get(name=cat3, category2__name=cat2, category2__category1__name=cat1)
            test_instance = Test.objects.create(
                test_origin=category3,
                testText=test_text,
                testImage='',
                testDescription=''
            )
            self.stdout.write(self.style.SUCCESS(test_instance.id))
            for answer_data in answers:
                if answer_data.get('is_correct') == 0:
                    is_correct_temp = False
                else:
                    is_correct_temp = True
                Answers.objects.create(
                        tests=test_instance,
                        answer_text=answer_data.get('answer_text'),
                        is_correct=is_correct_temp,
                        answers_image=''  # Update with actual image path if available
                )
            self.stdout.write(self.style.SUCCESS("Test Created successfully"))
        except Exception as e:
            # self.stderr.write(self.style.ERROR("Wrong Generated"))
            return False, f"Failed to create test record: {str(e)}"

