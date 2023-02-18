from django.shortcuts import render

def frontpage(request):
    return render(request, 'core/frontpage.html')

def login(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage.html')
    else:
        form = SignUpForm()
    
    return render(request, 'core/login.html', {'form': form})