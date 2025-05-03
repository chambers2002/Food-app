from django.shortcuts import render

def budget_home(request):
    return render(request, 'budgetgroceries/BudgetGroceries.html')

def cheap_staples(request):
    return render(request, 'budgetgroceries/CheapStaples.html')

def weekly_deals(request):
    return render(request, 'budgetgroceries/WeeklyDeals.html')

def budget_calc(request):
    return render(request, 'budgetgroceries/BudgetCalculator.html')

def store_comparison(request):
    return render(request, 'budgetgroceries/StoreComparison.html')

# Create your views here.
