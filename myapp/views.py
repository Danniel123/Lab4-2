from django.http import HttpResponse, Http404
import datetime
from django.template.loader import get_template 
from django.template import Context 
from django.shortcuts import render_to_response, render, RequestContext
import MySQLdb
from myapp.models import Book,Author

def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
			authors = Author.objects.filter(Name = q)
			if not authors:
				error = True
			else:
				id = authors[0].AuthorID
				books = Book.objects.filter(AuthorID = id)
				return render_to_response('search_results.html',{'authors': authors, 'query': q, 'books': books})
    return render_to_response('search_form.html',{'error': error})
	
def details(request):
	p = request.GET['ISBN']
	books = Book.objects.filter(ISBN = p)
	x = books[0].AuthorID
	authors = Author.objects.filter(AuthorID = x)
	return render_to_response('details.html',{'books': books,'authors':authors})

def dele(request):
	r = request.GET['ISBN']
	books = Book.objects.filter(ISBN = r)
	books.delete()
	return render_to_response('delete.html')
	
	
def addbook(request):
	if request.GET:
		book = Book()
		book.ISBN = request.GET['ISBN']
		book.Title = request.GET['Title']
		book.AuthorID = request.GET['AuthorID']
		book.Publisher = request.GET['Publisher']
		book.PublishDate = request.GET['PublishDate']
		book.Price = request.GET['Price']
		
		id = Author.objects.filter(AuthorID = book.AuthorID)
		if not id:
			return render_to_response('author_not_exist.html')
		else:
			book.save()
		return render_to_response('add_finish.html')
	else:
		return render_to_response('addbook.html')
	

def addauthor(request):
	if request.GET:
 
		author = Author()
		author.AuthorID = request.GET['AuthorID']
		author.Name = request.GET['Name']
		author.Age = request.GET['Age']
		author.Country = request.GET['Country']
		author.save()
		return render_to_response('add_finish.html')
	else:
		return render_to_response('addauthor.html')
		
		
def editbook(request):
	isbn = request.GET['ISBN']
	books = Book.objects.get(ISBN = isbn)
	if request.POST:
		books.ISBN = request.POST['ISBN']
		books.Title = request.POST['Title']
		books.AuthorID = request.POST['AuthorID']
		books.Publisher = request.POST['Publisher']
		books.PublishDate = request.POST['PublishDate']
		books.Price = request.POST['Price']
		books.save()
		return render_to_response('edit_finish.html')
	else:
		return render_to_response('editbook.html',{'books':books})