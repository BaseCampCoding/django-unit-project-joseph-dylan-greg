from django.urls import path
from django.conf.urls import url
from .views import (
    WelcomeView,
    SignUpView,
    HomeView,
    PythonView,
    DefinitionView,
    DailyReflectionView,
    WeeklyReflectionView,
    UnitReflectionView,
    ResourcesView,
    PrintView,
    IndexView,
    HtmlDefView,
    PythonDefView,
    IfView,
    ForView,
    WhileView,
    DictView,
    QuizListView,
    CategoriesListView,
    ViewQuizListByCategory,
    QuizUserProgressView,
    QuizMarkingList,
    QuizMarkingDetail,
    QuizDetailView,
    QuizTake,
    index,
    login_user,
    logout_user,
    VideoView,
)

urlpatterns = [
    path("", WelcomeView.as_view(), name="welcome"),
    path("home/", HomeView.as_view(), name="home"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("pqa/", PythonView.as_view(), name="pqa"),
    path("print/", PrintView.as_view(), name="print"),
    path("indexes/", IndexView.as_view(), name="indexes"),
    path("if/", IfView.as_view(), name="if"),
    path("for/", ForView.as_view(), name="for"),
    path("while/", WhileView.as_view(), name="while"),
    path("dict/", DictView.as_view(), name="dict"),
    path("definitions/", DefinitionView.as_view(), name="definition"),
    path("htmldef/", HtmlDefView.as_view(), name="htmldef"),
    path("pythondef/", PythonDefView.as_view(), name="pydef"),
    path("reflections/", DailyReflectionView.as_view(), name="daily_reflection"),
    path("weeklysummary/", WeeklyReflectionView.as_view(), name="weekly_summary"),
    path("unitsummary/", UnitReflectionView.as_view(), name="unit_summary"),
    path("resources/", ResourcesView.as_view(), name="resource"),
    path("videos/", VideoView.as_view(), name="videos"),
    url(regex=r"^$", view=index, name="index"),
    url(regex=r"^login/$", view=login_user, name="login"),
    url(regex=r"^logout/$", view=logout_user, name="logout"),
    url(regex=r"^cards/$", view=QuizListView.as_view(), name="quiz_index"),
    url(
        regex=r"^category/$",
        view=CategoriesListView.as_view(),
        name="quiz_category_list_all",
    ),
    url(
        regex=r"^category/(?P<category_name>[\w|\W-]+)/$",
        view=ViewQuizListByCategory.as_view(),
        name="quiz_category_list_matching",
    ),
    url(
        regex=r"^progress/$", view=QuizUserProgressView.as_view(), name="quiz_progress"
    ),
    url(regex=r"^marking/$", view=QuizMarkingList.as_view(), name="quiz_marking"),
    url(
        regex=r"^marking/(?P<pk>[\d.]+)/$",
        view=QuizMarkingDetail.as_view(),
        name="quiz_marking_detail",
    ),
    #  passes variable 'quiz_name' to quiz_take view
    url(
        regex=r"^(?P<slug>[\w-]+)/$",
        view=QuizDetailView.as_view(),
        name="quiz_start_page",
    ),
    url(
        regex=r"^(?P<quiz_name>[\w-]+)/take/$",
        view=QuizTake.as_view(),
        name="quiz_question",
    ),
]