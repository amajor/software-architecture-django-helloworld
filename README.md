# Lab 5

## Start App

Run the following command from inside the `helloworld` directory.

```shell
python manage.py runserver
```

### For an API Response

Open your browser at http://127.0.0.1:8000/api/

You should get this response:

```json
{"Message": "Hello World!"}
```

### For a Rendered Page

Then open your browser at the address http://127.0.0.1:8000/hello/

You should get a rendered web page.

### For a Personal Greeting

If there is a person's name stored in the database, you can view the greeting for that person.

http://127.0.0.1:8000/hello/1/

---

# Admin

## Add a Name

Get into the python shell.

```shell
python manage.py shell
```

Now we can interact with the model. The `>>> ` is your shell's prompt.

```shell
>>> from hello.models import Name
>>> Name.objects.all()
```

This will list all the name objects.

To add a new name we can define an object:

```shell
>>> n = Name(first_name_text="Alison", last_name_text="Major")
>>> n.save()
```

Access the attributes of your new object this way:

```shell
>>> n.id
1

>>> n.first_name_text
'Alison'

>>> n.last_name_text
'Major'
```

Addition methods provide us with more options now:

```shell
>>> from hello.models import Name
>>> n = Name.objects.get(id=1)

>>> n.first_name()
'Alison'

>>> n.last_name()
'Major'

>>> n.full_name()
'Alison Major'
```

## Admin Users

Create a superuser.

```shell
python manage.py createsuperuser
```

Follow the prompts.

Now start the development server again.

```shell
python manage.py runserver
```

Navigate to http://127.0.0.1:8000/admin/
