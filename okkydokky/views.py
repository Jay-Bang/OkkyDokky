from django.shortcuts import render, redirect
from .models import DataStats, CodeStats, QuestionTable, Customer
from django.db.models import Q
import json
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
import math
# from datetime import datetime

# before_time = datetime.now()
# after_time = datetime.now()
# cal_time= after_time - before_time
# print(cal_time)

def homeView(request):
    qs1 = DataStats.objects.all()
    qs2 = CodeStats.objects.all()

    years = []
    total_datas = []
    no_answers = []
    answers = []
    unchecked_answers = []
    checked_answers = []
    answer_ratios = []
    checked_answer_ratios = []
    checked_answer_ratios = []
    code_languages = []
    total_useds = []


    for q in qs1:
        years.append(q.year)
        total_datas.append(q.total_data)
        no_answers.append(q.no_answer)
        answers.append(q.answer)
        unchecked_answers.append(q.unchecked_answer)
        checked_answers.append(q.checked_answer)
        answer_ratios.append(q.answer_ratio)
        checked_answer_ratios.append(q.checked_answer_ratio)

    for q in qs2[0:10]:
        code_languages.append(q.code_language)
        total_useds.append(q.total_used)

    context = {
        'years': years,
        'total_datas': total_datas, 
        'no_answers': no_answers, 
        'answers': answers, 
        'unchecked_answers': unchecked_answers, 
        'checked_answers': checked_answers, 
        'answer_ratios': answer_ratios, 
        'checked_answer_ratios': checked_answer_ratios,
        'code_languages': code_languages, 
        'total_useds': total_useds
        }

    return render(request, 'okkydokky/home.html', context)

def boardView(request):
    if request.is_ajax():
        context = serializedQS(request)

        return HttpResponse(json.dumps(context), content_type='application/json')
    return render(request, 'okkydokky/board.html')

def mypageView(request, user):
    if request.is_ajax():
        context = serializedQS(request)

        return HttpResponse(json.dumps(context), content_type='application/json')
    return render(request, 'okkydokky/mypage.html')

def serializedQS(request):
            
    getValueTask = getValue(request)

    searchTask = searchItem(
        getValueTask['limit'], 
        getValueTask['page'], 
        getValueTask['startData'], 
        getValueTask['endData'], 
        getValueTask['searchKeyword'], 
        getValueTask['conditionVal'], 
        getValueTask['request'], 
        getValueTask['myPage']
        )

    pageInfo = pagination(
        getValueTask['limit'], 
        getValueTask['page'], 
        searchTask['totalData']
        )

    qs = searchTask['qs']
    page = getValueTask['page']
    totalData = searchTask['totalData']
    noAnswer = searchTask['noAnswer']
    unCheckedAnswer = searchTask['unCheckedAnswer']
    checkedAnswer = searchTask['checkedAnswer']
    totalPage = searchTask['pageCount']
    startRange = pageInfo['startRange']
    endRange = pageInfo['endRange']
    preEndRange = pageInfo['prevEndRange']
    nextStartRange = pageInfo['nextStartRange']
    myPage = getValueTask['myPage']

    qslist =[]
    for q in qs:
        qlist = [
            q.id, 
            q.post_url, 
            q.post_title, 
            q.total_comment, 
            str(q.post_datetime)[:-6],
            q.post_content, 
            (q.post_component).split('$'), 
            (q.code_lang)[1:30].split('$'), 
            q.checked_answer, 
            str(q.answer_datetime)[:-6],
            q.post_url.split('/')[4], 
            ]
        qslist.append(qlist)
    
    context = {
        'qslist': qslist, 
        'page': page, 
        'totalData': totalData, 
        'totalPage': totalPage, 
        'startRange': startRange, 
        'endRange': endRange, 
        'preEndRange': preEndRange, 
        'nextStartRange': nextStartRange,
        'myPage': myPage,
        'noAnswer': noAnswer,
        'unCheckedAnswer': unCheckedAnswer,
        'checkedAnswer': checkedAnswer
        }


    return context

def logIn(request):
    user = request.user.is_authenticated
    if user:
        return render(request, 'okkydokky/home.html')
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('okkydokky:board')
            else:
                return redirect('okkydokky:login')
        else:
            return redirect('okkydokky:login')

    return render(request, 'okkydokky/login.html')

def logOut(request):
    user = request.user.is_authenticated

    if user:
        logout(request)
        return redirect('okkydokky:board')
    else:
        return redirect('okkydokky:login')

def signUp(request):
    user = request.user.is_authenticated

    if user:
        return render(request, 'okkydokky/login.html')
         
    if request.POST:
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        
        if User.objects.filter(username=username):
            return render(request, 'okkydokky/signup.html')
        elif username and password:
            password = make_password(password)
            User.objects.create(
                password=password,
                username=username
            )
            return redirect('okkydokky:login')
    return render(request, 'okkydokky/signup.html')

def deleteAccount(request):
    user = request.user.is_authenticated
    
    if request.POST:
        if user:
            user = request.user
            username = request.POST.get('username',None)
            password = request.POST.get('password',None)
            
            password = check_password(password, user.password)

            if User.objects.filter(username=username) and password:
                User.objects.get(username=username).delete()
            return redirect('../../okkydokky/board')
            
    return render(request,'okkydokky/delete.html')

def scrapPost(request, pk):
    user = request.user.is_authenticated

    if user:
        userid = request.user.id

        user = User.objects.get(id=userid)
        customer = Customer.objects.filter(user=user)
        if customer:
            customer = Customer.objects.get(user=user)
        else:
            Customer.objects.create(user=user)
            customer = Customer.objects.get(user=user)

        questiontable = QuestionTable.objects.get(id=pk)
        
        questiontable.customer.add(customer)

        message = '저장되었습니다.'
        context ={
            'message':message
        }

        return HttpResponse(json.dumps(context), content_type='application/json')

def deletePost(request, pk):
    user = request.user.is_authenticated

    if user:
        userid = request.user.id

        user = User.objects.get(id=userid)
        customer = Customer.objects.filter(user=user)
        if customer:
            customer = Customer.objects.get(user=user)
        else:
            Customer.objects.create(user=user)
            customer = Customer.objects.get(user=user)

        questiontable = QuestionTable.objects.get(id=pk)
        
        questiontable.customer.remove(customer)

        message = '삭제되었습니다.'
        context ={
            'message':message
        }

        return HttpResponse(json.dumps(context), content_type='application/json')

def getValue(request):
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    searchKeyword = request.GET.get('searchKeyword', None)
    conditionVal = request.GET.get('conditionVal')
    myPage = request.GET.get('check', None)
    if myPage == None:
        myPage = False
    else:
        myPage = True
    
    startData = (int(page)-1) * int(limit)
    endData = startData + int(limit)

    searchTask = searchItem(limit, page, startData, endData, searchKeyword, conditionVal, request, myPage)

    context = {
        'limit': limit, 
        'page': page, 
        'startData': startData, 
        'endData': endData,
        'searchKeyword': searchKeyword, 
        'conditionVal': conditionVal, 
        'searchTask': searchTask,
        'request': request,
        'myPage': myPage
        }

    return context

def searchItem(limit, page, startData, endData, searchKeyword, conditionVal, request, myPage):
    user = request.user.is_authenticated
    
    if myPage:
        if user:
            userid = request.user.id

            user = User.objects.get(id=userid)
            customer = Customer.objects.filter(user=user)

            if customer:
                customer = Customer.objects.get(user=user)
            else:
                Customer.objects.create(user=user)
                customer = Customer.objects.get(user=user)

            qs = QuestionTable.objects.filter(customer=customer)
    else:
        qs = QuestionTable.objects.all()

    if searchKeyword == '' or None:
        qs = qs.order_by('-post_datetime')

    elif searchKeyword:
        if conditionVal == 'and':
            qs = andSearch(qs, searchKeyword)
            qs = qs.order_by('-answer_datetime', '-post_datetime')
        elif conditionVal == 'or':
            qs = orSearch(qs, searchKeyword)
            qs = qs.order_by('-answer_datetime', '-post_datetime')
    
    totalAnswer = answerCount(qs)
    print(totalAnswer)
    totalData = qs.count()
    qs = qs[startData:endData]
    

    paginator = pagination(limit, page, totalData)
    pageCount = paginator['totalPage']
    
    context = {
        'qs': qs,
        'totalData': totalData,
        'paginator': paginator,
        'pageCount': pageCount,
        'noAnswer': totalAnswer[0],
        'unCheckedAnswer': totalAnswer[1],
        'checkedAnswer': totalAnswer[2],
        }

    return context

def pagination(limit, page, totalData):
    totalPage = math.ceil(int(totalData) / int(limit))

    pageGroup = math.ceil(int(page) / int(limit))
    endRange = pageGroup * int(limit) #마지막 페이지 번호
    startRange = endRange - (int(limit) - 1) #첫번째 페이지 번호

    nextStartRange = endRange + 1 #다음페이지 시작 페이지 번호
    prevEndRange = startRange - 1 #이전페이지 마지막 페이지 번호

    if totalPage < int(limit):
        limit = totalPage
    if endRange > totalPage:
        endRange = totalPage
    
    context = {
        'totalPage': totalPage, 
        'startRange': startRange, 
        'endRange': endRange, 
        'prevEndRange': prevEndRange, 
        'nextStartRange': nextStartRange
        }

    return context

def andSearch(qs, searchKeyword):
    emptyqs = QuestionTable.objects.none()
    keywords = searchKeyword.split(' ')
    
    for keyword in keywords:
        filteredqs = qs.filter(
            Q(post_title__icontains=keyword) | 
            Q(post_content__icontains=keyword) | 
            Q(checked_answer__icontains=keyword)
        )
        qs = emptyqs.union(filteredqs)

    return qs

def orSearch(qs, searchKeyword):
    emptyqs = QuestionTable.objects.none()
    keywords = searchKeyword.split(' ')
    
    for keyword in keywords:
        filteredqs = qs.filter(
            Q(post_title__icontains=keyword) | 
            Q(post_content__icontains=keyword) | 
            Q(checked_answer__icontains=keyword)
        )
        emptyqs = emptyqs.union(filteredqs)

    return emptyqs

def answerCount(qs):
    #print(qs)
    no_answer = qs.filter(total_comment=0).count()
    unchecked_answer = qs.filter(total_comment__gt=0).filter(checked_answer__lt=0).count()
    checked_answer = qs.filter(checked_answer__gt=0).count()
    
    return_value = [no_answer, unchecked_answer, checked_answer]
    
    return return_value