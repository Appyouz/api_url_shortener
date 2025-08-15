import random
from sqlite3 import IntegrityError
from rest_framework import  status
from rest_framework.views import APIView
from .serializers import URLSerializer
from .models import URL
from rest_framework.response import Response
from django.shortcuts import redirect

class URLView(APIView):
    def post(self, request):
        serializer = URLSerializer(data=request.data)
        base = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if serializer.is_valid():
            # Create an instance of the serializer
            url_instance = serializer.save()

            try:
                # get id from the instance after save
                id = url_instance.id
                short_key = ""

                # Run loop until id is greater than zero
                while id > 0:
                    # Find the remainder of the id divided by 62
                    remainder = id % 62

                    # get quotient 
                    id = id // 62
                    
                    # pass the unique generate base values to our short_key
                    short_key = base[remainder] + short_key

                # Pass and save the short key in url_instance
                url_instance.short_key = short_key
                url_instance.save()
            #TODO: Implement a fall back incase base-62 dont work
            except IntegrityError:
                # Fix the length and charaacter set that is base
                KEY_LENGTH = 6
                CHARACTER_SET = base

                # Check for it until a unique id shows up thus infinite loop
                while True:
                    random_key = ""

                    #generate a random key equal to key_length
                    for _ in range(KEY_LENGTH):
                        random_key += random.choice(CHARACTER_SET)

                    # Check if the ranomd_key exists in database
                    # If it doesnt exist add it to short_key, save and break
                    if not URL.objects.filter(short_key=random_key).exists():
                        url_instance.short_key = random_key
                        url_instance.save()
                        break


            final_serializer = URLSerializer(url_instance)

            return Response(final_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ShortUrlView(APIView):
    def get(self, request, short_key):
        try:
            url_instance = URL.objects.get(short_key=short_key)
            return redirect(url_instance.long_url)
        except URL.DoesNotExist:
            return Response({"error": "Short URL not found"}, status=status.HTTP_404_NOT_FOUND)
