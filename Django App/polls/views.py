from django.shortcuts import render, redirect
import pickle
import pandas as pd

# Create your views here.
def first(request):
    res = 0
    if request.method == 'POST':
        if request.POST.get('pred_button'):
            X = request.POST['X']
            Y = request.POST['Y']
            month = request.POST['month']
            day = request.POST['day']
            FFMC = request.POST['FFMC']
            DMC = request.POST['DMC']
            DC = request.POST['DC']
            ISI = request.POST['ISI']
            temp = request.POST['temp']
            RH = request.POST['RH']
            wind = request.POST['wind']
            rain = request.POST['year']


            df = pd.DataFrame({'X': int(X), 'Y': int(Y),
                   'month': month, 'day': day,
                   'FFMC': float(FFMC), 'DMC': float(DMC), 'DC': float(DC),
                   'ISI': float(ISI), 'temp': float(temp), 'RH': int(RH),
                   'wind': float(wind), 'rain': float(rain)}, index = [0])
            

            def preprocess_data(data):
                data['day'] = data['day'].map({'fri': 1, 'tue': 2, 'sat': 3, 'sun': 4, 'mon': 5, 'wed': 6, 'thu': 7})
                data['month'] = data['month'].map(
                    {'mar': 1, 'oct': 2, 'aug': 3, 'sep': 4, 'apr': 5, 'jun': 6, 'jul': 7, 'feb': 8, 'jan': 9,
                     'dec': 10, 'may': 11, 'nov': 12})


                scale = pickle.load(open('/home/abdelmoneim/سطح المكتب/projects in python/on git hub/predict forest fires/scalling.pickle', 'rb'))
                data = scale.transform(data)

                return data

            data = preprocess_data(df)
            print(data)
            # load the model from disk
            model = pickle.load(open('/home/abdelmoneim/سطح المكتب/projects in python/on git hub/predict forest fires/ForestModel.pickle', 'rb'))

            res = model.predict(data)

        else:
            return redirect('homepage')
    else:
        pass

    return render(request, 'index.html', {'result': res})


def helper(x):
    if x == 0:
        return [0, 0]
    elif x == 2:
        return [1, 0]
    else:
        return [0, 1]