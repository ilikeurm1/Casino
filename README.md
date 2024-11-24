# Casino.py

## Configuration v1

The only configuration needed is `Main_Directory` which is a filepath pointing to the settings folder.

In the Settings.py file, edit:

```python
Main_Directory = os.getcwd() + r"\profiles\v1"
```

## Configuration v2+

Pretty much the same as v1 only your file is now saved in a **JSON** file instead of a txt file. Which makes it so there is 1 file for every user (as long as `Main_Directory` is the same).

## Configuration v4

For the settings file it's still the same as v2 but now you have a few customisable settings in [settings.py](Versions\v4\settings.py) under the `CUSTUMIZABLE SETTINGS` region.
