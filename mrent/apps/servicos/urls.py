from django.urls import include, path

from .views import servicos, marido, contratante

urlpatterns = [
    path('', servicos.home, name='home'),

    path('marido/', include(([
        path('', marido.QuizListView.as_view(), name='quiz_list'),
        path('interests/', marido.MaridoInterestsView.as_view(), name='marido_interests'),
        path('taken/', marido.TakenQuizListView.as_view(), name='taken_quiz_list'),
        path('quiz/<int:pk>/', marido.take_quiz, name='take_quiz'),
    ], 'servicos'), namespace='marido')),
    path('maridodealuguel', servicos.maridodealuguel, name='maridodealuguel'),

    path('contratante/', include(([
        path('', contratante.QuizListView.as_view(), name='quiz_change_list'),
        path('quiz/add/', contratante.QuizCreateView.as_view(), name='quiz_add'),
        path('quiz/<int:pk>/', contratante.QuizUpdateView.as_view(), name='quiz_change'),
        path('quiz/<int:pk>/delete/', contratante.QuizDeleteView.as_view(), name='quiz_delete'),
        path('quiz/<int:pk>/results/', contratante.QuizResultsView.as_view(), name='quiz_results'),
        path('quiz/<int:pk>/question/add/', contratante.question_add, name='question_add'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/', contratante.question_change, name='question_change'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/', contratante.QuestionDeleteView.as_view(), name='question_delete'),
    ], 'servicos'), namespace='contratante')),
]
