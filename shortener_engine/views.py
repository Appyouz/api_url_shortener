import random
from sqlite3 import IntegrityError
from rest_framework import serializers, status
from rest_framework.views import APIView
from .serializers import URLSerializer
from .models import URL
from rest_framework.response import Response

class URLView(APIView):
    def post(self, request):
        long_url = request.data.get('long_url')
        serializer = URLSerializer(data=request.data)
        base = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if serializer.is_valid():
            url_instance = serializer.save()

            try:
                id = url_instance.id
                short_key = ""
                while id > 0:
                    remainder = id % 62
                    id = id // 62
                    short_key = base[remainder] + short_key

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


