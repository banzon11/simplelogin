# Import necessary modules and functions
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib import messages

# Define the signup view
def signup(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # Create a form instance with the submitted data
        form = UserCreationForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            # Save the form data to the database
            form.save()
            # Get the username and password
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # Authenticate the user
            user = authenticate(username=username, password=raw_password)
            # Log the user in
            login(request, user)
            # Show a success message
            messages.success(request, 'You have successfully signed up!')
            # Redirect to the dashboard
            return redirect('dashboard')
        else:
            # Show an error message
            messages.error(request, 'Please correct the error below.')
    else:
        # Create a blank form
        form = UserCreationForm()
    # Render the signup template with the form
    return render(request, 'signup.html', {'form': form})

# Define the dashboard view
@login_required  # Require the user to be logged in
def dashboard(request):
    # Render the dashboard template
    return render(request, 'dashboard.html')

# Define a custom login view
class CustomLoginView(LoginView):
    template_name = 'login.html'  # Use the login template
    redirect_authenticated_user = True  # Redirect users who are already logged in

    # Define what happens when the form is valid
    def form_valid(self, form):
        # Show a success message
        messages.success(self.request, f'Welcome, {form.get_user().username}!')
        # Call the parent form_valid method
        return super().form_valid(form)

# Define a custom logout view
class CustomLogoutView(LogoutView):
    next_page = 'login'  # Redirect to the login page after logout
