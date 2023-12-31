from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import home, communication_list, communication_detail, my_question, my_answer, question_create, answer_create, answer_list,test,getList, create_comment,getMyList,getAnswerList


app_name = 'communicationApp'

urlpatterns = [
    path('home', home, name="home"),
    path('communication_list', communication_list, name='communication_list'), #소통게시판 메인
    path('communication_detail/<int:question_id>', communication_detail, name='communication_detail'), #소통게시판 메인_질문하나 클릭하면 나오는 화면
    path('my_question', my_question, name='my_question'), #내가 한 질문
    path('my_answer', my_answer, name='my_answer'), #내가 한 답변
    path('question_create', question_create, name='question_create'), #질문하기_작성할때
    path('answer_create/<int:question_id>', answer_create, name='answer_create'), #답변하기_작성할때
    path('answer_list', answer_list, name='answer_list'), #답변하기_리스트
    path('test', test, name="test"),
    path('create_comment/<int:question_id>', create_comment, name="create_comment"),
    path('getList', getList, name="getList"),
    path('getMyList', getMyList, name="getMyList"),
    path('getAnswerList', getAnswerList, name="getAnswerList")
    
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    