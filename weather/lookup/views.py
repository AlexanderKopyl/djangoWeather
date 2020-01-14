from django.shortcuts import render


def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']

        api_request = requests.get(
            "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+ zipcode +"&distance=5&API_KEY=7A895D99-D8D7-42D1-B90A-08694937172E")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        return render(request, 'lookup/home.html', {'zipcode':zipcode,'api':api})
    else:
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=49098&distance=5&API_KEY=7A895D99-D8D7-42D1-B90A-08694937172E")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

    return render(request, 'lookup/home.html', {'api': api})


def about(request):
    return render(request, 'lookup/about.html', {})