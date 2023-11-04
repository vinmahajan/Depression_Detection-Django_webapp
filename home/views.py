from django.shortcuts import render, HttpResponse
from . depdet_script import depression_detection

#depression_detection=depdet_script.depression_detection()
# Create your views here.
def index(request):
    return HttpResponse('This is home page')

def about(request):
    return HttpResponse('This is about page')
    
def depdet(request):

    return render(request, 'index.html')
    #return HttpResponse('This is depdet page')

def ddresult(request):
    print(request.POST)
    username=request.POST['username'] 

    user_data=depression_detection.down_tweets(username)
    cleaned_data=depression_detection.df_cleaner(user_data)
    predict=depression_detection.predict(cleaned_data)

    negatives=predict.tolist().count(1)
    positives=predict.tolist().count(0)

    if negatives > positives:
        user="Depressed"
        resultsuggestion="It seems like you are depressed, here Grandmaster Shifuji will help you..."
        video="https://www.youtube.com/embed/Dkq47BmvJ1k"
    
    else:
        user="Not Depressed"
        resultsuggestion="Congrats Your Are Not Depressed"
        video="https://youtu.be/XtLpjCzNPr8"
    negative_per=int(negatives*100/len(predict.tolist()))
    positive_per=int(positives*100/len(predict.tolist()))
    #print(f"{negative_per}% Negative & {positive_per}% Positive")
    
    return render(request, 'result.html', {'username':username, 'user': user, 'negative_per':negative_per, 'positive_per':positive_per,'resultsuggestion':resultsuggestion, 'video':video})
