from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Article
from .forms import ArticleForm
from .forms import RegistrationForm
from django.contrib.auth.models import User
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout


class HomeView(ListView):
    model = Article
    template_name = "app/home.html"
    context_object_name = "articles"

    def get_queryset(self):
        return Article.objects.order_by("-id")[:2]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["page_title"] = "Home"
        context["page_description"] = "Welcome to our website."

        return context


class AboutView(View):
    def get(self, request):
        return render(
            request,
            "app/about.html",
            {
                "page_title": "About",
                "page_description": "About  our website."
            }
        )



class ArticleList(ListView):
    model = Article
    template_name = "app/articles.html"

class ArticleDetailView(DetailView):
    model = Article
    template_name = "app/article-detail.html"

class ArticleCreate(LoginRequiredMixin, CreateView):

    model = Article
    form_class = ArticleForm
    template_name = "app/article-create.html"
    success_url = reverse_lazy("article")

    def form_valid(self, form):
        article = form.save(commit=False)
        article.author=self.request.user
        article.save()
        return super().form_valid(form)




class ArticleUpdate(LoginRequiredMixin, UpdateView):
    model = Article
    form_class= ArticleForm
    template_name = "app/article-update.html"
    success_url = reverse_lazy("article")

    def get_queryset(self):
        return Article.objects.filter(author = self.request.user)

class ArticleDelete(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = "app/article-delete.html"
    success_url = reverse_lazy("article")

    def get_queryset(self):
        return Article.objects.filter(author = self.request.user)

class Registration(View):
    def get(self, request):
        form = RegistrationForm()
        return render(
            request,
            "app/register.html",
            {
                "form":form
            }

        )

    def post(self, request):
        form = RegistrationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            User.objects.create_user(
                username,
                email,
                password
            )
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/")

        return render(
            request,
            "app/register.html",
            {
                "form": form
            }
        )


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(
            request,
            "app/login.html",
            {
                "form" : form
            }
        )

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("/")
            form.add_error(
                None,
                "Неверный username или password"
            )
        return render(
            request,
            "app/login.html",
            {"form":form}
            )

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/")