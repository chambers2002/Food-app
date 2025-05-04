from django.shortcuts import render

def budget_groceries(request):
    products = []
    product_query = request.GET.get('product')
    if product_query:
        # Placeholder product list
        products = [
            {"name": f"{product_query.title()} Brand A", "price": 1.00},
            {"name": f"{product_query.title()} Brand B", "price": 1.25},
        ]
    return render(request, "budgetgroceries/BudgetGroceries.html", {"products": products})


# Create your views here.
