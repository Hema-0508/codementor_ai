from django.shortcuts import render
from .ai_service import explain_code


def analyze_code(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        language = request.POST.get('language')

        if not code or not code.strip():
            return render(request, 'analyze.html', {
                'error': 'Please enter some code to analyze.'
            })

        explanation = explain_code(code, language)

        return render(request, 'analyze.html', {
            'code': code,
            'language': language,
            'explanation': explanation
        })

    return render(request, 'analyze.html')