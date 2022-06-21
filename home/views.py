from django.shortcuts import render
from .models import *
from django.http import JsonResponse
	
# Create your views here.
def home(request):
	Amenitie = Amenities.objects.all()
	context = {'Amenitie': Amenitie}
	return render(request, 'home.html', context)

def api_hotels(request):
	hotels_objs = Hotels.objects.all()
	price = request.GET.get('price')
	if price:
		hotels_objs = hotels_objs.filter(price__lte =price)


	Amenities = request.GET.get('Amenities')
	if Amenities:
		Amenities = Amenities.split(',')
		print('Amenities')
		em = []
		for e in Amenities:
			try:
				em.append(int(e))
			except Exception as e:
				pass

		hotels_objs = hotels_objs.filter(Amenities__in =em).distinct()
		



	payload = []
	for hotel_obj in hotels_objs:
		result = {}
		result['hotel_name']= hotel_obj.hotel_name
		result['hotel_description']= hotel_obj.hotel_description
		result['hotel_image']= hotel_obj.hotel_image
		result['hotel_price']=  hotel_obj.price
		payload.append(result)
	return JsonResponse(payload, safe=False)				