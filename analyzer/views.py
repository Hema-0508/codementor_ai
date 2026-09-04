from django.shortcuts import render


def analyze_code(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        language = request.POST.get('language')

        if not code or not code.strip():
            return render(request, 'analyze.html', {
                'error': 'Please enter some code to analyze.'
            })

        return render(request, 'analyze.html', {
            'code': code,
            'language': language
        })

    return render(request, 'analyze.html')