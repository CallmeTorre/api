# Api

The objective of this repository is creating a REST API with CRUD operations  (Create, Read, Update, Delete) using <a href="http://www.django-rest-framework.org">Django REST Framework</a>.

# Api's Schema

- `/restaurants/`: Here you can access to the main page of the Restaurant's API. 
- `/docs/`: Here you can find all the documentation of the API, and some examples of how to use it.
- `/schema/`: Here you can find the complete schema of the API.

## Examples

- GET ```curl --request GET \
  --url https://calm-wildwood-17330.herokuapp.com/restaurants/```
- POST '''curl --request POST \
  --url https://calm-wildwood-17330.herokuapp.com/restaurants/ \
  --header 'Content-Type: application/json' \
  --header 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  --form id=1 \
  --form rating=0 \
  --form 'name=Noa Noa' \
  --form site=http://Elnoanoa.com \
  --form email=juan@gabriel.com \
  --form phone=5546789097 \
  --form street=Elm \
  --form city=Kukaponga \
  --form state=Mexico \
  --form lat=19.909394798264 \
  --form long=-89.309103981'''
- PUT ```curl --request PUT \
  --url https://calm-wildwood-17330.herokuapp.com/restaurants/1/ \
  --header 'Content-Type: application/json' \
  --header 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  --form id=1 \
  --form rating=0 \
  --form 'name=El Nuevo Noa Noa' \
  --form site=http://Elnoanoa.com \
  --form email=juan@gabriel.com \
  --form phone=5546789097 \
  --form 'street=Hollywood Boulevard' \
  --form city=Kukaponga \
  --form state=Mexico \
  --form lat=19.909394798264 \
  --form long=-89.309103981```
- DELETE ```curl --request GET \
  --url https://calm-wildwood-17330.herokuapp.com/restaurants/1/```

If you want test my app using POSTMAN check this<a href="https://documenter.getpostman.com/view/1727394/api/RW1boKPb"> link</a>