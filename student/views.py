from django.shortcuts import render,redirect
from .forms import RegistrationForm,UpdateUserForm,UpdateProfileFormVerified,UpdateProfileFormNotVerified
from .models import Profile
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.model_selection  import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.externals import joblib
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            display = 1
            title = 'Thank You!!'
            message = 'Your registration was Successful Please Login to continue!!'
            context = {'display': display, 'message': message, 'title': title}
            return render(request, 'home/homepage.html', context)
        '''display = 1
        title = 'OOPS!!'
        message = 'THERE WAS AN ERROR!!
        context = {'display': display, 'message': message, 'title': title}'''
        return render(request, 'registration/registration_form.html', {'form': form})

    else:
        form = RegistrationForm()
    return render(request, 'registration/registration_form.html', {'form': form})

def dashboard(request):
    user = request.user.id
    context = {'user': user, 'profile': request.user.profile}
    return render(request, 'home/dashboard.html', context)


def view_profile(request):
    context = {'user': request.user, 'profile': request.user.profile}
    return render(request, 'user/profile.html', context)


def update_profile(request):
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=request.user)
        if request.user.profile.verified:
            profile_form = UpdateProfileFormVerified(request.POST, request.FILES, instance=request.user.profile)
        else:
            profile_form = UpdateProfileFormNotVerified(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('student:view_profile')
    else:
        if request.user.profile.verified:
            user_form = UpdateUserForm(instance=request.user)
            profile_form = UpdateProfileFormVerified(instance=request.user.profile)
        else:
            user_form = UpdateUserForm(instance=request.user)
            profile_form = UpdateProfileFormNotVerified(instance=request.user.profile)
    profile = request.user.profile
    user = request.user
    context = {'user_form': user_form, 'profile_form': profile_form, 'profile': profile, 'user': user}
    return render(request, 'user/update_profile.html', context)

def cal(request):
     profile = request.user.profile
     x=profile.Languages
     x=x.lower()
     tt=x.split(',')
     count=0
     for i in tt:
        if(i=='html')or(i=='css')or(i=='bootstrap')or(i=='prolog'):
             count=count+1
        else:
            count=count+2
     return count

def pre_form(request):
    dataset = pd.read_csv('D:\collgp\prediction_portal\static\student.csv')
    dataset['co_cur'] = dataset['co_cur'].map({'yes': 1, 'no': 0})
    X = dataset.iloc[:, [1, 2, 3, 4]].values
    y = dataset.iloc[:, 5].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
    rclassifier = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=0)
    rclassifier.fit(X_train, y_train)
    y_pred = rclassifier.predict(X_test)
    # Making confusion matrix
    cn = confusion_matrix(y_test, y_pred)
    acc=accuracy_score(y_test, y_pred)
    # save model to disk
    joblib.dump(rclassifier,'student_model.pkl')
    # predict on saved model
    load_model = joblib.load('student_model.pkl')
    profile = request.user.profile
    xy = profile.cgpa
    yz = profile.projects
    zx = cal(request)
    print(zx)
    if profile.co_cur==True:
        mn=1
    else:
        mn=0
    print(mn)
    g = load_model.predict([[xy, yz, zx, mn]])
    g=g[0]
    g=g.item()
    print(g)
    print(acc)
    if(g==3):
             return render(request, 'home/3.html')
    if(g==2):
             return render(request, 'home/2.html')
    if(g==1):
             return render(request, 'home/1.html')
