import numpy as np
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import Event, Program, Information
from .serializers import EventSerializer, ProgramSerializer, UserSerializer
from .semantic_search import sentence_transformer

from sentence_transformers import util
from transformers import DistilBertTokenizer, DistilBertForQuestionAnswering, pipeline
import torch

model_name = 'distilbert-base-uncased-distilled-squad'
# tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased-distilled-squad')
# model = DistilBertForQuestionAnswering.from_pretrained('distilbert-base-uncased-distilled-squad')
qa_pipeline =  pipeline('question-answering', model=model_name, tokenizer=model_name)


# Create your views here.

class EventsListCreateView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class ProgramListView(generics.ListAPIView):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class InformationSearchView(generics.GenericAPIView):
    """Ищем по кодируемому тексту"""
    def post(self, request, format=None):
        question = request.data.get('question')
        if question:
            answers = []
            prob_answer = []
            question_vector = sentence_transformer.encode(question)
            for inf in Information.objects.all():
                sim = util.cos_sim(question_vector, np.array(inf.vector, dtype=np.float32))
                print(sim)
                if sim.item() > 0.75:
                    prob_answer.append(inf.text)
                # inputs = tokenizer(question, pa, return_tensors="pt")
            for pa in prob_answer:
                with torch.no_grad():
                    pa_answs = qa_pipeline(question=[question], context=pa)
                    answers.extend(pa_answs)

        return Response(answers)
                #     outputs = model(**inputs)
                #
                # answer_start_index = torch.argmax(outputs.start_logits)
                # answer_end_index = torch.argmax(outputs.end_logits)
                #
                # predict_answer_tokens = inputs.input_ids[0, answer_start_index: answer_end_index + 1]
                # tokenizer.decode(predict_answer_tokens)
