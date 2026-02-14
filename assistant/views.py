from .utils import extract_receipt_data  # Import your function!
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Expense
from .forms import ExpenseForm




@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    return render(request, 'assistant/list.html', {"expenses": expenses})


@login_required
def upload_receipt(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            # Save but not yet commit
            expense_instance = form.save(commit=False)
            expense_instance.user = request.user


            expense_instance.save()

            image_path = expense_instance.receipt_image.path


            merchant_name, total_amount = extract_receipt_data(image_path)

            # Save 
            expense_instance.merchant = merchant_name
            expense_instance.amount = total_amount
            expense_instance.save()

            return redirect("dashboard")
    else:
        form = ExpenseForm()

    return render(request, 'assistant/upload.html', {'form': form})


@login_required
def dashboard(request):
    expenses = Expense.objects.filter(user=request.user)


    print(f"Total expenses for {request.user}: {expenses.count()}")
    for exp in expenses:
        print(f"  - {exp.merchant}: ${exp.amount}")

    total_spent = sum(e.amount for e in expenses if e.amount)
    return render(request, "assistant/dashboard.html", {"expenses": expenses, "total_spent": total_spent})
