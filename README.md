### This is educational project.
### Example of web chat, created with Django Framework and Django Channels package.

# Setup with Linux

First install docker yourself.

Then open shell and print

```
chmod +x ./setup.sh
./setup.sh
```

This will run redis daemon server, install Django2, Channels, make SQL migrations and run server.

After that, to run server again use
```
python3 ./manage.py runserver
```

# How to use

Open `http://127.0.0.1:8000` in browser.
