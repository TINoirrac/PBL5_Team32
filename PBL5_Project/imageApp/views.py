import cv2
from django.http import JsonResponse
import numpy as np
from rest_framework.decorators import api_view


@api_view(['POST'])
def analyze_image(request):
    image_file = request.FILES.get('image')
    if image_file:
        image = cv2.imdecode(np.fromstring(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
        brightness = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY).mean()
        contrast = cv2.Laplacian(image, cv2.CV_64F).var()
        return JsonResponse({'brightness': brightness, 'contrast': contrast})
    return JsonResponse({'error': 'No image was uploaded.'})
