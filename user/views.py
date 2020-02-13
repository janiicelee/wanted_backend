import json
import bcrypt
import jwt

from wanted.settings  import SECRET_KEY
from django.views     import View 
from django.http      import JsonResponse
from django.db        import IntegrityError
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from .models import User


class UserView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if len(data['password']) < 5:
                return JsonResponse({'message':'SHORT_PASSWORD'}, status = 400)
            
            validates_email(data['email'])
            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

            User(
                name = data['name'],
                email = data['email'],
                password = hashed_password.decode('utf-8')
            ).save()

            return JsonResponse({'message':'SUCCESS'}, status = 200)

        except KeyError:
            return JsonResponse({'message':'INVALID_KEYS'}, status = 400)
        
        except IntegrityError:
            return JsonResponse({'message':'EMAIL_ALREADY_EXIST'}, status = 400)
        
        except TypeError:
            return JsonResponse({'message':'WRONG_INPUT_VALUE'}, status = 400)

        except ValidationError:
            return JsonResponse({'message':'NOT_AN_EMAIL'}, status = 400)
