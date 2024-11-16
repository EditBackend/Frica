from django.shortcuts import render
from .models import Product, Category , Company
# Create your views here.

# 👉--------------------------------yordamchi funksiyalar--------------------------------------👈

def upperCase(categories1):
    categories = []
    for x in range(len(categories1)):
        name = categories1[x].name.upper()
        img1 = categories1[x].img1
        img2 = categories1[x].img2
        title = categories1[x].title.upper()
        description = categories1[x].description
        categories.append({
            'name': name,
            'img1': img1,
            'img2': img2,
            'title': title,
            'description': description,
        })

    return categories

def objectsFilter(slug, data, property):
    products = data.objects.filter(**{property: Category.objects.get(name=slug)})
    return products


def toliq(data):
    fulldata = data.objects.all().order_by('name')
    return fulldata






# 👉--------------------------------yordamchi funksiyalar end--------------------------------------👈

# 👉--------------------------------Pages--------------------------------------👈
def index(request):
    products = toliq(Product)

    categories1 = toliq(Category)
    companies = toliq(Company)
    laptop = objectsFilter('computers', Product, 'category')
    categoryName = "Computers & Laptop"
    categories = upperCase(categories1)
    print(categories1)

    context = {
        'products': products,
        'categories': categories,
        'companies': companies,
        'category': laptop,
        'categoryName': categoryName,
    }

    return render(request, 'pages/index.html', context =context)

def computers(request):
    computers = objectsFilter('computers', Product, 'category')
    categoryName = 'Computers & Laptop'
    category =  objectsFilter('computers', Category, 'name')
    context = {
        'computers': computers,
        'categoryName': categoryName,
        'category': category

    }
    return render(request, 'pages/computers.html', context = context)

def contact(request):
    return render(request, 'pages/contact.html', context = {})

def means_clothes(request):
    computers = objectsFilter('manclothes', Product, 'category')
    categoryName = 'Man Clothes'
    category = objectsFilter('manclothes', Category, 'name')
    context = {
        'computers': computers,
        'categoryName': categoryName,
        'category': category

    }
    return render(request, 'pages/mans_clothes.html', context =context)

def womans_clothes(request):
    computers = objectsFilter('womanclothes', Product, 'category')
    categoryName = 'Woman Clothes'
    category = objectsFilter('womanclothes', Category, 'name')
    context = {
        'computers': computers,
        'categoryName': categoryName,
        'category': category

    }
    return render(request, 'pages/womans_clothes.html', context = context)


# 👉--------------------------------Pages end--------------------------------------👈
# 👉--------------------------------category--------------------------------------👈

def category(request, slug):
    products = Product.objects.all().order_by('-name')
    categories1 = Category.objects.all()
    companies = Company.objects.all()
    laptop = products.filter(category=categories1.get(name=slug.lower()))
    categoryName = slug
    categories = []
    for x in range(len(categories1)):
        name = categories1[x].name.upper()
        img1 = categories1[x].img1
        img2 = categories1[x].img2
        categories.append({
            'name': name,
            'img1': img1,
            'img2': img2,

        })


    context = {
        'products': products,
        'categories': categories,
        'companies': companies,
        'category': laptop,
        'categoryName': categoryName,
    }
    return render(request, 'pages/index.html',context = context)

# 👉--------------------------------category end--------------------------------------👈

# 👉--------------------------------detail--------------------------------------👈

def detail(request, id):
    product = Product.objects.get(id=id)

    context = {
        'product': product,
    }
    return render(request, 'detail/detail.html', context = context)

# 👉--------------------------------detail end--------------------------------------👈






